import allure
import pytest
from selenium.webdriver.common.by import By

from common.file_read import load_case_data
from common.utils import BasePage
from conftest import browser


class TestMainPage(object):

    @allure.story('百度首页')
    @allure.title('百度搜索')
    @pytest.mark.parametrize('data', load_case_data('test_01.yaml')[0], ids=['case_name', 'case_name1'])
    def test_02(self, browser, data):
        """
            百度搜索
            :param browser:
            :param data:
            :return:
        """
        driver = BasePage(browser)
        driver.visit(data['url'])
        driver.input(*data['input'])
        driver.click(*data['click'])
        element = browser.find_element(By.XPATH, '//*[@class="toindex"]')
        driver.set_attribute(element, 'class', 'ffffffffffffffffff')
