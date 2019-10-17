import random
import unittest
from time import sleep
from selenium.get_browser import get_browser


class AddDevice(unittest.TestCase):
    def setUp(self):
        self.browser = get_browser()
        self.browser.get("http://118.24.178.224:8180/examples/home.html")
        # 新增设备成功

    def test_add_device_success(self):
        # 输入浏览器网址
        self.browser.find_element_by_id("device").click()  # 找到设备管理菜单并点击
        # 第一种方式切换iframe
        # browser.switch_to.frame("iframe_a")
        # 第二种方式切换iframe
        iframe = self.browser.find_element_by_xpath("//iframe[@name='iframe_a']")
        self.browser.switch_to.frame(iframe)
        self.browser.find_element_by_xpath("//input[@value='新增']").click()  # 找到新增元素并点击
        # 切换至新增页面iframe
        self.browser.switch_to.frame("showMyWindowId")
        # 生成五位数的随机数
        device_num = random.randint(10000, 99999)
        # 找到新增页面编号输入框并输入编号为生成的随机数
        sleep(5)
        self.browser.find_element_by_xpath("//input[@id='_easyui_textbox_input1']").send_keys(device_num)
        # 找到新增页面名称输入框并输入名称为aaaa
        self.browser.find_element_by_xpath("//input[@id='_easyui_textbox_input2']").send_keys("aa8888aa")
        # 找到新增页面确定按钮并点击
        self.browser.find_element_by_xpath("//a[text()='确定']").click()
        sleep(5)
        # 验证预期结果与实际结果是否相符（验证编号是否添加成功）
        # 返回上级iframe
        self.browser.switch_to.parent_frame()
        self.assertIsNotNone(self.browser.find_element_by_xpath("//div[text()='{}']".format(device_num)))

    # 新增设备失败
    def test_add_device_fail01(self):
        # 1、新增设备失败——编号只能为5个字符

        self.browser.find_element_by_id("device").click()  # 找到设备管理菜单并点击
        # 第一种方式切换iframe
        # browser.switch_to.frame("iframe_a")
        # 第二种方式切换iframe
        iframe = self.browser.find_element_by_xpath("//iframe[@name='iframe_a']")
        self.browser.switch_to.frame(iframe)
        sleep(3)
        self.browser.find_element_by_xpath("//input[@value='新增']").click()  # 找到新增元素并点击
        # 切换至新增页面iframe
        self.browser.switch_to.frame("showMyWindowId")
        sleep(3)
        # 找到新增页面编号输入框并输入编号为666666
        self.browser.find_element_by_xpath("//input[@id='_easyui_textbox_input1']").send_keys("666666")
        # 找到新增页面名称输入框并输入名称为aaaa
        self.browser.find_element_by_xpath("//input[@id='_easyui_textbox_input2']").send_keys("aaaa")
        # 统计当先页面源码中“编号只能为5个字符”的次数
        # before_str_count = browser.page_source.count("编号只能为5个字符")
        # print(before_str_count)
        # 找到新增页面确定按钮并点击
        self.browser.find_element_by_xpath("//a[text()='确定']").click()
        sleep(5)
        # 验证预期结果与实际结果是否相符（验证编号超过5个字符的时候出现“编号只能为5个字符”提示字符）
        # 统计当先页面源码中“编号只能为5个字符”的次数
        after_str_count = self.browser.page_source.count("编号只能为5个字符")
        self.assertEqual(after_str_count, 2)

    def test_add_device_fail02(self):
        # 2、新增设备失败——姓名不能为空
        self.browser.find_element_by_id("device").click()  # 找到设备管理菜单并点击
        # 第一种方式切换iframe
        # browser.switch_to.frame("iframe_a")
        # 第二种方式切换iframe
        iframe = self.browser.find_element_by_xpath("//iframe[@name='iframe_a']")
        self.browser.switch_to.frame(iframe)
        self.browser.find_element_by_xpath("//input[@value='新增']").click()  # 找到新增元素并点击
        # 切换至新增页面iframe
        self.browser.switch_to.frame("showMyWindowId")
        sleep(3)
        # 找到新增页面编号输入框并输入编号为64666
        self.browser.find_element_by_xpath("//input[@id='_easyui_textbox_input1']").send_keys("64666")
        # before_str_count = browser.page_source.count("姓名不能为空")
        # 统计当先页面源码中“姓名不能为空的”的次数
        # print(before_str_count)
        # 找到新增页面确定按钮
        self.browser.find_element_by_xpath("//a[text()='确定']").click()
        sleep(5)
        # 验证预期结果与实际结果是否相符（验证姓名为空的时候出现“姓名不能为空”的提示字符）
        # 统计当先页面源码中“姓名不能为空的”的次数
        after_str_count = self.browser.page_source.count("姓名不能为空")
        print(after_str_count)
        self.assertEqual(after_str_count, 2)

    def test_add_device_fail03(self):
        # 3、新增设备失败——编号不能为空
        self.browser.find_element_by_id("device").click()  # 找到设备管理菜单并点击
        # 第一种方式切换iframe
        # browser.switch_to.frame("iframe_a")
        # 第二种方式切换iframe
        iframe = self.browser.find_element_by_xpath("//iframe[@name='iframe_a']")
        self.browser.switch_to.frame(iframe)
        sleep(5)
        self.browser.find_element_by_xpath("//input[@value='新增']").click()  # 找到新增元素并点击
        # 切换至新增页面iframe
        self.browser.switch_to.frame("showMyWindowId")
        sleep(5)
        # 找到新增页面名称输入框并输入名称为aaaa
        self.browser.find_element_by_xpath("//input[@id='_easyui_textbox_input2']").send_keys("aaaa")
        # 统计当先页面源码中“编号不能为空”的次数
        # before_str_count = browser.page_source.count("编号不能为空")
        # print(before_str_count)
        # 找到新增页面确定按钮并点击
        self.browser.find_element_by_xpath("//a[text()='确定']").click()
        sleep(5)
        # 验证预期结果与实际结果是否相符（验证编号超过5个字符的时候出现“编号不能为空”提示字符）
        # 统计当先页面源码中“编号不能为空”的次数
        after_str_count = self.browser.page_source.count("编号不能为空!")
        print(after_str_count)
        self.assertEqual(after_str_count, 2)

    def tearDown(self):
        self.browser.quit()


suite = unittest.TestSuite()  # 实例化一个测试套件实例
suite.addTest(AddDevice.test_add_device_fail03)
