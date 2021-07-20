"""
==================
Author:Chloeee
Time:2021/3/27 14:59
Contact:403505960@qq.com
==================
"""
import time
from common.basepage import BasePage
from selenium.webdriver.common.by import By
from common.logger_handler import logger


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
        """
        签到
        """
        self.click_element(self.sign_in_btn_locator)
        self.send_text(self.sign_in_text_locator,sign_num)
        logger.info(f"签到，签到码为{sign_num}")

    def get_sign_in_time(self):
        """
        获得签到时间
        :return:
        """
        datetime_str = self.get_element_text(self.new_sign_time_locator)
        date,time_str = str.split(datetime_str)
        logger.info(f"签到时间为：{datetime_str}")
        return date,time_str

    def get_sign_in_state(self):
        """
        获得签到状态
        :return:
        """
        state_str = self.get_element_text(self.new_sign_state_locator)
        logger.info(f"当前签到状态：{state_str}")
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
    # 考勤frame-数字考勤-结束按钮
    number_attendance_cancel = (By.XPATH,'//*[@id="number-attend"]//a[@class="sure active" and text()="结束"]')
    # 考勤frame-数字考勤-结束按钮-确认结束按钮
    num_att_cancel_confirm = (By.XPATH,'//*[contains(text(),"结束并完成考勤")]/following-sibling::div/*[text()="结束"]')
    # 考勤frame-旧考勤弹窗
    old_attendance = (By.XPATH,'//*[@id="number-attend"]')
    # 考勤frame-考勤结果弹窗关闭
    close_attend_result = (By.CSS_SELECTOR,".attendResult > .header > .icon")
    # 考勤frame -考勤统计返回按钮
    back_to_attend_list = (By.CSS_SELECTOR,".backtolistline > a > i")

    def check_student_in_class_member(self,student_id):
        """查看学生是否在课堂的成员里面"""
        # 点击成员进入
        self.click_element(self.class_member_link_locator)
        # 找到学生分组
        self.click_element(self.student_group_locator)
        # 找到成员
        member_locator = (By.XPATH,f'//*[@title="{student_id}"]')
        logger.info(f"查看成员{student_id}是否在课堂成员中")
        return self.wait_elements_visible(member_locator)

    def raise_attendance(self):
        """
        发起考勤，返回考勤码字符串
        :return:sign_num_str
        """
        logger.info("发起考勤")
        # 点击考勤按钮
        self.click_element(self.check_attendance_locator)
        # 等待
        # att_ele = self.wait_element_visible()
        self.switch_to_the_frame(self.attendance_iframe)
        # self.driver.switch_to.frame(att_ele)

        # 如果上一次考勤还没结束，先结束考勤
        if self.wait_element_visible(self.old_attendance):
            self.click_element(self.number_attendance_cancel)
            self.click_element(self.num_att_cancel_confirm)
            self.click_element(self.close_attend_result)
            self.click_element(self.back_to_attend_list)

        # 点击新建考勤
        self.click_element(self.create_attendance)
        # 点击数字考勤
        self.click_element(self.number_attendance)
        # 点击开始考勤
        self.click_element(self.start_attendance_btn)
        # 获得考勤码
        sign_num_elements = self.wait_elements_visible(self.sign_in_number_locator)
        sign_num_list = []
        for ele in sign_num_elements:
            sign_num_list.append(ele.text)
        sign_num_str = ''.join(sign_num_list)
        if sign_num_str:
            logger.info(f"已获得考勤码：{sign_num_str}")
        else:
            logger.warning("考勤码为空，请检查考勤码的定位")
        return sign_num_str

    def get_sign_in_member_count(self):
        """
        获得考勤人数
        """
        # 等待人数加载：默认是先显示0，需要时间加载实际人数
        time.sleep(2)
        sign_in_num_str = self.get_element_text(self.sign_in_ing_num_locator)
        sign_in_num = int(sign_in_num_str)
        logger.info(f"当前显示的考勤人数为：{sign_in_num}")
        return sign_in_num
