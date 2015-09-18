#!/usr/bin/python python
# -*-coding:utf-8 -*-
__author__ = 'Clyde Ding'
import urllib, urllib2, httplib, cookielib
from lxml import etree as etree
import logging
import random
import logging.handlers
import threading
from threading import Timer
import re
import sys
import datetime
import time

reload(sys)
sys.setdefaultencoding('utf-8')


def auto_login_dfzq():
    name = ' '
    passwd = ' '
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36')]
    urllib2.install_opener(opener)
    url = "http://oa.orientsec.com.cn/names.nsf?Login"
    # 1 登录 设置cookie
    postdata = urllib.urlencode({
        'Username': name,
        'Password': passwd,
        'RedirectTo': '/oa/xtyfzb.nsf/kq?Openpage',
        '%%ModDate': 0000000000000000,
        '$PublicAccess': 1,
        'ReasonType': 0,
        '$$HTMLTagAttributes': 'lang=\"en\"'
    })
    req = urllib2.Request(url, postdata)
    urllib2.urlopen(req)
    req = urllib2.Request("http://oa.orientsec.com.cn/oa/kqgl_3.nsf/gr?openview")
    f2 = urllib2.urlopen(req)
    content = f2.read()
    # 2 寻找 签到 节点
    tree = etree.HTML(content)
    node = tree.xpath(u"/html/body/form/table[1]/tr/td[1]/a[1]/img")
    host = "http://oa.orientsec.com.cn"
    destURL = ""
    if node[0].tail == u' 签到':
        desURL = host + tree.xpath(u"/html/body/form/table[1]/tr/td[1]/a[1]/@href")[0]
    # 3 打开签到页面
    req = urllib2.Request(desURL)
    f3 = urllib2.urlopen(req)
    content = f3.read()
    # 4 检验签到页面是否为本人
    tree = etree.HTML(content)
    signName = tree.xpath(u"/html/body/form/font[3]")[0].text
    signContent = ""
    if signName == u'':
        actionURL = host + tree.xpath(u"/html/body/form/@action")[0]
        clickFunction = tree.xpath(u"/html/body/form/table/tr/td/a/@onclick")[0]
        P_ONCLICK = re.compile("\\D('(?P<onclick>\S+)',\\D)")
        # parse the string like : return _doClick('48257574002DDF3F.3184826b47e721bb4825689c002c0a96/$V5ACTIONS/0.17C', this, null)
        matcher = re.search(P_ONCLICK, clickFunction)
        if matcher is not None:
            account = matcher.group("onclick")
            postSignData = urllib.urlencode({
                '__Click': account,
                'sm': ''
            })
            req = urllib2.Request(actionURL, postSignData)
            f4 = urllib2.urlopen(req)
            signContent = f4.read()
            print signContent
            now = datetime.datetime.now().strftime('%H_%M_%S')
            logger.debug('Finish sign work at %s', now)
    return signContent


def is_sign_time():
    start_time = '08_30_00'
    end_time = '08_35_00'
    now = datetime.datetime.now().strftime('%H_%M_%S')
    logger.debug('Time string is  %s...', now)
    if start_time <= now <= end_time:
        return True
    else:
        return False


if __name__ == '__main__':
    # log config
    PATH = 'D:/opt/project/pyproject/'
    fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger = logging.getLogger('autoLogin')
    LOG_FILE = PATH + 'autoLogin.log'
    fileHandler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)
    fileHandler.setFormatter(fmt)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)

    if is_sign_time():
        logger.debug('Do sign work now...')
        auto_login_dfzq()
