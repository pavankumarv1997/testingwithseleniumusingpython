from selenium import webdriver
import unittest
import time
import pytest
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import allure
from selenium.webdriver.common.action_chains import ActionChains

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    base_url = "https://www.clickoncare.com/"

    # Checks login page whether user enters otp or not
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self ):
        self.loginpage.click_on_login_button()
        self.driver.implicitly_wait(5)
        phone_num = "8217019247"
        self.loginpage.set_phone_num(phone_num)
        time.sleep(2)

        self.loginpage.get_otp_button()
        time.sleep(20)
        entered_otp = self.loginpage.read_otp()
        # resends otp by checking whether user entered otp or not
        if (len(entered_otp) == 0):
            self.resend_otp_via_call()
        else:
            self.loginpage.submit_otp()
            print("logged in successfully")
        time.sleep(5)
        self.driver.implicitly_wait(10)
        current_url = self.loginpage.verifyUrl(self.base_url)
        self.ts.mark(current_url , "Url Verification")
        account = self.loginpage.verifySuccessfullLogin()
        self.ts.markFinal("test_login",account,"My Account Verification")
        # self.assertEqual(self.base_url,self.driver.current_url,"LogIn UnSuccessfull")

    # resend otp via call method this is not a test method
    def resend_otp_via_call(self):
        self.loginpage.resend_otp_button()
        time.sleep(25)
        self.loginpage.submit_otp()

    def test_logout(self):
        pytest.skip('for a reason will implement later!')
        self.driver.implicitly_wait(10)
        loginpage = LoginPage(self.driver)
        actions = ActionChains(self.driver)
        loginpage.mouse_hover_on_more(actions,time)
        time.sleep(5)
        print("Logged out Successfully....")



