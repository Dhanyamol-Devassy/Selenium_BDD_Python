import sys
import os
import subprocess
import argparse
import shutil
from dotenv import load_dotenv  # Optional for loading .env files
from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException

# Define the root directory of the project
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Define paths for reports and results
ALLURE_RESULTS_DIR = os.path.join(PROJECT_ROOT, 'reports', 'allure-results')
ALLURE_REPORT_DIR = os.path.join(PROJECT_ROOT, 'reports', 'allure-report')
SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT, 'reports', 'screenshots')

def run_command(command):
    """Runs a shell command and handles errors."""
    try:
        subprocess.run(command, cwd=PROJECT_ROOT, check=True)
    except FileNotFoundError:
        print(f"Error: Command '{command[0]}' not found. Make sure it is installed and accessible.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{' '.join(command)}' failed with exit code {e.returncode}")
        sys.exit(e.returncode)

def ensure_directory_exists(directory):
    """Creates a directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def run_behave(feature_file=None):
    """Runs Behave BDD tests."""
    print("Running Behave tests...")
    command = ['behave']
    if feature_file:
        command.append(feature_file)
    run_command(command)

def generate_allure_report():
    """Generates the Allure report from the test results."""
    print("Generating Allure report...")
    ensure_directory_exists(ALLURE_RESULTS_DIR)
    run_command(['allure', 'serve', ALLURE_RESULTS_DIR])

def clean_reports():
    """Cleans up old Allure results and screenshots."""
    print("Cleaning up reports...")
    for directory in [ALLURE_RESULTS_DIR, SCREENSHOTS_DIR]:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"Deleted: {directory}")
        else:
            print(f"Directory not found, skipping: {directory}")

def run_tests():
    """Runs unit tests using pytest."""
    print("Running unit tests...")
    run_command(['pytest'])

def setup_environment():
    """Sets up the environment for the tests."""
    print("Setting up environment...")
    env_path = os.path.join(PROJECT_ROOT, '.env')
    if os.path.exists(env_path):
        load_dotenv(env_path)
        print("Loaded environment variables from .env file")
    else:
        print(".env file not found, skipping...")

<<<<<<< HEAD
def start_selenium_browser():
    """Starts a Selenium WebDriver session and handles session creation errors."""
    try:
        print("Starting Selenium WebDriver...")
        driver = webdriver.Chrome()  # Adjust this based on your preferred browser/driver
        driver.get("https://example.com")  # Example URL to load
        return driver
    except SessionNotCreatedException as e:
        print(f"Error: Session not created. {str(e)}")
        print("This might be due to a mismatch between the WebDriver and browser version.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Unable to start browser. {str(e)}")
        sys.exit(1)
=======
def run_browser_tests():
    """Runs Selenium WebDriver tests with --user-data-dir argument."""
    print("Running Selenium WebDriver tests...")

    # Example for initializing Chrome WebDriver with --user-data-dir argument
    options = webdriver.ChromeOptions()
    #options.add_argument("--user-data-dir=/path/to/your/user/data")  # Specify the directory

    driver = webdriver.Chrome(options=options)

    # Your test logic here (e.g., navigating to a website)
    driver.get('http://example.com')
    print("Tests completed.")

    # Close the WebDriver after the test
    driver.quit()
>>>>>>> 245c59f4139f6ab73795b858d1b30450c89ab0e9

def main():
    """Main function to handle command-line commands."""
    parser = argparse.ArgumentParser(description="Manage the BDD project")
    parser.add_argument('command', nargs="?", help="Command to run (e.g., run, test, report, clean, setup)")

    parser.add_argument('--feature', help="Run a specific feature file")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        'run': lambda: run_behave(args.feature),
        'test': run_tests,
        'report': generate_allure_report,
        'clean': clean_reports,
        'setup': setup_environment,
        'start-selenium': start_selenium_browser  # Added Selenium command
    }

    if args.command in commands:
        commands[args.command]()
    else:
        print(f"Unknown command: {args.command}")
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
