from linebot.models import *
from linebot import LineBotApi,WebhookHandler
def sendUse(message):  #使用說明
    try:
        text1 ='''
1. 「房間預約」及「取消訂房」可預訂及取消訂房。每個 LINE 帳號只能進行一個預約記錄。
2. 「關於我們」對旅館做簡單介紹及旅館圖片。
3. 「位置資料」列出旅館地址，並會顯示地圖。
4. 「聯絡我們」可直接撥打電話與我們聯繫。
               '''
        message = TextSendMessage(
            text = text1
        )
        return message
    except:
        return "發生錯誤"
