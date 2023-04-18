import requests
from bs4 import BeautifulSoup 
from linebot.models import *
import pandas as pd


def headlines():
    url = "https://news.cnyes.com/news/cat/headline"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    soup1 = soup.find_all("a",{"class":"_1Zdp"},limit = 10)
    base = "https://news.cnyes.com"
    title = []
    address = []
    for i in soup1:
        title.append(i.get("title"))
        address.append(base + i.get("href"))
    message = FlexSendMessage(
        alt_text = '頭條新聞',
        contents ={
        "type": "bubble",
        "hero": {
        "type": "image",
        "url": "https://campaign.cnyes.com/topics/anuesns/images/logo-dark.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "margin": "none"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "xs",
            "contents": [
            {
                "type": "text",
                "text": "財經新聞",
                "wrap": True,
                "weight": "bold",
                "gravity": "center",
                "size": "3xl"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[0]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[0])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[1]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[1])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[2]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[2])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[3]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[3])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[4]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[4])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[5]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[5])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[6]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[6])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[7]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[7])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[8]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[8])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[9]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[9])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                }
                ]
            }
            ],
            "margin": "none"
        }
        }
    )
    return message

def tw_stock():
    url = "https://news.cnyes.com/news/cat/tw_stock"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    soup1 = soup.find_all("a",{"class":"_1Zdp"},limit = 10)
    base = "https://news.cnyes.com"
    title = []
    address = []
    for i in soup1:
        title.append(i.get("title"))
        address.append(base + i.get("href"))
    message = FlexSendMessage(
        alt_text = '台股新聞',
        contents = {
        "type": "bubble",
        "hero": {
        "type": "image",
        "url": "https://campaign.cnyes.com/topics/anuesns/images/logo-dark.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "margin": "none"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "xs",
            "contents": [
            {
                "type": "text",
                "text": "財經新聞",
                "wrap": True,
                "weight": "bold",
                "gravity": "center",
                "size": "3xl"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[0]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[0])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[1]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[1])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[2]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[2])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[3]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[3])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[4]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[4])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[5]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[5])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[6]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[6])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[7]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[7])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[8]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[8])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[9]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[9])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                }
                ]
            }
            ],
            "margin": "none"
        }
        }
    )
    return message

def wd_stock():
    url = "https://news.cnyes.com/news/cat/wd_stock"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    soup1 = soup.find_all("a",{"class":"_1Zdp"},limit = 10)
    base = "https://news.cnyes.com"
    title = []
    address = []
    for i in soup1:
        title.append(i.get("title"))
        address.append(base + i.get("href"))
    message = FlexSendMessage(
        alt_text = '國際新聞',
        contents = {
        "type": "bubble",
        "hero": {
        "type": "image",
        "url": "https://campaign.cnyes.com/topics/anuesns/images/logo-dark.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "margin": "none"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "xs",
            "contents": [
            {
                "type": "text",
                "text": "財經新聞",
                "wrap": True,
                "weight": "bold",
                "gravity": "center",
                "size": "3xl"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[0]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[0])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[1]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[1])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[2]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[2])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[3]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[3])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[4]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[4])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[5]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[5])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[6]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[6])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[7]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[7])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[8]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[8])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "◆" + str(title[9]),
                        "color": "#0066FF",
                        "size": "lg",
                        "flex": 1,
                        "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": str(address[9])
                        },
                        "wrap": True
                    }
                    ],
                    "margin": "none"
                }
                ]
            }
            ],
            "margin": "none"
        }
        }
    )
    return message

def stock_new():
    buttons_template_message = TemplateSendMessage( 
    alt_text = "股票新聞",
    template=ButtonsTemplate( 
        thumbnail_image_url="https://cimg.cnyes.cool/prod/news/4413249/l/80014f698152aa983bc9e9984fe4510f.png",
        title="股市新聞", 
        text="請點選想查詢的新聞種類", 
        actions=[
            MessageAction( 
                label="頭條新聞 TOP10",
                text="頭條新聞"),
            MessageAction( 
                label="台股新聞 TOP10",
                text="台股新聞"),
            MessageAction( 
                label="國際新聞 TOP10",
                text="國際新聞"),    
            ] 
        ) 
    )
    return buttons_template_message

def weekly_news():
    url3 = requests.get('https://pocketmoney.tw/articles/')
    sp3 = BeautifulSoup(url3.text, "html.parser")
    get_img = sp3.find_all('img', class_="wp-post-image")[0]
    table3 = sp3.find_all('a',class_='post-thumb')[0]
    url = table3.get('href')
    img = get_img.get("src")
    flex_message = FlexSendMessage(
            alt_text="每周財經大事新聞",
            contents={
                "type": "bubble",
                "size": "giga",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": img,
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "1252:837",
                        "gravity": "center",
                        "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": url
                        }
                    }
                    ],
                    "paddingAll": "0px"
                }
                }
    )
    return flex_message