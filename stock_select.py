import requests
from bs4 import BeautifulSoup
import re
from stock import *
from linebot.models import *
import emoji

#地雷股檢測
def select_1(message):
  print("123")
  if not re.match(r"[+-]?\d+$", message):
        message = stock_change(message)
  url = "https://goodinfo.tw/StockInfo/StockFinDetail.asp"
  headers = {
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
      'referer': 'https://goodinfo.tw/StockInfo/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID=' + str(message)
  }
  data = {
      "STEP": "DATA",
      "STOCK_ID": str(message),
      "RPT_CAT": "XX_M_YEAR",
  }
  res = requests.post(url,headers = headers,data = data)
  res.encoding = "utf-8"
  soup = BeautifulSoup(res.text,"html.parser")
  soup_t1 = soup.find_all("tr",{"class":"bg_h1 fw_normal"})[0]
  title = soup_t1.find_all("nobr")[:4]
  soup1 = soup.find_all("tr",{"bgcolor":"white"})
  for i in range(len(soup1)):
      if soup1[i].find_all("nobr")[0].text == "每股自由現金流量\xa0(元)": #自由現金流量
          fcfps = soup1[i].find_all("nobr")[:6] 
      if soup1[i].find_all("nobr")[0].text == "每股稅後盈餘\xa0(元)": #每股稅後盈餘
          eps = soup1[i].find_all("nobr")[:6] 
      if soup1[i].find_all("nobr")[0].text =="負債總額年成長率": #負債總額年成長率
          debt = soup1[i].find_all("nobr")[:6] 
      if soup1[i].find_all("nobr")[0].text == "股東權益報酬率": #股東權益報酬率
          roe = soup1[i].find_all("nobr")[:6]
      if soup1[i].find_all("nobr")[0].text == "資產報酬率": #資產報酬率
          roa = soup1[i].find_all("nobr")[:6]
  sum_count = 0
  #自由現金流量近五年有三年> 0
  count_1 = 0  
  for i in fcfps[1:]:
      if float(i.text) > 0:
          count_1 += 1
  if count_1 >= 3:
      a = "{} 通過 自由現金流量近五年有三年 > 0 ({}/5)".format(emoji.emojize(':green_circle:',use_aliases=True),count_1)
  else:
      a = "{} 沒過 自由現金流量近五年有三年 > 0 ({}/5)".format(emoji.emojize(':x:',use_aliases=True),count_1)
      sum_count += 1
  #自由現金流量近五年平均> 0
  sum_1 = 0
  for i in fcfps[1:]:
      sum_1 += float(i.text)
  av_1 = sum_1/5
  if  av_1> 0:
      b = "{} 通過 自由現金流量近五年平均大於 > 0 ({:.2f}元)".format(emoji.emojize(':green_circle:',use_aliases=True),av_1)
  else:
      b = "{} 沒過 自由現金流量近五年平均大於 > 0 ({:.2f}元)".format(emoji.emojize(':x:',use_aliases=True),av_1)
      sum_count += 1
  #每股稅後盈餘近五年有三年大>0
  count_2 = 0
  for i in eps[1:]:
      if float(i.text) > 0:
          count_2 += 1
  if count_2 >= 3:
      c = "{} 通過 每股稅後盈餘近五年有三年大於 > 0 ({}/5)".format(emoji.emojize(':green_circle:',use_aliases=True),count_2)
  else:
      c = "{} 沒過 每股稅後盈餘近五年有三年大於 > 0 ({}/5)".format(emoji.emojize(':x:',use_aliases=True),count_2)
      sum_count += 1
  #自由現金流量近五年平均> 0
  sum_2 = 0
  for i in eps[1:]:
      sum_2 += float(i.text)
  av_2 = sum_2/5
  if  av_2> 0:
      d = "{} 通過 每股稅後盈餘近五年平均大於 > 0 ({:.2f}元)".format(emoji.emojize(':green_circle:',use_aliases=True),av_2)
  else:
      d = "{} 沒過 每股稅後盈餘近五年平均大於 > 0 ({:.2f}元)".format(emoji.emojize(':x:',use_aliases=True),av_2)
      sum_count += 1
  #負債總額年成長率平均<20%
  sum_3 = 0
  for i in debt[1:]:
      sum_3 += float(i.text)
  av_3 = sum_3/5
  if  av_3< 20:
      e = "{} 通過 負債總額年成長率平均<20% ({:.2f}%)".format(emoji.emojize(':green_circle:',use_aliases=True),av_3)
  else:
      e = "{} 沒過 負債總額年成長率平均<20% ({:.2f}%)".format(emoji.emojize(':x:',use_aliases=True),av_3)
      sum_count += 1
  #ROE近五年有三年 > ROA
  count_3 = 0
  for i,j in zip(roe[1:],roa[1:]):
      if float(i.text) > float(j.text):
          count_3 += 1
  if count_3 == 5:
      f = "{} 通過 ROE近五皆 > ROA ({}/5)".format(emoji.emojize(':green_circle:',use_aliases=True),count_3)
  else:
      f = "{} 沒過 ROE近五年皆 > ROA ({}/5)".format(emoji.emojize(':x:',use_aliases=True),count_3)
      sum_count += 1
  #ROE近五年有三年> 10%
  count_4 = 0
  for i in roe[1:]:
      if float(i.text) > 10:
          count_4 += 1
  if count_4 >= 3:
      g = "{} 通過 ROE近五年有三年> 10% ({}/5)".format(emoji.emojize(':green_circle:',use_aliases=True),count_4)
  else:
      g = "{} 沒過 ROE近五年有三年> 10% ({}/5)".format(emoji.emojize(':x:',use_aliases=True),count_4)
      sum_count += 1
  #暴雷程度
  thunder = sum_count / 7 *100
  sum = "{} 暴雷程度 : {:.2f}%".format(emoji.emojize(':zap:',use_aliases=True),thunder)
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
  title_ = df_4.values[0,0] + " " + df_4.values[0,1]
  message = FlexSendMessage(
              alt_text = '陳陳的嘉理',
              contents = {
    "type": "bubble",
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": str(title_),
          "weight": "bold",
          "size": "xxl",
          "margin": "none",
          "wrap": True,
          "align": "center"
        },
        {
          "type": "text",
          "text": "地雷股檢測報告",
          "weight": "bold",
          "size": "xxl",
          "margin": "none",
          "wrap": True,
          "align": "center"
        },
        {
          "type": "image",
          "url": "https://i04piccdn.sogoucdn.com/4df8bda2750d575f",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "fit",
          "action": {
            "type": "uri",
            "uri": "https://linecorp.com"
          }
        },
        {
          "type": "text",
          "text": "透過自由現金流量、EPS、負債比、ROE及ROA之相關比較，檢測公司是否存在虛增獲利、負債過高以至還不出來的風險",
          "size": "sm",
          "color": "#aaaaaa",
          "wrap": True
        },
        {
          "type": "separator",
          "margin": "xxl"
        },
        {
          "type": "box",
          "layout": "vertical",
          "margin": "xxl",
          "spacing": "sm",
          "contents": [
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "X",
                  "size": "sm",
                  "color": "#555555",
                  "flex": 0,
                  "margin": "none",
                  "align": "start"
                },
                {
                  "type": "text",
                  "text": "沒過",
                  "size": "sm",
                  "color": "#555555",
                  "flex": 0,
                  "align": "center",
                  "wrap": True,
                  "margin": "xs"
                },
                {
                  "type": "text",
                  "text": "自由現金流量近五年有三年>0",
                  "size": "sm",
                  "color": "#555555",
                  "flex": 0,
                  "wrap": True,
                  "align": "center",
                  "margin": "sm"
                },
                {
                  "type": "text",
                  "text": "(2/5)",
                  "size": "sm",
                  "color": "#555555",
                  "flex": 0,
                  "margin": "sm"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "Chewing Gum",
                  "size": "sm",
                  "color": "#555555",
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "$0.99",
                  "size": "sm",
                  "color": "#111111",
                  "align": "end"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "Bottled Water",
                  "size": "sm",
                  "color": "#555555",
                  "flex": 0
                },
                {
                  "type": "text",
                  "text": "$3.33",
                  "size": "sm",
                  "color": "#111111",
                  "align": "end"
                }
              ]
            },
            {
              "type": "separator",
              "margin": "xxl"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "margin": "xxl",
              "contents": [
                {
                  "type": "text",
                  "text": "ITEMS",
                  "size": "sm",
                  "color": "#555555"
                },
                {
                  "type": "text",
                  "text": "3",
                  "size": "sm",
                  "color": "#111111",
                  "align": "end"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "TOTAL",
                  "size": "sm",
                  "color": "#555555"
                },
                {
                  "type": "text",
                  "text": "$7.31",
                  "size": "sm",
                  "color": "#111111",
                  "align": "end"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "CASH",
                  "size": "sm",
                  "color": "#555555"
                },
                {
                  "type": "text",
                  "text": "$8.0",
                  "size": "sm",
                  "color": "#111111",
                  "align": "end"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "contents": [
                {
                  "type": "text",
                  "text": "CHANGE",
                  "size": "sm",
                  "color": "#555555"
                },
                {
                  "type": "text",
                  "text": "$0.69",
                  "size": "sm",
                  "color": "#111111",
                  "align": "end"
                }
              ]
            }
          ]
        },
        {
          "type": "separator",
          "margin": "xxl" 
        },
        {
          "type": "box",
          "layout": "horizontal",
          "margin": "md",
          "contents": [
            {
              "type": "text",
              "text": "PAYMENT ID",
              "size": "xs",
              "color": "#aaaaaa",
              "flex": 0
            },
            {
              "type": "text",
              "text": "#743289384279",
              "color": "#aaaaaa",
              "size": "xs",
              "align": "end"
            }
          ]
        }
      ],
      "margin": "none",
      "spacing": "none"
    },
    "styles": {
      "footer": {
        "separator": True
      }
    }
  }
  )