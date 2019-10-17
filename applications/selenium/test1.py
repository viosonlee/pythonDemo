from time import sleep
import unittest
from selenium.config_file import browser_type, url
from selenium.get_browser import get_browser


class DeleteDevice(unittest.TestCase):
    def setUp(self):
        self.browser = get_browser(browser_type)
        self.browser.get(url)
        # 新增设备成功

    def test_delete_device_success(self):  # 删除设备成功
        self.browser.find_element_by_id("device").click()  # 找到设备管理菜单并点击
        self.browser.switch_to.frame("iframe_a")  # 切换到列表界面的iframe
        print("数量%d" % self.browser.page_source.count("deleteEquipment"))
        self.browser.find_element_by_xpath('''//*[@onclick="deleteEquipment('82499');"]''').click()
        self.browser.find_element_by_xpath('''//a[@class="l-btn l-btn-small"]''').click()

        sleep(5)
        after_str_count = self.browser.page_source.count("删除成功")
        self.assertEqual(after_str_count, 2)

    def test_reset_device_button(self):
        self.browser.find_element_by_id("device").click()
        self.browser.switch_to.frame("iframe_a")
        no_input = self.browser.find_element_by_xpath("""//input[@id="_easyui_textbox_input1"]""")
        no_input.click()
        test_no = "dddddd"
        no_input.send_keys(test_no)
        sleep(2)
        self.browser.find_element_by_xpath("""//input[@value="重置"]""").click()

        find_no = no_input.get_attribute("value")
        print("find_no%s" % find_no)
        if find_no == "" or find_no is None:
            print("重置成功")
        else:
            print("重置失败")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    suite = unittest.TestSuite()  # 实例化一个测试套件实例
    suite.addTest(DeleteDevice("test_reset_device_button"))
    runcase = unittest.TextTestRunner()  # 实例化一个测试用例执行器
    runcase.run(suite)  # 执行套件中的用例
