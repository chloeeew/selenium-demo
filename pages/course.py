"""
==================
Author:Chloeee
Time:2021/3/27 14:59
Contact:403505960@qq.com
==================
"""
from common.basepage import BasePage
from selenium.webdriver.common.by import By
import time

class CoursePage(BasePage):
    pass


class CoursePageStudent(CoursePage):
    # 立即签到按钮
    sign_in_btn_locator = (By.XPATH, '//*[text()="立即签到"]')
    # 签到码输入框
    sign_in_text_locator = (By.CSS_SELECTOR, ".vc-number > input")
    # 最新已签到时间
    new_sign_time_locator = (By.XPATH, '(//*[@class="time"])[1]')
    # 最新签到状态
    new_sign_state_locator = (By.XPATH, '(//*[@class="state"])[1]/span')


    def to_sign_in(self, sign_num):
        self.click_element(self.sign_in_btn_locator)
        self.send_text(self.sign_in_text_locator,sign_num)

    def get_sign_in_time(self):
        datetime_str = self.get_element_text(self.new_sign_time_locator)
        date,time_str = str.split(datetime_str)
        return date,time_str

    def get_sign_in_state(self):
        state_str = self.get_element_text(self.new_sign_state_locator)
        return state_str


class CoursePageTeacher(CoursePage):
    """课程详情页"""
    # 成员按钮
    class_member_link_locator = (By.XPATH, '//*[contains(@class,"iconchengyuan")]/ancestor::a')
    # 成员-全部学生
    student_group_locator = (By.XPATH, '//*[text()="全部学生（学生"]')
    # 考勤按钮
    check_attendance_locator = (By.XPATH, "//*[text()='考勤']/ancestor::a")
    # 考勤iframe
    attendance_iframe = (By.XPATH,'//*[@id="layui-layer1"]//iframe')
    # 考勤frame-新建考勤
    create_attendance = (By.XPATH, '//*[text()="新建考勤"]')
    # 考勤frame-数字考勤
    number_attendance = (By.XPATH,'//*[@class="attance-way"]/li[@data-type="1"]')
    # 考勤frame-开始考勤按钮
    start_attendance_btn = (By.XPATH, '//*[contains(@class,"layui-layer-page")]//*[text()="开始考勤"]')
    # 考勤码
    sign_in_number_locator = (By.CSS_SELECTOR, ".number-box > span")
    # 已签到人数
    sign_in_ing_num_locator = (By.XPATH, '//*[@id="number-attend"]//i[@class="ing"]')

    def check_student_in_class_member(self,student_id):
        """查看学生是否在课堂的成员里面"""
        # 点击成员进入
        self.click_element(self.class_member_link_locator)
        # 找到学生分组
        self.click_element(self.student_group_locator)
        # 找到成员
        member_locator = (By.XPATH,f'//*[@title="{student_id}"]')
        return self.driver.find_element(*member_locator)

    def raise_attendance(self):
        self.click_element(self.check_attendance_locator)
        att_ele = self.wait_element_visible(self.attendance_iframe)
        self.driver.switch_to.frame(att_ele)
        self.click_element(self.create_attendance)
        self.click_element(self.number_attendance)
        self.click_element(self.start_attendance_btn)
        sign_num_elements = self.get_elements(self.sign_in_number_locator)
        sign_num_list = []
        for ele in sign_num_elements:
            sign_num_list.append(ele.text)
        sign_num_str = ''.join(sign_num_list)
        return sign_num_str

    def get_sign_in_member_count(self):
        time.sleep(2)
        sign_in_num_str = self.get_element_text(self.sign_in_ing_num_locator)
        sign_in_num = int(sign_in_num_str)
        return sign_in_num
