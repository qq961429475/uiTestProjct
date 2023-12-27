import datetime
import time


# 统计执行时间的闭包函数
def time_count(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"执行时间为：{end - start}")
        # return res

    return wrapper


# 对时间格式化的闭包函数
def time_format(func):
    def wrapper():
        res = func()
        # 将时间格式化为年月日时分秒
        aa = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(res))
        # print(aa)
        return aa

    return wrapper


@time_format
def get_time():
    tt = 1703678852.4704676
    return tt


print(get_time())
