import os
import shutil
import pytest
from common.utils import tendency_data_operate

if __name__ == '__main__':
    pytest.main([])
    shutil.copy("config/environment.properties", "allure-results")
    os.system('allure generate ./allure-results/ -o ./allure-report/ --clean')
    tendency_data_operate()
    # os.system('allure open ./allure-report')
