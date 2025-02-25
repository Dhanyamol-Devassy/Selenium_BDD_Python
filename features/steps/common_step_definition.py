import random
import string
import os
from behave import *
from selenium.webdriver.common.by import By
from xpath_files.common_xpaths import CommonXPaths
from utils.driver_utils import DriverUtils

# Utility Functions
def generate_unique_name():
    """Generate a random name with a capitalized first letter."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)).capitalize()

def generate_unique_email(name):
    """Generate a unique email address using the given name."""
    return f"{name.lower()}@example.com"

@When("The user clicks {string} button with link")
def step_impl(context, string):
    """Clicks a button with a given label on the homepage."""
    try:
        xpath = CommonXPaths.buttons_with_text_home_page % string
        context.driver_utils.click_element(By.XPATH, xpath)
        context.logger.info(f"Clicked the '{string}' button on the home page.")
    except Exception as e:
        context.logger.error(f"Error clicking the '{string}' button: {e}")
        raise

@Then("The {string} section should be visible")
def step_impl(context, string):
    """Verify that a specific section is visible on the page."""
    try:
        xpath = CommonXPaths.text_messages_for_section % string
        if context.driver_utils.is_element_present(By.XPATH, xpath):
            context.logger.info(f"The section '{string}' is visible.")
        else:
            raise AssertionError(f"The section '{string}' should be visible, but it is not.")
    except Exception as e:
        context.logger.error(f"Error verifying visibility of section '{string}': {e}")
        raise

@When("The user clicks on {string} button")
def step_impl(context, string):
    """Clicks a button with a specified label."""
    try:
        xpath = CommonXPaths.any_button % string
        context.driver_utils.click_element(By.XPATH, xpath)
    except Exception as e:
        context.logger.error(f"Error clicking the '{string}' button: {e}")
        raise

@Then("The {string1} header should be visible")
def step_impl(context, string1):
    try:
        #generate xpath
        xpath_required = string1.title()
        xpath = CommonXPaths.text_messages_for_section % xpath_required
        
        actual_text = context.driver_utils.get_element_text(By.XPATH, xpath)
        
        #strip off unnecessary quotes
        actual_text_cleaned = actual_text.strip('"')
        expected_text_cleaned = string1.strip('"')
        
        assert actual_text_cleaned == expected_text_cleaned, f"Expected text: '{expected_text_cleaned}', but got: '{actual_text_cleaned}'"
        
        # Log success mesage if the texts match
        context.logger.info(f"Text '{string1}' is correctly visible on the page.")
    except AssertionError as ae:
        context.logger.error(f"Assertion failed")
        raise
    
    except Exception as e:
            # Log the error and raise it
        context.logger.error(f"Error in step: Verify that {string1} is visible")
        raise
    

@When("Click OK button in the prompt")
def step_impl(context):
    """Handles JavaScript alert popups by clicking OK."""
    try:
        context.driver_utils.accept_alert()
    except Exception as e:
        context.logger.error(f"Error clicking OK in prompt: {e}")
        raise

@Then('Verify the user is on the home page')
def step_impl(context):
    """Confirms that the user is on the homepage."""
    try:
        current_url = context.driver_utils.get_current_url()
        expected_url = context.config['url']
        
        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"
        context.logger.info("User is on the home page.")
    except AssertionError as ae:
        context.logger.error(f"URL mismatch: {ae}")
        raise
    except Exception as e:
        context.logger.error(f"Error verifying homepage URL: {e}")
        raise

@Then("Verify the user is on the {string} page")
def step_impl(context, string):
    """Validates the current URL matches the expected page."""
    try:
        current_url = context.driver_utils.get_current_url()
        
        # Remove unwanted quotes if present in the string parameter
        string = string.strip('"')  # Strip double quotes
        
        # Construct the expected URL correctly
        expected_url = f"{context.config['url'].rstrip('/')}/{string.lstrip('/')}"

        assert current_url == expected_url, f"Expected: {expected_url}, but got: {current_url}"
        context.logger.info(f"User is on the '{string}' page.")
    except AssertionError as ae:
        context.logger.error(f"URL mismatch for '{string}': {ae}")
        raise
    except Exception as e:
        context.logger.error(f"Error verifying '{string}' page: {e}")
        raise



