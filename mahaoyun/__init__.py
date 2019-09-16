#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 18:11:06 2019

@author: mahaoyun
"""

from bs4 import BeautifulSoup
import requests, zipfile, io, os,rarfile
import re
import lxml
import urllib


def get_unzip_pdf(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    for i in soup.find_all('a', zcmsattachrela=re.compile('\d')):
        a = i.get('href')
        print(a)
        r = requests.get(a)
        if zipfile.is_zipfile(io.BytesIO(r.content)):
           z = zipfile.ZipFile(io.BytesIO(r.content))
           for file in z.namelist():
              filename = file.encode('cp437').decode('gbk')
              print(filename)
              z.extract(file, r'/Users/mahaoyun/Desktop/download_huaxia')
              os.chdir(r'/Users/mahaoyun/Desktop/download_huaxia')
              os.rename(file, filename)
#        elif rarfile.is_rarfile(io.BytesIO(r.content)):
#           z = rarfile.RarFile(io.BytesIO(r.content))
#           z.extract(file, r'/Users/mahaoyun/Desktop/download_huaxia')

find_value = '年度报告'
find_value = urllib.parse.quote(find_value, encoding='gbk')
index_url = 'http://fund.chinaamc.com/portal/cn/gsgg4zcms/informationNotice.jsp?pageIndex=0&title={}startDate=&endDate='.format(find_value)
html = requests.get(index_url)
soup = BeautifulSoup(html.text, 'lxml')
page_index = int(soup.find_all('span', class_='fc_ch1')[1].get_text())
for i in range(page_index):
    url = 'http://fund.chinaamc.com/portal/cn/gsgg4zcms/informationNotice.jsp?pageIndex={}&title={}&startDate=&endDate='.format(i, find_value)
    child_html = requests.get(url).text
    soup = BeautifulSoup(child_html,'lxml')
    for child_url in soup.find_all('a', target='_blank'):
        get_unzip_pdf(child_url.get('href'))


# url = 'http://www.chinaamc.com/guanyu/gonggao/index.shtml'