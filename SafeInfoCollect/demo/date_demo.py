# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/31 16:57
@Author  : GGStudy-DDUp
@FileName: date_demo.py
@Software: PyCharm
@GitHub  : https://github.com/GGStudy-DDUp
"""

import requests
import time
import random
import SafeInfoCollect.settings as setting
from hashlib import md5
from fake_useragent import UserAgent


# 启明星辰——安全简讯
def date_venustech(li):
    title, date, url, tag = [], [], [], []
    x = li.index('安全分析')
    i = 0
    while i < len(li):
        if i < x:
            if i == li.index('安全工具'):
                i += 1
                title.append(li[i])
                date.append(li[i + 1])
                url.append(li[i + 2])
                tag.append('安全工具')
            else:
                title.append(li[i])
                date.append(li[i + 1])
                url.append(li[i + 2])
                tag.append('安全简讯')
                i += 3
        elif i == x:
            i += 1
        else:
            title.append(li[i])
            date.append(li[i])
            url.append(li[i + 1])
            tag.append('安全分析')
            i += 2
    return title, date, url, tag


# 启明星辰——安全通告
def date_venustech2(li):
    x = li.index('漏洞详情')
    y = li.index('安全建议')
    date = ''
    title = li[1].strip()
    for i in li[x + 1:y]:
        date += i.strip()
    return sqliteEscape(title), sqliteEscape(date)


# 有道翻译——英文转中文
def translate(date):
    try:
        ua = UserAgent()
        s = md5()
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        string = "fanyideskweb" + date + salt + setting.TRANSLATE_KEYWORD
        s.update(string.encode())
        sign = s.hexdigest()
        data = {
            "i": date,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": ts,
            "bv": "bdc0570a34c12469d01bfac66273680d",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }
        res = requests.post(
            url="https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule",
            data=data,
            headers={
                'User-Agent': str(ua.random),
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "Content-Length": "487",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie": setting.TRANSLATE_COOKIES,
                "Host": "fanyi.youdao.com",
                "Origin": "https://fanyi.youdao.com",
                "Referer": "https://fanyi.youdao.com/",
                "X-Requested-With": "XMLHttpRequest"
            }
        ).json()
        time.sleep(1)
        return res['translateResult'][0][0]['tgt']
    except:
        return date


# inforisktoday, securityaffairs——日期转换
def change_date(date):
    mon = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
           'December']

    try:
        str_mon = date.split()
        i = mon.index(str_mon[0])
        if i < 9:
            mon_int = '0' + str(i + 1)
        else:
            mon_int = str(i + 1)

        li = str_mon[1].split(',')
        if int(li[0]) < 10:
            date_int = '0' + li[0]
        else:
            date_int = li[0]

        date = str_mon[2].strip() + '-' + mon_int + '-' + date_int
        return date
    except:
        return date


# antiy——日期提取
def choise_date(date):
    try:
        return date.split()[1]
    except:
        return date


# SQLite——数据传入特殊字符转义
def sqliteEscape(keyWord):
    try:
        keyWord = keyWord.replace("/", "//")
        keyWord = keyWord.replace("'", "''")
        keyWord = keyWord.replace("[", "/[")
        keyWord = keyWord.replace("]", "/]")
        keyWord = keyWord.replace("%", "/%")
        keyWord = keyWord.replace("&", "/&")
        keyWord = keyWord.replace("_", "/_")
        keyWord = keyWord.replace("(", "/(")
        keyWord = keyWord.replace(")", "/)")
        return keyWord
    except:
        return keyWord
