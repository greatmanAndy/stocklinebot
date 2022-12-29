from linebot.models import *

def flex():
    message = FlexSendMessage(
        alt_text= "翻譯",
        contents= {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://translate.google.com.tw/?hl=zh-TW"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    },
    "contents": [
      {
        "type": "text",
        "text": "翻譯網站",
        "size": "xxl",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"
              },
              {
                "type": "text",
                "text": "$10.5",
                "weight": "bold",
                "margin": "sm",
                "flex": 0
              },
              {
                "type": "text",
                "text": "400kcl",
                "size": "sm",
                "align": "end",
                "color": "#aaaaaa"
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"
              },
              {
                "type": "text",
                "text": "$15.5",
                "weight": "bold",
                "margin": "sm",
                "flex": 0
              },
              {
                "type": "text",
                "text": "550kcl",
                "size": "sm",
                "align": "end",
                "color": "#aaaaaa"
              }
            ]
          }
        ]
      },
      {
        "type": "text",
        "text": "Sauce, Onions, Pickles, Lettuce & Cheese",
        "wrap": True,
        "color": "#aaaaaa",
        "size": "xxs"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "color": "#905c44",
        "margin": "xxl",
        "action": {
          "type": "uri",
          "label": "馬上前往",
          "uri": "https://translate.google.com.tw/?hl=zh-TW"
        }
      }
    ]
  }
}
    )
    return message