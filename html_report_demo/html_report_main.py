import unittest
from datetime import datetime

from XTestRunner import HTMLTestRunner


class Env:
    now = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    report_dir = '../test_case/report_dir/'
    report_name = f'{report_dir}{now}.html'


# verbosity：报告的详细程度，只有0、1、2 ，2为最详细
if __name__ == '__main__':
    env = Env()
    report_name = env.report_name
    print(report_name)
    suit = unittest.defaultTestLoader.discover(start_dir='../test_case', pattern='t_*.py')
    with open(report_name, "wb") as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, title="XXX自动化测试报告", tester='gaofei',
                                description="欢迎关注公众号：大森玩测试", language='zh-CN')
        runner.run(suit)

    # runner.send_email(
    #     user="sender@qq.com",
    #     password="xxx",
    #     host="smtp.qq.com",
    #     to="recipient@126.com",
    #     attachments='report',
    #     ssl=True
    # )
    #
