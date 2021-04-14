"""
==================
Author:Chloeee
Time:2021/3/16 22:04
Contact:403505960@qq.com
==================
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from common.basepage import BasePage
import time


class HomePage(BasePage):
    """课堂派个人主页
    1、获取用户名
    """
    # 头像
    avatar_locator = (By.CLASS_NAME, "avatar")


    def get_usr_name(self):
        """获取登录的名称
        """
        # 登录后等待头像的出现
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=0.2)
        wait.until(expected_conditions.visibility_of_element_located(self.avatar_locator))
        return self.get_element_attribute(self.avatar_locator, "title")

    @staticmethod
    def __year_validate__(year_text):
        year_list = ["2010-2011", "2011-2012", "2012-2013", "2013-2014", "2014-2015",
                     "2015-2016", "2016-2017", "2017-2018", "2018-2019", "2019-2020",
                     "2020-2021", "2021-2022", "2022-2023", "2023-2024"]
        if year_text in year_list:
            return True
        return False

    def check_class_by_name(self, current_class_name):
        """查找是否有课程"""
        return self.driver.find_element(By.XPATH, f'//a[text()="{current_class_name}"]')

    def get_class_name_by_num(self, num):
        """根据课程名称，获取加课码"""
        class_title_ele_locator = (By.XPATH, f'//*[text()=" 加课码：{num}"]/ancestor::dl//*[@class="jumptoclass"]')
        class_title_ele = self.wait_element_visible(class_title_ele_locator)
        class_name = class_title_ele.get_attribute("title")
        return class_name

    def check_class_by_num(self, class_num):
        """根据课程码查看是否有课程"""
        class_code_locator = (By.CLASS_NAME,"invitecode")
        data_code_list = self.get_elements(class_code_locator)
        for element in data_code_list:
            if class_num in element.text:
                return element
        return False



class HomePageStudent(HomePage):
    # 加入课程按钮
    add_class_btn_locator = (By.XPATH,'//div[contains(@class,"ktcon1l") and contains(text(),"加入课程")]')
    # 弹窗=请输入加课验证码框
    add_class_input_locator = (By.XPATH,'//input[@placeholder="请输入课程加课验证码"]')
    # 弹窗=加入按钮
    add_class_confirm_btn_locator = (By.XPATH, '//*[text()="加入"]')
    # 弹窗=取消按钮
    add_class_cancel_btn_locator = (By.CSS_SELECTOR, ".cjli1 > a")
    # 退课弹窗-输入用户密码输入框
    quit_pwd_locator = (By.XPATH, '//*[@placeholder="请输入登录密码验证"]')
    # 退课弹窗-退课确认按钮
    quit_button_locator = (By.XPATH, '//a[@class="btn btn-positive"  and text()="退课"]')


    def click_into_class_by_num(self,class_num):
        # 找到课程，进入课程
        class_link_locator = (By.XPATH, f'//*[text()=" 加课码：{class_num}"]/ancestor::dl//a[@class="jumptoclass"]')
        self.click_element(class_link_locator)

    def add_class(self, num, confirm=True):
        """点击加入课程
        confirtm为Ture时，即选择确定；为False时，即选择取消
        """
        self.click_element(self.add_class_btn_locator)
        self.send_text(self.add_class_input_locator,num)

        if confirm:
            self.click_element(self.add_class_confirm_btn_locator)
        else:
            self.click_element(self.add_class_cancel_btn_locator)
        time.sleep(2)

    def quit_class_by_name(self,name, usr_pwd):
        # 找到更多->点击
        class_more_ele_locator = (By.XPATH,f'//*[@title="{name}"]/ancestor::dl//*[@class="kdmore"]')
        self.click_element(class_more_ele_locator)
        # 找到退课按钮->点击
        class_quit_btn_locator = (By.XPATH, f'//*[@title="{name}"]/ancestor::dl//*[text()="退课"]')
        self.click_element(class_quit_btn_locator)
        # 退课弹窗，找到输入框，输入密码
        self.send_text(self.quit_pwd_locator,usr_pwd)
        # 点击退课确认按钮
        self.click_element(self.quit_button_locator)
        # 时间缓冲
        time.sleep(3)



class HomePageTeacher(HomePage):
    # 创建/加入课程按钮
    create_button_locator = (By.XPATH, "//*[contains(text(),'创建/加入课程')]")
    # 2级：创建课程按钮
    create_class_button_locator = (By.ID, "addClass")
    # 创建课程弹窗-课程名称框
    class_name_locator = (By.XPATH, '//*[@placeholder="请输入课程名称"]')
    # 创建课程弹窗-年份下拉框
    year_locator = (By.XPATH, '//*[@class="yearselbox"]/p')
    # 创建课程弹窗-学期下拉框
    semester_locator = (By.XPATH, '//*[@class="studydatebox"]/p')
    # 创建课程弹窗-创建按钮
    create_confirm_button_locator = (By.XPATH, '//*[text()="创建"]')
    # 创建课程弹窗
    new_class_frame_locator = (By.ID, "new-class")
    # 课堂页面-成员，点击成员进入
    class_member_link_locator = (By.XPATH, '//*[contains(@class,"iconchengyuan")]/ancestor::a')


    def click_into_class_by_num(self,class_num):
        # 找到课程，进入课程
        class_link_locator = (By.XPATH, f'//*[@data-code="{class_num}"]/ancestor::dl//a[@class="jumptoclass"]')
        self.click_element(class_link_locator)

    def create_class(self, current_class_name, year="2021-2022"):
        """创建课程"""
        if not self.__year_validate__(year):
            raise ValueError
        self.click_element(self.create_button_locator)
        self.click_element(self.create_class_button_locator)
        # 输入课程名称
        self.send_text(self.class_name_locator,current_class_name)
        # 选择年份
        self.click_element(self.year_locator)
        year_locator = (By.XPATH, f'//li[text()="{year}"]')
        self.scroll_and_click(year_locator)
        # 选择学期
        self.click_element(self.semester_locator)
        semester_locator = (By.XPATH, '(//*[@id="studydatelists"]/descendant::li)[1]')
        self.click_element(semester_locator)
        # 创建
        self.click_element(self.create_confirm_button_locator)


    def class_sign_in(self,class_num):
        # 找到课程，进入课程
        self.click_into_class_by_num(class_num)
