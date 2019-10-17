import ast
import datetime
import re
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

curr_date = datetime.datetime(2002, 1, 31, 0, 0)
earl_date = datetime.datetime(2001, 12, 31, 0, 0)
curr_sec = time.mktime(curr_date.timetuple())
earl_sec = time.mktime(earl_date.timetuple())
only_earl_year = str(datetime.datetime.fromtimestamp(earl_sec).year)
only_earl_month = str(datetime.datetime.fromtimestamp(earl_sec).month)
space_list = [' ', '\n', '\t', '\r']
total_news = list()

while curr_sec >= earl_sec:
    only_date = str(datetime.datetime.fromtimestamp(curr_sec).date())
    curr_year = str(datetime.datetime.fromtimestamp(curr_sec).year)
    curr_month = str(datetime.datetime.fromtimestamp(curr_sec).month)
    base_url = 'http://fund.megabank.com.tw/ETFData/djjson/ETNEWSjson.djjson?a=4&b=%s'
    base_url = base_url % (only_date)
    base_html = requests.get(base_url)
    base_html = base_html.text
    print(base_html)
    base_soup = BeautifulSoup(base_html, features='lxml')
    summary = base_soup.find('p')
    if summary is not None:
        for s in summary:
            # eolhandle()這裡插入
            s = ast.literal_eval(s)
            for d in s['ResultSet']['Result']:
                news, news_str = list(), str()
                reformatted_date = datetime.datetime.strptime(d['V1'], '%Y/%m/%d').strftime('%Y-%m-%d')
                content_url = 'http://fund.megabank.com.tw/ETFData/djhtm/ETNEWSContentMega.djhtm?TYPE=4&DATE=%s&A=%s'
                content_url = content_url % (reformatted_date, d['V3'])
                if reformatted_date != only_date:
                    break
                else:
                    content_html = requests.get(content_url)
                    content_html = content_html.text
                    content_soup = BeautifulSoup(content_html, features='lxml')
                    content = content_soup.find_all('p')
                    try:
                        if bool(re.search('(\d{4})[/.-](\d{2})[/.-](\d{2})', content[0].getText())):
                            content = content[1:]
                        if '編者按' in content[-1].getText():
                            content = content[:-1]
                        for c in content:
                            news_str += c.getText()
                        news.extend([reformatted_date, d['V2'], news_str, d['V3']])
                    except IndexError:
                        news.extend([reformatted_date, d['V2'], '', d['V3']])
                total_news.append(news)
            print('已爬完%s的新聞' % (only_date))
    curr_sec -= 86400.0
    yest_month = str(datetime.datetime.fromtimestamp(curr_sec).month)
    if curr_month != yest_month:
        table = pd.DataFrame(total_news, columns=['日期', '標題',  '內文', '編號'])
        table.to_csv('D:/python_note/Project/financial news/%s/%s.csv' % (curr_year, curr_year+'-'+curr_month))
        total_news = list()
