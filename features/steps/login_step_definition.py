import common_step_definition
from time import sleep
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath_files.loginPage_xpaths import LoginPageXPaths
from xpath_files.common_xpaths import CommonXPaths
from utils.driver_utils import DriverUtils
from xpath_files.registerPage_xpaths import RegisterPageXPaths

 
@When("The user enters correct login name and email address")
def step_impl(context):
    try:
        context.driver_utils.send_keys_to_element(By.XPATH, LoginPageXPaths.email_field_login, context.config['email'])
        context.driver_utils.send_keys_to_element(By.XPATH, LoginPageXPaths.password_field_login, context.config['password'])
        context.first_name = context.config['firstname']
    except Exception as e:
        # Log the error with detailed message
        context.logger.error("Error in step: The user enters correct login name and email address")     
        # Reraise the exception to ensure the test fails
        raise
    
#name and email address are generated randomly during runtime   
@When("The user enters incorrect login name and email address")
def step_impl(context):
    try:
        # Generate a unique first name
        first_name = common_step_definition.generate_unique_name()
        context.first_name = first_name
        # Generate the corresponding unique email
        email = common_step_definition.generate_unique_email(first_name)
        context.email = email
        context.driver_utils.send_keys_to_element(By.XPATH, LoginPageXPaths.email_field_login, email)
        context.driver_utils.send_keys_to_element(By.XPATH, LoginPageXPaths.password_field_login, first_name) #passing password as the first name
        
    except Exception as e:
        # Log the error with detailed message
        context.logger.error("Error in step: The user enters incorrect login name and email address")     
        # Reraise the exception to ensure the test fails
        raise
    
@Then('Verify that Logged in as username is visible')
def step_impl(context):
    try:
        expected_text = "Logged in as "+context.first_name
        context.logger.info("Expected log in message is "+expected_text)
        actual_text = context.driver_utils.get_element_text(By.XPATH, RegisterPageXPaths.logged_in_text)
        assert actual_text.strip() == expected_text.strip(), f"Expected text: '{expected_text}', but got: '{actual_text.strip()}'"
        context.logger.info(f"Text '{expected_text}' is correctly visible on the page.")
    
    except AssertionError as e:
            # Log if the assertion fails
        context.logger.error(f"Text mismatch: Expected '{expected_text}', but found '{actual_text.strip()}'.")
        raise
    except Exception as e:
            # Log the error and raise it
        context.logger.error(f"Error in step: Verify that Logged in as username is visible")
        raise