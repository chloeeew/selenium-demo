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

from pages.login import LoginPage
from pages.index import IndexPage
from pages.home import HomePage
from data import login
import pytest
import allure

@allure.feature("登录测试")
class TestLogin:

    @allure.title("冒烟测试-登录成功")
    @pytest.mark.parametrize("username,pwd,expected", login.data_list_success)
    def test_login_success(self, get_driver, username, pwd, expected):
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
        login_page = LoginPage(driver)
        # CHAINED CALL，SET USERNAME AND PASSWORD, THEN CLICK CONFIRM
        login_page.set_usr_and_password(username, pwd).click_login_confirm()

        # COMPARE
        actual = HomePage(driver).get_usr_name()
        assert actual == expected

    @allure.title("异常登录测试用例")
    @pytest.mark.parametrize("username,pwd,expected", login.data_list_wrong)
    def test_login_usr_empty(self, get_driver, username, pwd, expected):
        """测试用户名为空
        1、访问登录页面
        2、输入值
        3、根据错误信息对比预期结果
        """
        driver = get_driver

        # CALL ON LOGIN PAGE DIRECTLY，SKIP THE INDEX-PAGE PROCESS
        login_page = LoginPage(driver).get_into_login_url()
        login_page.set_usr_and_password(username, pwd).click_login_confirm()

        # COMPARE
        actual = login_page.get_error_tips()
        for i, el in enumerate(actual):
            assert el.text == expected[i]



