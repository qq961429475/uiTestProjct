'''
    反射机制
'''
from selenium import webdriver


def open_browser(type_):
    # 基于反射的形态来简化代码
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


# 反射机制其实就是类的表达式
# 获取属性:在原有的类中，获取指定的属性
getattr(webdriver, 'Ie')
# 意思就是等于webdriver.Ie
# 如果要获取函数
getattr(webdriver, 'Chrome')()
# 意思就是等于webdriver.Chrome()
'''
    这三个，请看录播。因为我也没怎么用过。
    能否在函数上应用，课后试验
    写法：
        setattr(attrname,value)()
    如果不能用，就是不行。应该是不可以的。
'''
# 设置属性 ：在原有的类中，添加新的属性或者是修改已有属性的值
# setattr()
# 含有属性：在原有的类中，判断是否存在有指定的属性
# hasattr()
# 删除属性：在原有的类中，删除以存有的属性。
# delattr()
