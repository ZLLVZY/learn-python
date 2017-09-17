# coding:utf-8

import xlrd

import xlwt

import requests

import urllib

import math

import re

pattern_x = re.compile(r'"lng":(.+?),')
pattern_y = re.compile(r'"lat":(.+?)}')

def get_mercator(addr):
    quote_addr1 = urllib.parse.quote(addr.encode('utf8'))
    quote_addr2 = urllib.parse.quote(u'红河哈尼彝族自治州'.encode('utf8'))
    html = "http://api.map.baidu.com/geocoder/v2/?callback=renderOption&output=json&address=%s&city=%s&ak=DD279b2a90afdf0ae7a3796787a0742e" %(quote_addr1,quote_addr2)
    req = requests.get(html)
    content = req.text
    x = re.findall(pattern_x, content)
    y = re.findall(pattern_y, content)
    return (x,y)

def run():

    data = xlrd.open_workbook('模板.xls')

    rtable = data.sheets()[0]

    nrows = rtable.nrows

    values = rtable.col_values(0)

 

    workbook = xlwt.Workbook()

    wtable = workbook.add_sheet('data', cell_overwrite_ok=True)

    row = 0

    for value in values:

        mercator = get_mercator(value)

        if mercator:

            wgs = mercator

        else:

            wgs = ('NotFound', 'NotFound')

        print("%s,%s,%s" % (value, wgs[0], wgs[1]))

        wtable.write(row, 0, value)

        wtable.write(row, 1, wgs[0])

        wtable.write(row, 2, wgs[1])

        row = row + 1

 

    workbook.save('data.xls')


 

if __name__ == '__main__':
    run()