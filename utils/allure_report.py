import allure

def attach_screenshot_to_report(driver):
    screenshot_path = 'reports/screenshots/failed_step.png'
    driver.save_screenshot(screenshot_path)
    allure.attach.file(screenshot_path, name='Failure Screenshot', attachment_type=allure.attachment_type.PNG)
