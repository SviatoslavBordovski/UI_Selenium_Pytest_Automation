from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from helpers.generic_helper import GenericHelpers
from locators.login_signup_page_locators import LoginSignupLocators
from pages.abstractPage import DefaultSeleniumDriver
from utils import utils as utils


l_s_locators = LoginSignupLocators()

class LoginPage(DefaultSeleniumDriver):

    def get_email_input(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.email_address_xpath}").send_keys(Keys.CONTROL + 'a', Keys.DELETE)

        return self.driver.find_element(By.XPATH, l_s_locators.email_address_xpath)

    def get_password_input(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.password_xpath}").send_keys(Keys.CONTROL + 'a', Keys.DELETE)

        return self.driver.find_element(By.XPATH, l_s_locators.password_xpath)

    def get_name_input(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.name_xpath}").send_keys(Keys.CONTROL + 'a', Keys.DELETE)

        return self.driver.find_element(By.XPATH, value=f"{l_s_locators.name_xpath}")

    def get_signup_email_input(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.signup_email_xpath}").send_keys(Keys.CONTROL + 'a', Keys.DELETE)

        return self.driver.find_element(By.XPATH, value=f"{l_s_locators.signup_email_xpath}")

    def assert_login_page_is_visible(self):

        # Check url is correct
        expected_url = f"{utils.URL}/login"
        found_url = self.driver.current_url
        assert expected_url == found_url, f"Found url => {found_url}, expected url => {expected_url}"

        # Check login page title detected
        self.verify_login_page_visible()

        # Check login form header is correct
        title = self.driver.find_element(By.XPATH, l_s_locators.login_header_xpath).text
        assert utils.login_form_header == title, f"ERROR! Found title => {title}"

    def verify_login_page_visible(self):
        GenericHelpers(self.driver).check_page_title("Signup / Login")

    def assert_signup_full_form_visible(self):
        form_title = self.driver.find_element(By.XPATH, l_s_locators.full_signup_form_xpath).is_displayed()
        assert form_title is True, f"ERROR! Actual boolean => {form_title}"

    def assert_incorrect_email_password_alert_shown(self, expected_alert_message: str):
        found_alert_message = self.driver.find_element(
            By.XPATH, value=f"{l_s_locators.incorrect_email_password_xpath % expected_alert_message}").text
        assert expected_alert_message == found_alert_message, f"Actual found message => {found_alert_message}, " \
                                                              f"expected alert message => {expected_alert_message}"

    def assert_successfully_created_account(self, expected_title: str):
        actual_title = self.driver.find_element(By.XPATH, value=f"{l_s_locators.account_created_header_xpath}").text
        assert expected_title == actual_title, f"Expected title => {expected_title}, but found => {actual_title}"
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.registration_continue_button_xpath}").click()

    def assert_user_name_is_visible(self, user_name):
        user_name_button = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, f"{l_s_locators.user_name_navbar_xpath % user_name}")))
        assert user_name in user_name_button.text, f"Button was not visible and clickable, " \
                                                   f"so boolean => {user_name_button}, name => {user_name_button.text}"
        return user_name_button.text
