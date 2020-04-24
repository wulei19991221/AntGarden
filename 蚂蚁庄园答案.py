# !/usr/bin/python3
# --coding:utf-8--
# @Author:吴磊
# @Time: 2020年04月23日11时
# @File: 蚂蚁庄园答案.py
from requests_html import HTMLSession
import re
import time


def get_max_page():
    max_page = 0
    try:
        r = session.get(url)
        last = r.html.find('.page-last', first=True).attrs['href']
        rule = re.compile("_(.*?).html")
        max_page = re.findall(rule, last)[0]
    except (AttributeError, TypeError):
        print('请重新检查网址')
    return max_page


def all_answers(counts):
    all_url = [f'https://www.youxi369.com/news/2254_{i}.html' for i in range(counts, 1, -1)]
    all_url.append(url)
    content = ''
    content_list = []
    for i in all_url:
        ps = session.get(i).html.find('.strategy-main-content p')
        for p in ps:
            if p.text not in content_list:
                content_list.append(p.text)
        content_list.sort()
        for j in content_list:
            content += j + '\n'
        content_list.clear()
        content += '*' * 120 + '\n'
    with open(f'蚂蚁庄园每日答案{time.strftime("%y-%m-%d")}.txt', mode='w', encoding='utf-8') as f:
        f.write(content)


def get_latest_answer():
    ps = session.get(url).html.find('.strategy-main-content p')
    print(ps[3].text)


def save_all_answer():
    page_num = int(get_max_page())
    all_answers(page_num)
    print('save all successful')


if __name__ == '__main__':
    start = time.time()
    session = HTMLSession()
    url = 'https://www.youxi369.com/news/2254.html'
    # get_latest_answer()
    save_all_answer()
    session.close()
    print(f'{time.time() - start:.2f}')
