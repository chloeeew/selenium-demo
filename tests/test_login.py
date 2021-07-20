"""
==================
Author:Chloeee
Time:2021/3/14 13:24
Contact:403505960@qq.com
==================
编写课堂派老版本的登录功能自动化用例，
考虑成功和典型的异常场景：
1、成功
2、用户名为空
3、密码为空
4、用户名不存在
5、密码长度不正确(5位和31位)
"""
import time
import pytest
import allure
from pages.login import LoginPage
from pages.index import IndexPage
from pages.home import HomePage
from common.logger_handler import logger
from common.yaml_handler import yaml_testcase

@allure.feature("登录测试")
class TestLogin:

    @allure.title("冒烟测试-登录成功")
    @pytest.mark.parametrize("yaml_data", yaml_testcase.get('data_list_success'))
    def test_login_success(self, yaml_data,get_driver):
        """测试登录成功的场景（冒烟）
        1、打开浏览器
        2、进入登录也页面
        3、输入用户名、密码
        4、点击登录
        5、登录成功
        """
        # USING FIXTURE TO GET DRIVER A WHICH JUST OPENED THE BROWSER
        driver = get_driver
        # CREATE INDEX PAGE OBJECT
        index_page = IndexPage(driver)
        index_page.close_init_popup_window()  # CLOSE POPUP
        index_page.click_into_login()  # CLICK TO-LOGIN BUTTON

        # CREATE LOGIN PAGE OBJECT
        time.sleep(2)
        login_page = LoginPage(driver)

        # CHAINED CALL，SET USERNAME AND PASSWORD, THEN CLICK CONFIRM
        login_page.set_usr_and_password(yaml_data.get('usr'), yaml_data.get('pwd')).click_login_confirm()

        # create homepage object
        time.sleep(2)
        home_page = HomePage(driver)

        # COMPARE
        actual = home_page.get_usr_name()
        logger.info(f"实际结果为：{actual},预期结果为{yaml_data['expected']}")
        assert actual == yaml_data['expected']



    @allure.title("异常登录测试用例")
    @pytest.mark.parametrize("yaml_data", yaml_testcase.get('data_list_wrong'))
    def test_login_usr_empty(self, get_driver, yaml_data):
        """测试用户名为空
        1、访问登录页面
        2、输入值
        3、根据错误信息对比预期结果
        """
        driver = get_driver

        # CALL ON LOGIN PAGE DIRECTLY，SKIP THE INDEX-PAGE PROCESS
        login_page = LoginPage(driver).get_into_login_url()
        login_page.set_usr_and_password(yaml_data.get('usr'), yaml_data.get('pwd')).click_login_confirm()

        # COMPARE
        actual = login_page.get_error_tips()
        for i, el in enumerate(actual):
            assert el.text == yaml_data.get('expected')[i]



