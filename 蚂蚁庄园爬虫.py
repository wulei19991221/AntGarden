# !/usr/bin/python3
# --coding:utf-8--
# @Author:吴磊
# @Time: 2020年04月23日11时
# @File: 蚂蚁庄园答案.py
from lxml import etree
import re
import time
import requests
from print_color import *


def get_max_page():
    max_page = 0
    try:
        r = requests.get(url).text
        htm = etree.HTML(r)
        last = htm.xpath('.//div[@class="page-container"]/a[last()]/@href')[0]
        max_page = re.findall("_(.*?).html", last)[0]
    except (AttributeError, TypeError):
        print_c(fred, '请重新检查网址')
    return max_page


def all_answers(counts):
    all_url = [f'https://www.youxi369.com/news/2254_{i}.html' for i in range(counts, 1, -1)]
    all_url.append(url)
    for i in all_url:
        content = ''
        r = requests.get(i).text
        htm = etree.HTML(r)
        ps = htm.xpath('.//div[@class="strategy-main-content"]/p')
        for p in ps[::-1]:
            text = ''.join(p.xpath('.//text()'))
            if '月' in text and '日' in text:
                content += text + '\n'
        content += '*' * 120 + '\n'
        with open(f'蚂蚁庄园每日答案{time.strftime("%y-%m-%d")}.txt', mode='a', encoding='utf-8') as f:
            f.write(content)


def get_latest_answer():
    current_time = list(time.strftime('%m月%d日'))
    if current_time[0] == '0':
        del current_time[0]
    if current_time[-3] == '0':
        del current_time[-3]
    current_time = ''.join(current_time)
    r = requests.get(url).text
    htm = etree.HTML(r)
    ps = htm.xpath('.//div[@class="strategy-main-content"]/p[position()<10]')
    for p in ps:
        today_ans = ''.join(p.xpath('.//text()'))
        if current_time in today_ans:
            print_c(fblue, today_ans)


def save_all_answer():
    page_num = int(get_max_page())
    all_answers(page_num)
    print_c('save all successful')


if __name__ == '__main__':
    start = time.time()
    url = 'https://www.youxi369.com/news/2254.html'
    # get_latest_answer()
    # save_all_answer()
    print_c(f'耗时: {time.time() - start:.2f}秒')
