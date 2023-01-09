import requests
from bs4 import BeautifulSoup
from linebot.models import *

def getnewbook():
    url='https://www.books.com.tw/web/sys_newtopb/books/02/?loc=P_0002_003'
    html=requests.get(url)
    sp=BeautifulSoup(html.text,'lxml')
    m=sp.select('.mod_a')[0].select('.item')
    # rank = 0
    title_list = []
    address = []
    for i in m:
        # rank += 1
        title = i.find_all('h4')[0].text
        if len(title) > 20: title = title[0:20]
        title_list.append(title)
        address.append(i.select('a')[0]['href'])
        
    message = FlexSendMessage(
    alt_text = '新書推薦',
    contents ={
        "type": "bubble",
        "hero": {
        "type": "image",
        "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/G/logo/books_logo.jpg&v=624133c3k&w=250&h=250",
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
                "text": "新書推薦",
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
                        "text": "◆" + str(title_list[0]),
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
                        "text": "◆" + str(title_list[1]),
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
                        "text": "◆" + str(title_list[2]),
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
                        "text": "◆" + str(title_list[3]),
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
                        "text": "◆" + str(title_list[4]),
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
                        "text": "◆" + str(title_list[5]),
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
                        "text": "◆" + str(title_list[6]),
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
                        "text": "◆" + str(title_list[7]),
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
                        "text": "◆" + str(title_list[8]),
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
                        "text": "◆" + str(title_list[9]),
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

        

def getfamousbook():
    url='https://www.books.com.tw/web/sys_saletopb/books/02/?loc=P_0002_003'
    html=requests.get(url)
    # html.encoding='utf-8'
    sp=BeautifulSoup(html.text,'lxml')
    m=sp.select('.mod_a')[0].select('.item')
    title_list = []
    address = []
    for i in m:
        
        title = i.find_all('h4')[0].text
        if len(title) > 20: title = title[0:20]
        title_list.append(title)
        address.append(i.select('a')[0]['href'])
    
    
    
    message = FlexSendMessage(
    alt_text = '暢銷書推薦',
    contents ={
        "type": "bubble",
        "hero": {
        "type": "image",
        "url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/G/logo/books_logo.jpg&v=624133c3k&w=250&h=250",
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
                "text": "暢銷書推薦",
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
                        "text": "◆" + str(title_list[0]),
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
                        "text": "◆" + str(title_list[1]),
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
                        "text": "◆" + str(title_list[2]),
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
                        "text": "◆" + str(title_list[3]),
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
                        "text": "◆" + str(title_list[4]),
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
                        "text": "◆" + str(title_list[5]),
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
                        "text": "◆" + str(title_list[6]),
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
                        "text": "◆" + str(title_list[7]),
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
                        "text": "◆" + str(title_list[8]),
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
                        "text": "◆" + str(title_list[9]),
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
