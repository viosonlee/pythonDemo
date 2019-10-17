import os

from selenium import webdriver
import traceback
import downloader


def get_driver(url):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("headless")
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(url)

    return driver


def deal_li(li):
    # print(li.find_element_by_tag_name("a").get_attribute("href"))
    pi_driver = get_driver(
        li.find_element_by_tag_name("a").get_attribute("href"))
    # print(pi_driver.page_source)
    # title
    h1 = pi_driver.find_element_by_xpath(
        '//*[@class="photo-hd"]').find_element_by_tag_name('h1')
    title = h1.text.replace(":", "")
    print("title:%s" % title)

    div_pic = pi_driver.find_element_by_xpath('//*[@id="img"]')
    url = div_pic.find_element_by_tag_name('img').get_attribute("src")
    print("url:%s" % url)

    file_type = os.path.basename(url).split(".")[1]

    file_path = ("/Users/lyf/Pictures/crawler_images/%s.%s" % (title, file_type)) \
        .replace(" ", "")

    print(file_path)

    downloader.download_file(url, file_path)

    # 需要vip才能下载原尺寸
    # size_span = pi_driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[2]/p[2]/span')
    # print("size:%s"%size_span.text)
    pi_driver.close()


if __name__ == '__main__':
    page = 1
    base_url = 'http://pic.netbian.com/'
    while True:
        if page == 1:
            root_url = base_url
        else:
            root_url = "{}index_{}.html".format(base_url, page)
        print(root_url)
        my_driver = get_driver(root_url)
        # print(my_driver.page_source)
        try:
            ul_list = my_driver.find_element_by_xpath(
                '//*[@id="main"]/div[3]/ul')
            li_list = ul_list.find_elements_by_tag_name("li")
            for li_item in li_list:
                deal_li(li_item)
            my_driver.close()
            page += 1
        except:
            print(traceback.format_exc())
            break
