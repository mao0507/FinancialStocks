# 與富果API取得連結
from fugle_realtime import HttpClient
import json
import os


# 給予富果API api_token
api_client = HttpClient(api_token='')
#api_client = HttpClient(api_token='demo')


# 開啟 JSON 檔案
with open("C:/Users/User/Desktop/code/FinancialStocks/python/model.json", encoding="utf-8") as f:
    # 讀取 JSON 檔案
    data = json.load(f)
    # 查看整個 JSON 資料解析後的結果
    #print(type(data))

    # 取得data.json現有紀錄股票編號
    arr = []
    for i in range(len(data)):
        # print(data[i]['股票號碼'])
        arr.append(data[i]['股票號碼'])
        stock = api_client.intraday.quote(symbolId=arr[i])
        print(stock.get('data'))
        # 檢查是否有出現需要欄位資料
        if stock.get('data','none') != 'none' :
            #有欄位才修改資料
            data[i]['股票當日收盤價'] = stock['data']['quote']['trade']['price']

    #print(json.dumps(data, ensure_ascii=False))

    file = open("C:/Users/User/Desktop/code/FinancialStocks/json/data.json",
                "w+", encoding="utf-8")
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()
    print('Update Finish..')
