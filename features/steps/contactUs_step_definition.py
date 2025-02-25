from time import sleep
from behave import *
import os
import common_step_definition
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath_files.registerPage_xpaths import RegisterPageXPaths
from xpath_files.common_xpaths import CommonXPaths
from utils.driver_utils import DriverUtils
from xpath_files.contactUs_xpaths import ContactUsPageXPaths
from utils.logger import get_logger

    
@When("The user fills in contact us information")
def step_impl(context):
    """Fills out the Contact Us form with test data."""
    try:
        contact_info = {
            "name": context.config['firstname'],
            "email": context.config['email'],
            "subject": context.config['contactUsSubject'],
            "message": context.config['contactUsMessage']
        }

        # Fill in form fields
        context.driver_utils.send_keys_to_element(By.XPATH, ContactUsPageXPaths.name_field_contactUs, contact_info['name'])
        context.driver_utils.send_keys_to_element(By.XPATH, ContactUsPageXPaths.email_field_contactUs, contact_info['email'])
        context.driver_utils.send_keys_to_element(By.XPATH, ContactUsPageXPaths.subject_field_contactUs, contact_info['subject'])
        context.driver_utils.send_keys_to_element(By.XPATH, ContactUsPageXPaths.message_field_contactUs, contact_info['message'])

        # File upload handling
        upload_path = os.path.join(os.getcwd(), "contactUs")
        context.driver_utils.upload_file(By.XPATH, ContactUsPageXPaths.choosefile_field_contactUs, upload_path)

        # Submit the form
        context.driver_utils.scroll_into_view_and_click(By.XPATH, ContactUsPageXPaths.submit_button_contactUs)
        context.logger.info("Contact Us form submitted successfully.")
    except Exception as e:
        context.logger.error(f"Error filling out Contact Us form: {e}")
        raise