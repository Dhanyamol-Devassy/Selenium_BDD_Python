import json
import os
import time
import shutil
import tempfile
import psutil
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import get_logger
from utils.driver_utils import DriverUtils

# Define the path to the config file in the root folder
config_path = os.path.join(os.getcwd(), 'config.json')

# Load configuration from JSON file
def load_config():
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def before_all(context):
    """Before any test starts."""
    try:
        # Initialize the logger before any logging actions
        context.logger = get_logger()
        
        # Now that the logger is initialized, proceed with other actions
        context.logger.info("Initializing test setup...")
        
        clean_up_directories(context)  # Ensure this action doesn't log before the logger is ready
        
        # Load configuration
        context.config = load_config()
        context.logger.info("Configuration loaded successfully.")
        
    except Exception as e:
        print(f"Error during before_all setup: {str(e)}")
        raise  # Reraise the exception to halt execution


def after_all(context):
    """After all tests finish."""
    try:
        context.logger.info("Test environment cleanup completed.")
    except Exception as e:
        print(f"Error during after_all cleanup: {str(e)}")

def before_scenario(context, scenario):
    """Before each scenario starts."""
    try:
        context.logger.info(f"*****************Starting scenario: {scenario.name}*****************")
        
        # Create a unique temporary user data directory for each scenario
        user_data_dir = tempfile.mkdtemp(prefix=f"user_data_{int(time.time())}_")  # Ensure unique directory
        context.user_data_dir = user_data_dir  # Store the path to clean up later
        
        context.logger.info(f"Created unique user data directory: {user_data_dir}")

        # Ensure that no existing Chrome processes are running
        os.system("pkill -f chrome")  # Forcefully kill any existing Chrome processes
        
        # Set up the WebDriver with the unique user data directory
        context.logger.info("Setting up WebDriver for scenario...")
        service = Service(ChromeDriverManager().install())  # Set up the Chrome WebDriver service
        options = webdriver.ChromeOptions()
        options.add_argument(f'--user-data-dir={user_data_dir}')
        options.add_argument(f'--profile-directory={int(time.time())}_profile')  # Unique profile directory
        options.add_argument('--disable-sync')  # Disable syncing to avoid data conflicts
        options.add_argument('--no-first-run')  # Prevent Chrome from creating default profile if it doesn't exist
        options.add_argument('--headless')  # Add headless if running in CI/CD to avoid UI popups

        # Launch the WebDriver with a clean session
        context.driver = webdriver.Chrome(service=service, options=options)  # Create the WebDriver instance
        context.driver.maximize_window()  # Maximize the browser window

        # Initialize the DriverUtils class with the driver and logger
        context.driver_utils = DriverUtils(context.driver, context.logger)
        context.logger.info("WebDriver setup complete.")
    except Exception as e:
        context.logger.error(f"Error in before_scenario: {str(e)}")
        raise  # Halt execution if setup fails

def after_scenario(context, scenario):
    """After each scenario finishes."""
    try:
        if scenario.status == 'failed':
            if hasattr(context, 'driver') and context.driver:
                capture_screenshot(context.driver, context.logger)
                context.logger.info(f"Screenshot captured for failed scenario: {scenario.name}")
            else:
                context.logger.warning("No WebDriver available to capture screenshot.")
                
        context.logger.info(f"*****************Finished scenario: {scenario.name}*****************")
    except Exception as e:
        context.logger.error(f"Error in after_scenario for scenario '{scenario.name}': {str(e)}")
    finally:
        if hasattr(context, 'driver') and context.driver:
            try:
                context.driver.quit()
                context.logger.info("WebDriver closed.")
            except Exception as cleanup_error:
                context.logger.error(f"Error during WebDriver cleanup: {str(cleanup_error)}")
        
        # Clean up the temporary user data directory
        if hasattr(context, 'user_data_dir') and os.path.exists(context.user_data_dir):
            try:
                shutil.rmtree(context.user_data_dir)
                context.logger.info(f"Temporary user data directory '{context.user_data_dir}' cleaned up.")
            except Exception as cleanup_error:
                context.logger.error(f"Error during cleanup of user data directory: {str(cleanup_error)}")

def kill_chrome_processes():
    """Kill any remaining Chrome processes to avoid user data directory being in use."""
    for proc in psutil.process_iter(['pid', 'name']):
        if 'chrome' in proc.info['name'].lower():
            try:
                proc.kill()
                print(f"Killed process {proc.info['name']} with PID {proc.info['pid']}")
            except psutil.NoSuchProcess:
                pass  # Process has already been terminated


def capture_screenshot(driver, logger):
    """Capture a screenshot for failed steps."""
    try:
        screenshot_dir = os.path.join(os.getcwd(), 'reports/screenshots')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)  # Create directory if it doesn't exist

        screenshot_path = os.path.join(screenshot_dir, f'{int(time.time())}.png')
        driver.save_screenshot(screenshot_path)
        logger.error(f"Screenshot saved: {screenshot_path}")
    except Exception as e:
        logger.error(f"Error capturing screenshot: {str(e)}")

def before_step(context, step):
    """Before each step starts."""
    try:
        context.logger.info(f"Starting step: {step.name}")
    except Exception as e:
        context.logger.error(f"Error in before_step: {str(e)}")

def after_step(context, step):
    """After each step finishes."""
    try:
        if step.status == 'failed':
            if hasattr(context, 'driver') and context.driver:
                capture_screenshot(context.driver, context.logger)
                context.logger.info(f"Screenshot captured for failed step: {step.name}")
            else:
                context.logger.warning("No WebDriver available to capture screenshot.")
        context.logger.info(f"Step '{step.name}' finished with status: {step.status}")
    except Exception as e:
        context.logger.error(f"Error in after_step for step '{step.name}': {str(e)}")


def clean_up_directories(context):
    """Clean up the necessary directories."""
    try:
        # Define paths to the directories you want to clean
        directories_to_clean = [
            'reports/allure-results',  # Allure results directory
            'reports/screenshots',      # Screenshots directory
            'allure-results/',
            'reports/allure-report'     # Log files directory (if any)
        ]
        
        # Loop through each directory and remove its contents
        for dir_path in directories_to_clean:
            if os.path.exists(dir_path):
                # Remove all files and subdirectories inside the directory
                for root, dirs, files in os.walk(dir_path, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        shutil.rmtree(os.path.join(root, name))
                context.logger.info(f"Cleaned up directory: {dir_path}")
            else:
                context.logger.warning(f"Directory does not exist: {dir_path}")
    except Exception as e:
        context.logger.error(f"Error cleaning up directories: {str(e)}")
