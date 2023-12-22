import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu(unittest.TestCase):
    base_url = "https://www.baidu.com"

    def test(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        driver.find_element(By.ID, "kw").send_keys("selenium")
        driver.find_element(By.ID, "su").click()

        # 元素截图
        # elem = driver.find_element(By.ID, "su")
        # self.images.append(elem.screenshot_as_base64)
        # 竖屏截图
        self.images.append(driver.get_screenshot_as_base64())
        # 最大化截图
        # self.driver.maximize_window()
        self.images.append(driver.get_screenshot_as_base64())
        self.assertEqual(1, 2)

    def test_1(self):
        """
        这是test_01
        """
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        driver.find_element(By.ID, "kw").send_keys("selenium")
        driver.find_element(By.ID, "su").click()

        # 元素截图
        # elem = driver.find_element(By.ID, "su")
        # self.images.append(elem.screenshot_as_base64)
        # 竖屏截图
        self.images.append(driver.get_screenshot_as_base64())
        self.assertEqual(1, 1)

    def test_2(self):
        self.assertEqual(2, 2)
