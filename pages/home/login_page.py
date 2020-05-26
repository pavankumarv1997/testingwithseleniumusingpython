import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    # locators of all the login page elements
    login_element_xpath = "/html/body/div[2]/div/div[1]/div[3]/ul/li[2]/a/span"
    phone_num_id = "phone_no1"
    get_otp_id = "verify-btn"
    enter_otp_id = "otp"
    send_otp_id = "sendOtp"
    resend_otp_id = "resendOtp-btn"
    more_button_hover_xpath = "/html/body/div[2]/div/div[1]/div[3]/ul/li[4]/span"
    logout_link_xpath = "/html/body/div[2]/div/div[1]/div[3]/ul/li[4]/ol/div/li[6]/a"
    logged_in_account_xpath ="/html/body/div[2]/div/div[1]/div[3]/ul/li[2]/a/span"

    # constructor method to make driver to identify all the elements
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_login_button(self):
        self.elementClick(self.login_element_xpath,locatorType="xpath")

    # list  of actions performed on that page
    def set_phone_num(self, phone_num):
        self.sendKeys(phone_num,self.phone_num_id)

    def get_otp_button(self):
        self.elementClick(self.get_otp_id)
    def read_otp(self):
        entered_otp = self.getElement(self.enter_otp_id).get_attribute("value")
        return entered_otp

    def submit_otp(self):
        self.elementClick(self.send_otp_id)
    def resend_otp_button(self):
        self.elementClick(self.resend_otp_id)

    def verifyUrl(self,base_url):
        return self.verifyPageUrl("https://www.clickoncare.com/")

    def verifySuccessfullLogin(self):
        account = self.getElement(self.logged_in_account_xpath,"xpath").get_attribute("innerHTML")
        if "My Account" in account:
            return True
        else:
            return False

    def mouse_hover_on_more(self, actions, time):
        more_option = self.getElement(self.more_button_hover_xpath,"xpath")
        logout = self.getElement(self.logout_link_xpath , "xpath")
        actions.move_to_element(more_option).click(logout).perform()




