from os.path import dirname

# 测试用例数据目录
case_data_path = dirname(dirname(__file__)) + '/test_case/data/'
# 配置文件路径
config_path = dirname(dirname(__file__)) + '/config/config.ini'
# 日志路径
log_path = dirname(dirname(__file__)) + '/mylog.log'

if __name__ == '__main__':
    print(case_data_path)
    print(config_path)
    print(log_path)
