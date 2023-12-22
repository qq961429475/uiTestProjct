import json
import os
import shutil
import pytest


# 趋势图数据处理
def tendency_data_operate():
    # 读取已备份的json文件
    r = json.load(open('history-trend_bak.json'))
    # 获取最大buildOrder序号值
    index = r[0]['buildOrder']

    # 读取最新history-trend.json值
    text2 = json.load(open('./allure_report/widgets/history-trend.json'))
    text2[0]['buildOrder'] = index + 1

    # 插入最新数据
    r.insert(0, text2[0])
    # 将最新数据覆盖原数据
    json.dump(r, open('history-trend_bak.json', 'w'), indent=4)
    # 写入./allure_report/widgets/history-trend.json
    json.dump(r, open('./allure_report/widgets/history-trend.json', 'w'))


if __name__ == '__main__':
    # 不要加-s参数，allure将stdout输出到allure报告，加了只会输出到console里
    # 用例执行步骤中会有一个stdout附件记录单个用例执行过程中的stdout
    pytest.main(["-v", "./test_case/test_case.py", "--alluredir", "./allure_result", "--clean-alluredir"])
    shutil.copy("environment.properties", "allure_result")
    os.system('allure generate ./allure_result/ -o ./allure_report/ --clean')
    tendency_data_operate()
    os.system('allure open ./allure_report')
