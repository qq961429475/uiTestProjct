import time

import pytest
from selenium.webdriver.common.by import By

from test_case.test_baidu_mainpage.baidu_mainpage import BaiDuMainPage


class TestDemo:
    def test_search(self, browser):
        driver = BaiDuMainPage(browser)
        driver.open_baidu_url()
        driver.search("selenium")
        assert "baidu" == driver.find_element('xpath', '//*[@id="u"]/a[1]').text

    def test_click_news(self, browser):
        driver = BaiDuMainPage(browser)
        driver.open_baidu_url()
        driver.click_news()
        driver.switch_to_window(-1)
        status = driver.assert_element_text('text', '热点要闻', '热点要闻')
        assert status

    def test_change(self, browser):
        driver = BaiDuMainPage(browser)
        driver.open_baidu_url()
        driver.driver.find_element(By.ID, 'kw').send_keys('selenium')
        time.sleep(5)


if __name__ == '__main__':
    pytest.main(["-s", '-v', "test_baidu_mainpage.py"])
