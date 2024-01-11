import json
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir=C:\Users\96142\AppData\Local\Google\Chrome\User Data")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def visit(self, url):
        self.driver.get(url)

    def find_element(self, method, method_value):
        if method == "id":
            return self.driver.find_element(By.ID, method_value)
        elif method == "name":
            return self.driver.find_element(By.NAME, method_value)
        elif method == "class_name" or method == "class":
            return self.driver.find_element(By.CLASS_NAME, method_value)
        elif method == "link_text" or method == 'text':
            return self.driver.find_element(By.LINK_TEXT, method_value)
        elif method == "partial_link_text":
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, method_value)
        elif method == "tag_name" or method == "tag":
            return self.driver.find_element(By.TAG_NAME, method_value)
        elif method == "xpath":
            return self.driver.find_element(By.XPATH, method_value)
        elif method == "css_selector" or method == "css":
            return self.driver.find_element(By.CSS_SELECTOR, method_value)

    # 隐式等待元素出现
    def wait_element(self, method, method_value):
        if method == "id":
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.ID, method_value),
                                                             message='等待失败')
        elif method == "name":
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.NAME, method_value),
                                                             message='等待失败')
        elif method == "class_name" or method == "class":
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.CLASS_NAME, method_value),
                                                             message='等待失败')
        elif method == "link_text" or method == 'text':
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.LINK_TEXT, method_value),
                                                             message='等待失败')
        elif method == "partial_link_text":
            return WebDriverWait(self.driver, 10, 0.5).until(
                lambda x: x.find_element(By.PARTIAL_LINK_TEXT, method_value), message='等待失败')
        elif method == "tag_name" or method == "tag":
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.TAG_NAME, method_value),
                                                             message='等待失败')
        elif method == "xpath":
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(By.XPATH, method_value),
                                                             message='等待失败')

    def click(self, method, method_value):
        self.find_element(method, method_value).click()

    def input(self, method, method_value, text):
        self.find_element(method, method_value).send_keys(text)

    def get_text(self, method, method_value):
        return self.find_element(method, method_value).text

    def move_to_element(self, method, method_value):
        element = self.find_element(method, method_value)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def move_element(self, draggable_element, target_element):
        """
        :param draggable_element: 拖拽元素
        :param target_element: 目标元素
        """
        actions = ActionChains(self.driver)
        actions.drag_and_drop(draggable_element, target_element).perform()

    def slide_element(self, draggable_element, xoffset, yoffset):
        """
        :param draggable_element: 拖拽元素
        :param xoffset: 横向偏移量
        :param yoffset: 纵向偏移量
        """
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(draggable_element, xoffset, yoffset).perform()

    def assert_toast_element(self, toast_message):
        try:
            xpath = '//*[@text=\'{}\']'.format(toast_message)
            toast_element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_elment(By.XPATH, xpath),
                                                                      message='等待失败')
            print(toast_element.text)  # 打印toast文本
            if toast_element.text == toast_message:
                return True
            else:
                return False
        except Exception as e:
            return e

    def get_attribute(self, method, method_value, name):
        return self.find_element(method, method_value).get_attribute(name)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def switch_to_frame(self, method, method_value):
        return self.driver.switch_to.frame(self.find_element(method, method_value))

    def switch_to_default(self):
        return self.driver.switch_to.default_content()

    def switch_to_window(self, index=0):
        return self.driver.switch_to.window((self.driver.window_handles[int(index)]))

    def quit(self):
        self.driver.quit()

    def screen_shot(self, filename):
        self.driver.save_screenshot(filename)

    def assert_text(self, method, method_value, respect):
        try:
            assert self.get_text(method, method_value) == respect
            return True
        except AssertionError:
            return False

    @staticmethod
    def sleep(num):
        time.sleep(num)


def tendency_data_operate():
    # 读取已备份的json文件
    r = json.load(open('../config/history-trend_bak.json'))
    # 获取最大buildOrder序号值
    index = r[0]['buildOrder']

    # 读取最新history-trend.json值
    text2 = json.load(open('../allure_report/widgets/history-trend.json'))
    text2[0]['buildOrder'] = index + 1

    # 插入最新数据
    r.insert(0, text2[0])
    # 将最新数据覆盖原数据
    json.dump(r, open('../config/history-trend_bak.json', 'w'), indent=4)
    # 写入./allure_report/widgets/history-trend.json
    json.dump(r, open('../allure_report/widgets/history-trend.json', 'w'))


if __name__ == '__main__':
    tendency_data_operate()
