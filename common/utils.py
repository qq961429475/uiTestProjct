import json
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.log import get_logger

log = get_logger('./mylog.log')


class BasePage:
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
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

    def scroll_to_element(self, method, method_value):
        """
        """
        element = self.find_element(method, method_value)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        return element

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        return self.driver.execute_script("return document.body.scrollHeight;")

    # 滚动到指定位置
    def scroll_to_position(self, position):
        self.driver.execute_script("window.scrollTo(0, {});".format(position))

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def get_scroll_height(self):
        return self.driver.execute_script("return document.body.scrollHeight;")

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
            xpath = '//*[text()=\'{}\']'.format(toast_message)
            toast_element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_elment(By.XPATH, xpath),
                                                                      message='等待失败')
            print(toast_element.text)  # 打印toast文本
            assert toast_element.text == toast_message
            return True
        except:
            return False

    def add_attribute(self, elementobj, attributeName, value):
        """
        封装向页面标签添加新属性的方法
        调用JS给页面标签添加新属性，arguments[0]~arguments[2]分别
        会用后面的element，attributeName和value参数进行替换
        添加新属性的JS代码语法为：element.attributeName=value
        比如input.name='test'
        """
        self.driver.execute_script("arguments[0].%s=arguments[1]" % attributeName, elementobj, value)

    def set_attribute(self, elementobj, attributeName, value):
        """
        封装设置页面对象的属性值的方法
        调用JS代码修改页面元素的属性值，arguments[0]~arguments[1]分别
        会用后面的element，attributeName和value参数进行替换
        """
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", elementobj, attributeName,
                                   value)

    def get_attribute(self, elementobj, attributeName):
        # 封装获取页面对象的属性值方法
        return self.driver.elementobj, elementobj.get_attribute(attributeName)

    def remove_attribute(self, elementobj, attributeName):
        """
        封装删除页面属性的方法
        调用JS代码删除页面元素的指定的属性，arguments[0]~arguments[1]分别
        会用后面的element，attributeName参数进行替换
        """
        self.driver.execute_script("arguments[0].removeAttribute(arguments[1])",
                                   elementobj, attributeName)

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

    def assert_element_text(self, method, method_value, respect):
        try:
            assert self.get_text(method, method_value) == respect
            return True
        except AssertionError:
            return False

    def assert_url(self, respect):
        try:
            assert self.get_url() == respect
            return True
        except AssertionError:
            return False

    def assert_title(self, respect):
        try:
            assert self.get_title() == respect
            return True
        except AssertionError:
            return False

    def assert_attribute(self, method, method_value, name, respect):
        try:
            assert self.get_attribute(method, method_value, name) == respect
            return True
        except AssertionError:
            return False

    def assert_element_exist(self, method, method_value):
        try:
            assert self.find_element(method, method_value)
            return True
        except AssertionError:
            return False

    # 修改元素属性值
    def change_element_attribute(self, method, method_value, name, respect):
        self.find_element(method, method_value).set_attribute(name, respect)

    @staticmethod
    def sleep(num):
        time.sleep(num)


def tendency_data_operate():
    # 读取已备份的json文件
    r = json.load(open('./config/history-trend_bak.json'))
    # 获取最大buildOrder序号值
    index = r[0]['buildOrder']

    # 读取最新history-trend.json值
    text2 = json.load(open('./allure-report/widgets/history-trend.json'))
    text2[0]['buildOrder'] = index + 1

    # 插入最新数据
    r.insert(0, text2[0])
    # 将最新数据覆盖原数据
    json.dump(r, open('./config/history-trend_bak.json', 'w'), indent=4)
    # 写入./allure_report/widgets/history-trend.json
    json.dump(r, open('./allure-report/widgets/history-trend.json', 'w'))


if __name__ == '__main__':
    tendency_data_operate()
