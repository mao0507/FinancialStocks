#!/usr/bin/env python
# coding: utf-8

# In[172]:


# 引用
import requests
import re
import json
import os

# 使用套件 BeautifulSoup
from bs4 import BeautifulSoup

# 取得網址
response = requests.get(
    'http://jsjustweb.jihsun.com.tw/z/ze/zeb/zebb.djhtm?a=EB028000')
# 指定節點
soup = BeautifulSoup(response.text, 'html.parser')
# table內容
table = soup.find('table', class_='t01')
# tr內容
trs = table.find_all('tr')
# td內容
tds = soup.find_all('td')
# 輸出排版後的table內容
# print(table.prettify())
# 輸出tr內容


# 建立陣列
arr = []

for tr in trs:

    t3n1s = tr.find_all('td', class_='t3n1')
    t3t1s = tr.find_all('script')
    for td_t3t1 in t3t1s:
        # 取出資料，並刪除其他不需要符號
        td_t3t1_Text = td_t3t1.getText().replace('<!--', '').replace('//-->',
                                                                     '').replace('GenLink2stk(', '').replace(');', '').replace("'", "").replace('AS', '')
        # 去除前端空白
        str = re.sub(r"^\s+|\s+$", "", td_t3t1_Text)
        # 取出個股編號
        str = str.split(',')[0]
        # print(str) #檢查用

        # 建立Model，用來記錄數值
        Model = {
            '股票編號': '',
            '除息日': '',
            '盈餘發放': '',
            '公積發放': '',
            '股利小計': '',
            '股利發放日': '',
            '除權日': '',
            '盈餘配股': '',
            '公積配股': '',
            '股權小計': '',
        }

        # 將資料寫入dict
        Model['股票編號'] = str
        Model['除息日'] = t3n1s[0].getText().replace(u'\xa0', u'')
        Model['盈餘發放'] = t3n1s[1].getText().replace(u'\xa0', u'')
        Model['公積發放'] = t3n1s[2].getText().replace(u'\xa0', u'')
        Model['股利小計'] = t3n1s[3].getText().replace(u'\xa0', u'')
        Model['股利發放日'] = t3n1s[4].getText().replace(u'\xa0', u'')
        Model['除權日'] = t3n1s[5].getText().replace(u'\xa0', u'')
        Model['盈餘配股'] = t3n1s[6].getText().replace(u'\xa0', u'')
        Model['公積配股'] = t3n1s[7].getText().replace(u'\xa0', u'')
        Model['股權小計'] = t3n1s[8].getText().replace(u'\xa0', u'')
        # 將資料加入陣列
        arr.append(Model)

# 檢查陣列用
# print(arr)


# 開啟 JSON 檔案
with open("C:/Users/User/Desktop/code/FinancialStocks/json/data.json", encoding="utf-8") as f:
    # 讀取 JSON 檔案
    data = json.load(f)

# 開始跑回圈去紀錄資料 最外層從model.json開始
for i in range(len(data)):
    for x in range(len(arr)):
        if data[i]['股票號碼'] == arr[x]['股票編號']:
            data[i]['股票發放現金股利'] = arr[x]['股利小計']
            data[i]['股票發放股票股利'] = arr[x]['股權小計']
        # 檢查用
        # print('---')
        #print(data[i]['股票號碼'],data[i]['股票預計發放股利'],data[i]['股票發放股票股利'] )
        # print(arr[x]['股票編號'],arr[x]['股利小計'],arr[x]['股權小計'])
        # print('---')
        #print(' ')

# 寫入
file = open("C:/Users/User/Desktop/code/FinancialStocks/json/data.json",
            "w+", encoding="utf-8")
file.write(json.dumps(data, ensure_ascii=False))
file.close()
print('Update Finish..')
