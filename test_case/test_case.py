import os
import pytest
from conftest import browser
import allure
from common.base import BasePage as bp
from common.file_read import read_yaml


class TestLogin():

    @pytest.mark.parametrize('data', read_yaml("111.yaml"))
    def test_01(self, data):
        print('开始测试')
        print(str(data))
        assert 1 == 1

    @allure.story('百度首页')
    @allure.feature('搜索模块')
    @allure.title('百度搜索')
    @pytest.mark.parametrize('data', read_yaml('111.yaml'), ids=['case_name', 'case_name1'])
    def test_02(self, browser, data):
        """
            百度搜索
            :param browser:
            :param data:
            :return:
        """
        driver = bp(browser)
        driver.visit(data['url'])
        driver.input(*data['input'])
        driver.click(*data['click'])
        assert driver.get_title() == data['expected']

    def test03(self):
        assert 1 == 1


if __name__ == '__main__':
    # 不要加-s参数，allure将stdout输出到allure报告，加了只会输出到console 里
    # 用例执行步骤中会有一个stdout附件记录单个用例执行过程中的stdout
    pytest.main(['-m', "test_case.py", "--alluredir", "./allure_result", "--clean-alluredir"])
    os.system('allure generate ./allure_result/ -o ./allure_report/ --clean')
    os.system('allure serve allure_result')
