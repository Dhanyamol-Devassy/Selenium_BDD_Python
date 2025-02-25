# utils/driverutils.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
from utils.logger import get_logger
from selenium.webdriver.support.ui import Select

class DriverUtils:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger  # Use the logger passed from environment.py

    def wait_for_element_to_be_clickable(self, by, value, timeout=10):
        """Wait until an element is clickable."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            self.logger.info(f"Element {value} is clickable.")
            return element
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error waiting for element {value} to be clickable: {error_message}")
            raise

    def click_element(self, by, value):
        """Click on an element after ensuring it's clickable."""
        try:
            element = self.wait_for_element_to_be_clickable(by, value)
            element.click()
            self.logger.info(f"Clicked on element: {value}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error clicking on element {value}: {error_message}")
            raise

    def wait_for_element_to_be_visible(self, by, value, timeout=10):
        """Wait until an element is visible on the page."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            self.logger.info(f"Element {value} is visible.")
            return element
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error waiting for element {value} to be visible : {error_message}")
            raise

    def navigate_to_url(self, url):
        """Navigate to a specific URL."""
        try:
            self.driver.get(url)
            self.logger.info(f"Navigated to URL: {url}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error navigating to URL {url} : {error_message}")
            raise

    def get_current_url(self):
        """Get the current URL of the browser."""
        try:
            current_url = self.driver.current_url
            self.logger.info(f"Current URL: {current_url}")
            return current_url
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error getting the current URL : {error_message}")
            raise

    def take_screenshot(self, file_name):
        """Take a screenshot and save it."""
        try:
            os.makedirs("screenshots", exist_ok=True)  # Ensure directory exists
            screenshot_path = f"screenshots/{file_name}.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved: {screenshot_path}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error taking screenshot : {error_message}")
            raise

    def close_browser(self):
        """Close the browser session."""
        try:
            self.driver.quit()
            self.logger.info("Browser closed successfully.")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error closing the browser : {error_message}")
            raise

    def send_keys_to_element(self, by, value, text):
        """Send keys to a web element."""
        try:
            element = self.wait_for_element_to_be_clickable(by, value)
            element.send_keys(text)
            self.logger.info(f"Sent keys '{text}' to element: {value}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error sending keys to element {value} : {error_message}")
            raise

    def clear_input_field(self, by, value):
        """Clear the input field."""
        try:
            element = self.wait_for_element_to_be_clickable(by, value)
            element.clear()
            self.logger.info(f"Cleared the input field: {value}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error clearing input field {value} : {error_message}")
            raise

    def wait_for_alert(self, timeout=10):
        """Wait for an alert to be present."""
        try:
            alert = WebDriverWait(self.driver, timeout).until(
                EC.alert_is_present()
            )
            self.logger.info("Alert is present.")
            return alert
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error waiting for alert : {error_message}")
            raise

    def accept_alert(self, timeout=10):
        """Accept the alert."""
        try:
            alert = self.wait_for_alert(timeout)
            alert.accept()
            self.logger.info("Alert accepted.")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error accepting the alert : {error_message}")
            raise

    def dismiss_alert(self, timeout=10):
        """Dismiss the alert."""
        try:
            alert = self.wait_for_alert(timeout)
            alert.dismiss()
            self.logger.info("Alert dismissed.")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error dismissing the alert : {error_message}")
            raise

    def switch_to_window(self, window_index=0):
        """Switch to a specific window by index."""
        try:
            all_windows = self.driver.window_handles
            self.driver.switch_to.window(all_windows[window_index])
            self.logger.info(f"Switched to window: {all_windows[window_index]}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error switching to window : {error_message}")
            raise

    def switch_to_frame(self, frame_reference):
        """Switch to a frame (either by name, index, or WebElement)."""
        try:
            self.driver.switch_to.frame(frame_reference)
            self.logger.info(f"Switched to frame: {frame_reference}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error switching to frame {frame_reference} : {error_message}")
            raise

    def switch_to_default_content(self):
        """Switch back to the default content (main page)."""
        try:
            self.driver.switch_to.default_content()
            self.logger.info("Switched to default content.")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error switching to default content : {error_message}")
            raise

    def right_click_on_element(self, by, value):
        """Right-click (context click) on an element."""
        try:
            element = self.wait_for_element_to_be_clickable(by, value)
            action = ActionChains(self.driver)
            action.context_click(element).perform()
            self.logger.info(f"Right-clicked on element: {value}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error right-clicking on element {value} : {error_message}")
            raise

    def move_to_element(self, by, value):
        """Move the mouse to an element."""
        try:
            element = self.wait_for_element_to_be_visible(by, value)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            self.logger.info(f"Moved to element: {value}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error moving to element {value} : {error_message}")
            raise

    def double_click_on_element(self, by, value):
        """Double-click on an element."""
        try:
            element = self.wait_for_element_to_be_clickable(by, value)
            action = ActionChains(self.driver)
            action.double_click(element).perform()
            self.logger.info(f"Double-clicked on element: {value}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error double-clicking on element {value} : {error_message}")
            raise

    def drag_and_drop(self, source_by, source_value, target_by, target_value):
        """Perform drag and drop operation."""
        try:
            source_element = self.wait_for_element_to_be_clickable(source_by, source_value)
            target_element = self.wait_for_element_to_be_clickable(target_by, target_value)
            action = ActionChains(self.driver)
            action.drag_and_drop(source_element, target_element).perform()
            self.logger.info(f"Dragged and dropped from {source_value} to {target_value}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error performing drag and drop : {error_message}")
            raise

    def get_element_text(self, by, value):
        """Get the text of an element."""
        try:
            element = self.wait_for_element_to_be_visible(by, value)
            text = element.text
            self.logger.info(f"Text of element {value}: {text}")
            return text
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error getting text of element {value} : {error_message}")
            raise

    def is_element_present(self, by, value):
        """Check if an element is present on the page."""
        try:
            element = self.driver.find_element(by, value)
            self.logger.info(f"Element {value} is present.")
            return True
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Element {value} not found : {error_message}")
            return False
        
    def select_dropdown_by_index(self, by, value, index):
        """
        Select an option in a dropdown by its index.
        """
        try:
            dropdown_element = self.wait_for_element_to_be_visible(by, value)
            select = Select(dropdown_element)
            select.select_by_index(index)
            self.logger.info(f"Selected index {index} from dropdown: {value}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error selecting index {index} from dropdown {value} : {error_message}")
            raise

    def select_dropdown_by_visible_text(self, by, value, text):
        """
        Select an option in a dropdown by its visible text.
        """
        try:
            dropdown_element = self.wait_for_element_to_be_visible(by, value)
            select = Select(dropdown_element)
            select.select_by_visible_text(text)
            self.logger.info(f"Selected option '{text}' from dropdown: {value}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error selecting option '{text}' from dropdown {value} : {error_message}")
            raise
    
    def scroll_into_view_and_click(self, by, value):
        """Scroll an element into view and click it."""
        try:
            # Find the element using the provided locator
            element = self.driver.find_element(by, value)
            
            # Scroll the element into view using JavaScript
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            
            # Optionally, use ActionChains to move to the element and click it
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            
            self.logger.info(f"Successfully clicked on the element with locator: {value}")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error clicking on element {value}: {error_message}")
            raise
    
    def assert_element_text(self, xpath, expected_text):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            actual_text = element.text.strip()
            assert actual_text == expected_text, f"Expected: '{expected_text}', but got: '{actual_text}'"
            return True
        except AssertionError as ae:
            error_message = str(ae).split("\n")[0]
            self.logger.error(f"Assertion failed for {xpath}: {error_message}")
            return False
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error occurred in asserting text for {xpath}: {error_message}")
            return False 
        
    def verify_list_is_not_empty(self, input_list, list_name):
        try:
        # Check if the list is not empty
            if not input_list:
                raise ValueError(f"The list {list_name} is empty.")

        # Log if the list is not empty
            self.logger.info(f"The list {list_name} is not empty. List contains {len(input_list)} items.")
    
        except Exception as e:
        # Handle the exception and log it
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error verifying list {list_name}: {error_message}")
            raise
    
    def create_file_if_not_exists(self, file_name, content="This is a sample file created for Selenium file upload test.", timeout=10):
        """Create the file in the project directory if it doesn't already exist."""
        try:
            # Check if file exists
            if not os.path.exists(file_name):
                with open(file_name, "w") as file:
                    file.write(content)
                self.logger.info(f"File '{file_name}' created successfully.")
            else:
                self.logger.info(f"File '{file_name}' already exists.")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error creating file '{file_name}': {error_message}")
            raise

    def upload_file(self, by, value, file_path, timeout=10):
        """Upload the created file"""
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File '{file_path}' does not exist.")

            file_input = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))
            file_input.send_keys(file_path)
            self.logger.info(f"File '{file_path}' uploaded successfully.")
        except FileNotFoundError as fnf:
            self.logger.error(f"File upload error: {str(fnf)}")
            raise
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error during file upload: {error_message}")
            raise
      
    def set_implicit_wait(self, timeout=10):
        """Set implicit wait for driver"""
        try:
            self.driver.implicitly_wait(timeout)
            self.logger.info(f"Implicit wait set to {timeout} seconds.")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            self.logger.error(f"Error setting implicit wait: {error_message}")
            raise
  
        
    
