from linebot.models import *
from linebot import LineBotApi,WebhookHandler
def sendUse(message):  #使用說明
    try:
        text1 ='''
        1.輸入股票加上股票「名稱」或「代號」 Ex:股票 台積電 ps:一定要空一格
        2.大戶籌碼加上股票「名稱」或「代號」 Ex:大戶籌碼 台積電 ps:一定要空一格
        3.基本面加上加上股票「名稱」或「代號」 Ex:基本面 台積電 ps:一定要空一格
        4.下面的選單直接點
        5.功能:頭條新聞、台股新聞、國際新聞、個股新聞、個股資訊、平均股利、歷年股利、最新法人買賣超、歷年法人買賣超
                外資買賣超、投信買賣超、自營商買賣超、三大法人買賣超、最新分鐘圖、日線圖、公司獲利能力、公司償債能力、公司經營能力
                
               '''
        message = TextSendMessage(
            text = text1
        )
        return message
    except:
        return "發生錯誤"
