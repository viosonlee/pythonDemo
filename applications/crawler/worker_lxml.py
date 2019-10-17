import os
import traceback
from urllib import request
from xml.etree.ElementTree import Element

import downloader
from config import url, dir_path
import http.client
from lxml import etree


def get_source(url):
    response = request.urlopen(url)  # type:http.client.HTTPResponse
    # print(response)
    source = response.read().decode("gbk")
    # print(source)
    return source


def deal_li(li):
    for map in li[0].items():  # type:map
        if map[0] == 'href':
            print(map[1])
            deal_detail_page(url + map[1])


def deal_detail_page(_url):
    root_ele = etree.HTML(get_source(_url))  # type:Element
    img_ele = root_ele.xpath('''//*[@id="img"]''')  # type :Element
    for img in img_ele[0]:  # type:Element
        print(img)
    src_url = ""
    title = ""
    for map in img.items():
        print(map)
        if map[0] == "src":
            src_url = url + map[1]
        if map[0] == "title":
            title = map[1]
    file_type = os.path.basename(src_url).split(".")[1]
    file_path = ("%s%s.%s" % (dir_path, title.replace("/", ""), file_type))
    print(file_path)
    downloader.download_file(src_url, file_path)


def deal_source(source):
    root_doc = etree.HTML(source)  # type: Element
    # print(root_doc)
    ul_list = root_doc.xpath('//ul[@class="clearfix"]')
    # print(ul_list[0].tag)
    for li in ul_list[0]:  # type:Element
        # print(li)
        deal_li(li)


if __name__ is "__main__":
    source = get_source(url)
    deal_source(source)
    page = 1
    while True:
        if page == 1:
            root_url = url
        else:
            root_url = "{}index_{}.html".format(url, page)
        print(root_url)
        try:
            source = get_source(root_url)
            deal_source(source)
            page += 1
        except:
            print(traceback.format_exc())
            break
