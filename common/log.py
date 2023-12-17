import logging
from logging.handlers import RotatingFileHandler

# 创建logger对象
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 创建FileHandler对象
fh = logging.FileHandler('../mylog.log', 'a')
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式（formatter）
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# 4、给handler添加formatter
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 5、给logger添加handler
logger.addHandler(fh)

# 输出到控制台
logger.addHandler(ch)

# def get_logger(log_file_path):
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.DEBUG)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     # 创建一个handler，用于写入日志文件
#     file_handler = RotatingFileHandler(log_file_path, maxBytes=1024 * 1024 * 10, backupCount=5)
#     file_handler.setLevel(logging.DEBUG)
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)
#     # 创建一个handler，用于输出到控制台
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(logging.DEBUG)
#     console_handler.setFormatter(formatter)
#     logger.addHandler(console_handler)
#     return logger
