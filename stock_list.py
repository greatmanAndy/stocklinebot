import pandas as pd
import requests
from flask import g
import re
from stock import stock_change


def stock_database_add(message):
    print("123")
    try:
        if not re.match(r"[+-]?\d+$", message):
            message = stock_change(message)
        url_ = "https://isin.twse.com.tw/isin/class_main.jsp?owncode=&stockname=&isincode=&market=1&issuetype=1&industry_code=&Page=1&chklike=Y"
        df_ = pd.read_html(requests.get(url_).text)[0]
        df_ = df_.iloc[:,2:7]
        df_.columns = df_.iloc[0,:]
        df_ = df_[1:]
        url2 = "https://isin.twse.com.tw/isin/class_main.jsp?owncode=&stockname=&isincode=&market=2&issuetype=4&industry_code=&Page=1&chklike=Y"
        df_2 = pd.read_html(requests.get(url2).text)[0]
        df_2 = df_2.iloc[:,2:7]
        df_2.columns = df_2.iloc[0,:]
        df_2 = df_2[1:]
        df_3 = pd.concat([df_,df_2])
        df_4 = df_3[df_3["有價證券代號"] == message]
        stock_i = df_4.values[0,0]
        stock_n = df_4.values[0,1]
        sql = '''
            SELECT *
              FROM [linebot].[dbo].[Stocklist]
        '''
        print(sql)
        result = pd.read_sql(sql=sql, con=g.cnxn, coerce_float=True)
        if str(stock_i) not in result["Symbol"].values:
            Insert_sql = '''
                INSERT INTO Stocklist (Symbol,Name) VALUES (N'{}',N'{}')
            '''.format(stock_i,stock_n)
            print(Insert_sql)
            cursor = g.cnxn.cursor()
            cursor.execute(Insert_sql)
            cursor.commit()

            return stock_i + stock_n + " 已關注"
        else:
            return stock_i + stock_n + " 已是關注股票"
    except Exception as e:
        print(e)
        return "查無您輸入的訊息，請重新輸入確認"