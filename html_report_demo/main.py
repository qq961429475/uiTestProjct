import unittest

from XTestRunner import HTMLTestRunner

if __name__ == '__main__':
    report = "./selenium_result.html"
    with(open(report, 'wb')) as fp:
        unittest.main(testRunner=HTMLTestRunner(
            stream=fp,
            tester="虫师",
            title='Selenium自动化测试报告',
            description=['类型：selenium', '操作系统：Windows', '浏览器：Chrome']
        ))
