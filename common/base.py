import datetime
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.driver.implicitly_wait(10)

    def visit(self, url):
        self.driver.get(url)

    @allure.step('查找元素')
    def find_element(self, method, locator):
        if method == "id":
            return self.driver.find_element(By.ID, locator)
        elif method == "name":
            return self.driver.find_element(By.NAME, locator)
        elif method == "class_name" or method == "class":
            return self.driver.find_element(By.CLASS_NAME, locator)
        elif method == "link_text":
            return self.driver.find_element(By.LINK_TEXT, locator)
        elif method == "partial_link_text":
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, locator)
        elif method == "tag_name" or method == "tag":
            return self.driver.find_element(By.TAG_NAME, locator)
        elif method == "xpath":
            return self.driver.find_element(By.XPATH, locator)
        elif method == "css_selector" or method == "css":
            return self.driver.find_element(By.CSS_SELECTOR, locator)

    @allure.step('点击元素')
    def click(self, method, locator):
        self.find_element(method, locator).click()

    @allure.step('输入文本')
    def input(self, method, locator, text):
        self.find_element(method, locator).send_keys(text)

    @allure.step('获取元素文本')
    def get_text(self, method, locator):
        return self.find_element(method, locator).text

    def get_attribute(self, method, locator, name):
        return self.find_element(method, locator).get_attribute(name)

    @allure.step('获取网页title')
    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def switch_to_frame(self, method, locator):
        return self.driver.switch_to.frame(self.find_element(method, locator))

    def switch_to_default(self):
        return self.driver.switch_to.default_content()

    def switch_to_window(self, index=0):
        return self.driver.switch_to.window((self.driver.window_handles[int(index)]))

    def quit(self):
        self.driver.quit()

    @allure.step('截图')
    def screen_shot(self, filename):
        self.driver.save_screenshot(filename)

    @allure.step('断言元素文本是否和期一致')
    def assert_text(self, method, locator, respect):
        try:
            assert self.get_text(method, locator) == respect
            return True
        except AssertionError:
            return False

    def sleep(self, num):
        time.sleep(num)
