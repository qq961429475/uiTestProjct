// 基于ini配置文件的log模块使用模板
import logging.config
logging.config.fileConfig('log.ini')
log = logging.getLogger()
log.info('11111111111')
//保持cookie的两种方法

1. options添加配置
   options.add_argument(r"user-data-dir=C:\Users\96142\AppData\Local\Google\Chrome\User Data_Backup")
2. 用pickle保存cookie，再读取
   driver = webdriver.Chrome()
   i do my login here
   保存cookies
   driver.get('')
   pickle.dump(driver.get_cookies(), open("name.pkl", "wb"))
   打开浏览器
   driver.get('https://www.baidu.com')
   加载cookies
   for cookie in pickle.load(open("cookies1.pkl", "rb")):
   driver.add_cookie(cookie)
   再打开网址
   driver.get('https://www.baidu.com')


