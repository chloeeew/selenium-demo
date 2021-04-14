"""
==================
Author:Chloeee
Time:2021/3/16 22:00
Contact:403505960@qq.com
==================
"""

from selenium.webdriver.common.by import By
from common.basepage import BasePage
from common import yaml_handler


host_url = yaml_handler.yaml_config["host"]


class LoginPage(BasePage):
    """课堂派登录页面
    1、输入用户名和密码
    2、勾选协议
    3、点击登录按钮
    4、清空用户名输入框
    5、清空密码输入框
    6、输入框全部清空
    7、获取错误信息
    """
    url = host_url + "/User/login"
    locator_login_confirm_button = (By.XPATH, "//div[contains(@class,'pt-login')]//a[@class='btn-btn']")
    locator_error_tips = (By.CLASS_NAME, "error-tips")
    locator_username_field = (By.NAME, "account")
    locator_pwd_field = (By.NAME, "pass")

    def get_into_login_url(self):
        """通过网页直接访问
        """
        self.driver.get(self.url)
        return self

    def set_usr_and_password(self, usr="", pwd=""):
        """输入用户名和密码
        默认用户名和密码输入的是空
        """
        self.send_text(self.locator_username_field, usr)
        self.send_text(self.locator_pwd_field, pwd)
        return self

    def click_login_confirm(self):
        """点击登录按钮
        """
        # 登录按钮
        self.click_element(self.locator_login_confirm_button)
        return self

    def get_error_tips(self):
        """获取输入框下提示的错误信息
        返回list
        """
        error_tips_list = self.driver.find_elements(*self.locator_error_tips)
        return error_tips_list
