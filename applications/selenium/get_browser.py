from selenium import webdriver
from selenium.config_file import time_out


def get_browser(browser_type):  # 定义一个获取浏览器的方法
    browser = None
    if browser_type == 'chrome':
        browser = webdriver.Chrome()  # 实例化一个谷歌浏览器
    elif browser_type == 'firefox':
        browser = webdriver.Firefox()
    elif browser_type == 'ie':
        browser = webdriver.Ie()
    elif browser_type == 'safari':
        browser = webdriver.Safari()
    else:
        print("请输入正确的浏览器类型")
    browser.maximize_window()  # 浏览器最大化
    browser.implicitly_wait(time_out)
    return browser
