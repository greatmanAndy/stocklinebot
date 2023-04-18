import mysql.connector
import pandas as pd
import requests
from stock import  stock_change
import re
from bs4 import BeautifulSoup
import emoji
import traceback

#新增股票到關注清單
def stock_database_add(message, user_id):
    try:
        if not re.match(r"[+-]?\d+$", message):
            message = stock_change(message)
            connection = mysql.connector.connect(host = "35.229.143.23",
                                                port = "3306",
                                                user = "root",
                                                password = "k&e5ry)'P&>E#8Z'",
                                                database = "stock_linebot",
                                                charset = 'utf8')
            cursor = connection.cursor()
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
            stock_id = df_4.values[0,0]
            stock_name = df_4.values[0,1]
            cursor.execute("SELECT stock_id, stock_name FROM `stock_subscribe` WHERE user_id='%s';" % (user_id))
            records = cursor.fetchall()
            s_d = pd.DataFrame(records,columns=["股票代號","股票名稱"])
            if str(stock_id) not in s_d["股票代號"].values:
                cursor.execute("INSERT INTO `stock_subscribe` (stock_id,stock_name,user_id) VALUES ('%s','%s','%s');" % (stock_id,stock_name,user_id))
                connection.commit()
                cursor.close()
                connection.close()
                return stock_id + stock_name + " 已關注"
            else:
                return stock_id + stock_name + " 已是關注股票"
    except Exception as e:
        traceback.print_exc()
        return "1查無您輸入的" + message + "，請重新輸入確認"

#刪除股票清單中的股票
def stock_database_del(message, user_id):
    try:
        if not re.match(r"[+-]?\d+$", message):
            message = stock_change(message)
        connection = mysql.connector.connect(host = "35.229.143.23",
                                            port = "3306",
                                            user = "root",
                                            password = "k&e5ry)'P&>E#8Z'",
                                            database = "stock_linebot",
                                            charset = 'utf8')
        cursor = connection.cursor()
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
        stock_id = df_4.values[0,0]
        stock_n = df_4.values[0,1]
        cursor.execute("SELECT stock_id, stock_name FROM `stock_subscribe` WHERE user_id='%s';" % (user_id))
        records = cursor.fetchall()
        s_d = pd.DataFrame(records,columns=["股票代號","股票名稱"])
        if str(stock_id) in s_d["股票代號"].values:
            cursor.execute("DELETE FROM `stock_subscribe` WHERE `id` = '%s' AND `user_id` = '%s';" % (stock_id, user_id))
            connection.commit()
            cursor.close()
            connection.close()
            return stock_id + stock_n + " 已取消關注"
        else:
            return stock_id + stock_n + " 並非已關注股票"
    except:
        return "查無您輸入的" + message + "，請重新輸入"

#查詢清單
def find_list(user_id):
    connection = mysql.connector.connect(host = "35.229.143.23",
                                        port = "3306",
                                        user = "root",
                                        password = "k&e5ry)'P&>E#8Z'",
                                        database = "stock_linebot",
                                        charset = 'utf8')
    cursor = connection.cursor()
    cursor.execute("SELECT stock_id, stock_name FROM `stock_subscribe` WHERE user_id='%s';" % (user_id))
    records = cursor.fetchall()
    s_d = pd.DataFrame(records,columns=["股票代號","股票名稱"])
    context = ""
    for i in range(len(s_d)):
        message = s_d.iloc[i][0]
        url = "https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID=" + str(message)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
        }
        res = requests.get(url,headers = headers)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text,"html.parser")
        soup1 = soup.find("table",{"class":"b1 p4_2 r10"})
        soup2 = soup1.find("tr",{"align":"center"}).text.split(" ")[1:-1]
        soup3 = soup.find("td",{"style":"padding:0 2px 5px 20px;width:10px;"})
        soup4 = soup3.find("a").text.split("\xa0")
        soup_1 = soup.find("td",{"style":"padding:0 18px 5px 0;text-align:right;"})
        star = emoji.emojize(':small_blue_diamond:')
        context += "{} {} 最新資訊 \n-------------------------- \n {}\n{} 最新成交價 : {} \n{} 開盤價 : {} \n{} 最高價 : {} \n{} 最低價 : {} \n{} 漲跌幅 : {} \n--------------------------\n".format(soup4[0],soup4[1],soup_1.text,star,soup2[0],star,soup2[5],star,soup2[6],star,soup2[7],star,soup2[3])
    return context
