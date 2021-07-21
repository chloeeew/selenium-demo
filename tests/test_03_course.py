"""
==================
Author:Chloeee
Time:2021/3/27 17:43
Contact:403505960@qq.com
==================
"""
import allure
from pages.home import HomePageTeacher,HomePageStudent
from pages.course import CoursePageTeacher, CoursePageStudent
from common.yaml_handler import yaml_config
from common.globalmethod import get_current_time,get_current_time_range_list
from common.logger_handler import logger

@allure.feature("课程主页测试")
class TestCourse:

    @allure.title("冒烟测试-测试签到")
    def test_student_sign_in(self,login_teacher,login_student):
        """ 学生签到 : 目前只做了1位学生的签到 """
        class_num = yaml_config["class_info"]["class_num"]

        driver_teacher = login_teacher
        home_page_teacher = HomePageTeacher(driver_teacher)
        home_page_teacher.click_into_class_by_num(class_num)

        # 老师发起签到
        course_page_teacher = CoursePageTeacher(driver_teacher)
        sign_num = course_page_teacher.raise_attendance()   # 获得签到码

        # 学生根据签到码签到
        driver_student = login_student
        home_page_student = HomePageStudent(driver_student)
        home_page_student.click_into_class_by_num(class_num)
        course_page_student = CoursePageStudent(driver_student)
        course_page_student.to_sign_in(sign_num)

        # 设置断言条件：
        # 1、学生显示的签到时间在执行后的前后一分钟内
        # 2、学生签到状态是出勤
        # 3、老师的签到人数增加1位
        now_time = get_current_time()
        time_validate_range_list = get_current_time_range_list(now_time)
        get_date,get_time = course_page_student.get_sign_in_time()
        state = course_page_student.get_sign_in_state()
        member_count = course_page_teacher.get_sign_in_member_count()
        try:
            assert state == "出勤"
        except AssertionError:
            logger.error(f"断言失败，当前学生状态{state},与实际结果出勤不同")
            raise AssertionError

        try:
            assert 1 == member_count
        except AssertionError:
            logger.error(f"断言失败，当前签到人数为{member_count},与实际结果1不同")
            raise AssertionError

        try:
            assert get_time in time_validate_range_list
        except AssertionError:
            logger.error(f"断言失败，当前签到时间为{get_time},不在{time_validate_range_list}范围区间内")
            raise AssertionError

