# -*- coding:utf-8 -*-
# @Time    :2021/3/20 13:54
# @Author  :ChloeeeeWang
# @Email   :403505960@qq.com
# @File    :.py
# @Software:PyCharm
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from common.yaml_handler import yaml_config
from common import globalmethod
from config.path import img_dir, join_dir_file
from common.logger_handler import logger


class BasePage:
    host = yaml_config['host']

    def __init__(self, driver_web: webdriver):
        self.driver = driver_web

    def goto(self,url:str):
        if url.startswith("http"):
            self.driver.get(url)
        else:
            full_url = self.host + url  # 当url是相对路径
            self.driver.get(full_url)
        return self


    def wait_element_visible(self,locator: tuple):
        """等待元素可见，并返回webElement"""
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=0.2)
            wait_ele = wait.until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException as e:
            logger.error(f"等待元素超时,无法找到元素：{e}")
            return None
        else:
            return wait_ele


    def wait_elements_visible(self, locator: tuple):
        """
        寻找元素，返回webelement对象，没有则返回None
        """
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=0.2)
            elements = wait.until(expected_conditions.visibility_of_all_elements_located(locator))
        except TimeoutException as e:
            logger.error(f"找不到该元素，请检查定位{locator}是否能正确定位：{e}")
            return None
        else:
            return elements


    def click_element(self, locator: tuple, force=False):
        """找到对应元素并点击
        """
        try:
            ele_target = self.wait_element_visible(locator)
        except TimeoutException as e:
            logger.error(f"定位超时，请检查定位{locator}是否能正确定位：{e}")
            raise TimeoutException
        else:
            logger.info(f"正在点击元素:{locator}")
            if not force:
                self.driver.execute_script("arguments[0].click()", ele_target)
            else:
                self.driver.execute_script("arguments[0].click({force: true})", ele_target)

    def scroll_and_click(self,locator: tuple,force=False):
        """滚动到可视的位置，并点击"""
        try:
            ele_target = self.driver.find_element(*locator)
        except NoSuchElementException as e:
            logger.error(f"找不到该元素，请检查定位{locator}是否能正确定位：{e}")
            raise NoSuchElementException
        else:
            target_el_located = ele_target.location_once_scrolled_into_view
            if not force:
                self.driver.execute_script("arguments[0].click()", ele_target)
            else:
                self.driver.execute_script("arguments[0].click({force: true})", ele_target)
        return self

    def switch_to_the_frame(self,locator:tuple):
        """
        等待并切换到iframe中
        """
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=0.2)
            wait_ele = wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(locator))
        except TimeoutException as e:
            logger.error(f"iframe等待超时，请检查frame的定位{locator}是否能正确定位：{e}")
            raise TimeoutException
        else:
            logger.info("已切换到iframe中")
        return self


    def send_text(self, locator: tuple, content):
        """向元素输入文字"""
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=1)
            el_account = wait.until(expected_conditions.visibility_of_element_located(locator))
            logger.info(f"找定位指定元素：{locator}")
        except TimeoutException as e:
            logger.error(f"找不到该元素，请检查定位{locator}是否能正确定位：{e}")
        else:
            logger.info(f"{locator}元素定位成功")
            el_account.send_keys(content)
        return self

    def double_click_ele(self,locator: tuple):
        """双击元素"""
        el_to_double_click = self.wait_element_visible(locator)
        ActionChains(self.driver).double_click(el_to_double_click).perform()
        return self

    def drag_and_drop_ele(self,start_locator: tuple, end_locator:tuple):
        """鼠标从start_locator拖拽到end_locator"""
        start_ele = self.wait_element_visible(start_locator)
        end_ele = self.wait_element_visible(end_locator)
        ActionChains(self.driver).drag_and_drop(start_ele,end_ele).perform()
        return self

    def mouse_hold_on(self,locator:tuple):
        ele = self.wait_element_visible(locator)
        ActionChains(self.driver).move_to_element(ele).perform()
        return self

    def get_element_attribute(self, locator: tuple, attr):
        """
        获得元素的属性值
        """
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=0.2)
            elements = wait.until(expected_conditions.visibility_of_element_located(locator))
            # elements = self.driver.find_elements(*locator)
        except TimeoutException as e:
            logger.error(f"找不到该元素，请检查定位{locator}是否能正确定位：{e}")
            return None
        else:
            att_txt = elements.get_attribute(attr)
            logger.info(f"{locator}找到了{attr}属性的值，值为：{att_txt}")
            return att_txt
        # return self.driver.find_element(*locator).get_attribute(attr)



    def get_element_text(self,locator:tuple):
        element = self.wait_element_visible(locator)
        element_txt = element.text
        return element_txt

    def screenshot(self):
        """截图"""
        current_time_str = globalmethod.get_current_time_str_time()
        file_name = f"screenshot-{current_time_str}.png"
        file = join_dir_file(img_dir, file_name)
        self.driver.get_screenshot_as_file(file)
        return self



if __name__ == "__main__":
    driver = webdriver.Chrome()

    bp = BasePage(driver)
    bp.goto("https://v4.ketangpai.com/User/login.html")
    driver.maximize_window()
    bp.send_text(('name','account'),"looker53@sina.com")
    bp.send_text(('name', 'pass'), "admin123456")
    import time
    time.sleep(12)
    driver.quit()



