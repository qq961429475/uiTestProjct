import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session", autouse=True)
def browser():
    """
        全局定义浏览器启动
    """

    global driver
    options = webdriver.ChromeOptions()
    # 加载cookie
    # options.add_argument(r"--user-data-dir=C:\Users\96142\AppData\Local\Google\Chrome\User Data")
    # 去掉密码管理弹窗
    prefs = dict()
    prefs["credentials_enable_services"] = False
    prefs["profiles.password_manager_enabled"] = False
    options.add_experimental_option('prefs', prefs)
    # 最大化
    options.add_argument("start-maximized")
    # 无头模式：
    # options.add_argument('--headless')
    # 去掉浏览器提示自动化黄条
    options.add_experimental_option('useAutomationExtension', False)
    # 禁用浏览器正在被自动化程序控制的提示
    options.add_argument('--disable-infobars')
    # 配置忽略HTTPS安全证书提示
    options.add_argument("--ignore-certificate-errors")
    # --no-sandbox 参数来禁用沙盒模式（因为权限会报错） (The process started from chrome location /usr/bin/google-chrome is no longer
    # running, so ChromeDriver is assuming that Chrome has crashed.)
    options.add_argument("--no-sandbox")
    chromedriver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(service=ChromeService(chromedriver_path), options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
    print("test end!")


def pytest_collection_modifyitems(items):
    """
    当ids用例别名乱码时,conftest里加
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    @pytest.mark.parametrize("input_title,",testdata["test_article"],ids=["新增文章"])
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode_escape")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param call:测试用例的测试步骤
　　         执行完常规钩子函数返回的report报告有个属性叫report.when
            先执行when=’setup’ 返回setup 的执行结果
            然后执行when=’call’ 返回call 的执行结果
            最后执行when=’teardown’返回teardown 的执行结果
    :param item:测试用例对象
    """
    # pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    # 获取调用结果的测试报告，返回一个report对象, report对象的属性包括when（steup, call, teardown三个值）、nodeid(测试用例的名字)、outcome(用例的执行结果，passed,
    # failed)
    report = outcome.get_result()
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            with allure.step("添加失败截图。。。"):
                allure.attach(driver.get_screenshot_as_png(),
                              "失败截图", allure.attachment_type.PNG)
