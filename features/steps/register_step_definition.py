from time import sleep
from behave import *
import common_step_definition
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath_files.registerPage_xpaths import RegisterPageXPaths
from xpath_files.common_xpaths import CommonXPaths
from utils.driver_utils import DriverUtils
from utils.logger import get_logger

#logger = get_logger()


@given('The user is on the home page url')
def step_impl(context):
    try:
        # Use DriverUtils to navigate to the URL
        context.driver_utils.navigate_to_url(context.config['url'])
        # Validate the current URL
        current_url_rendered = context.driver_utils.get_current_url()
        if current_url_rendered != context.config['url']:
            raise AssertionError(f"Expected URL: {context.config['url']}, but got: {current_url_rendered}")
    except Exception as e:
        # Log the error with detailed message
        context.logger.error("Error in step: The user is on the home page url")    
        # Reraise the exception to ensure the test fails
        raise
    
#name and email address are generated randomly during runtime   
@When("The user enters name and email address")
def step_impl(context):
    try:
        # Generate a unique first name
        first_name = common_step_definition.generate_unique_name()
        context.first_name = first_name
        # Generate the corresponding unique email
        email = common_step_definition.generate_unique_email(first_name)
        context.email = email
        # Send the generated first name and email to the respective fields
        context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.name_field_signup, first_name)
        context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.email_field_signup, email)
        
        # Log the generated values for verification purposes
        context.logger.info(f"Generated First Name: {first_name}, Generated Email: {email}")
    except Exception as e:
        # Log the error with detailed message
        context.logger.error("Error in step: The user enters name and email address")     
        # Reraise the exception to ensure the test fails
        raise
    
#uses predefined name and email in the config.json 
@When("The user enters name and email address from test data")
def step_impl(context):
    try:
        context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.name_field_signup, context.config['firstname'])
        context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.email_field_signup, context.config['email'])
        context.first_name=context.config['firstname']
        context.email=context.config['email']
    except Exception as e:
        # Log the error with detailed message
        context.logger.error("Error in step: The user enters name and email address")     
        # Reraise the exception to ensure the test fails
        raise

@When('The user fills in account information')
def step_impl(context):
        try:
            # Personal details
            personal_details = {
                "name": context.config['firstname']+" "+context.config['lastname'],
                'firstname': context.config['firstname'],
                'lastname': context.config['lastname'],
                'email': context.config['email'],
                'password': context.config['password'],
                'mobile': context.config['mobileNumber']
            }

            # Address details
            address_details = {
               'address': context.config['address'],
               'state': context.config['state'],
               'city': context.config['city'],
               'zipcode': context.config['zipcode']
            }

            # Select dropdown options
            birth_date = {
               'day': 1,      # Example: 1st day
               'month': 3,    # Example: March
                'year': 5      # Example: 5th year
            }

            # Fill personal information
            context.driver_utils.click_element(By.XPATH, RegisterPageXPaths.radio_button_for_title_mr)
            context.logger.info("Clicked the title radio button")
            #context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.input_field_name_register, personal_details['name'])
            #context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.nput_field_email_register, personal_details['email'])
            context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.input_field_password_register, personal_details['password'])

           # Select birthdate from dropdown
            context.driver_utils.select_dropdown_by_index(By.XPATH, RegisterPageXPaths.selector_days_register, birth_date['day'])
            context.driver_utils.select_dropdown_by_index(By.XPATH, RegisterPageXPaths.selector_month_register, birth_date['month'])
            context.driver_utils.select_dropdown_by_index(By.XPATH, RegisterPageXPaths.selector_years_register, birth_date['year'])

           # Fill address details
            context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.input_field_firstname_register, personal_details['firstname'])
            context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.input_field_lastname_register, personal_details['lastname'])
            context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.address_field1_regiter, address_details['address'])
            context.driver_utils.select_dropdown_by_visible_text(By.XPATH, RegisterPageXPaths.selector_country_register, context.config['country'])
            context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.input_state_register, address_details['state'])
            context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.input_city_register, address_details['city'])
            context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.input_zipcode_register, address_details['zipcode'])

            # Fill mobile number
            context.driver_utils.send_keys_to_element(By.XPATH, RegisterPageXPaths.input_mobile_register, personal_details['mobile'])
            context.driver_utils.scroll_into_view_and_click(By.XPATH, RegisterPageXPaths.create_button_register)

            context.logger.info("Registration form filled successfully.")
        
        except Exception as e:
            context.logger.error("Error in step: The user fills in account information")
            raise
        
    
        
             
        
            
    
    







            
        

