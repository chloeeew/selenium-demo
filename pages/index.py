"""
==================
Author:Chloeee
Time:2021/3/16 21:57
Contact:403505960@qq.com
==================
"""

from selenium.webdriver.common.by import By
from common import yaml_handler
from common.basepage import BasePage

host_url = yaml_handler.yaml_config["host"]


class IndexPage(BasePage):
    """课堂派旧版首页
    1、点击进入登录页面
    2、点击进入注册页面
    3、关闭页面初始化弹窗
    """
    # url地址
    url = host_url
    # 首页弹窗
    locator_popup = (By.CLASS_NAME, 'layui-layer-content')
    # 首页弹窗-关闭
    locator_popup_close = (By.XPATH, "//a[contains(@class,'layui-layer-close2')]")
    # 登录按钮
    locator_login_button = (By.CLASS_NAME, "login")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.url)

    def close_init_popup_window(self):
        """如果有弹窗，那么关闭弹窗
        """
        if self.driver.find_element(*self.locator_popup):
            self.click_element(self.locator_popup_close)
        return self

    def click_into_login(self):
        """找到登录按钮
        """
        self.click_element(self.locator_login_button)
        return self



