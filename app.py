from flask import Flask, request, abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import re


#funtion 功能
from blog import *
from news import *
from stock import *
from use import *


app = Flask(__name__)

line_bot_api = LineBotApi("uEUzpQi5I1Ch73qIaA3N31ptAWSG1sUQBDV5Yj4BLLBlRfCE3x62ZdYjAP54MJbvn5rLNsp5WTrb5zhTwkhO58FhRJWiEoc87vE/xmQY1qVR1Qqh7yh1823IHPwwehRXMg3fkoFwC9U6rCaB/APMcwdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("7e256e9ecd70a48250de5cd57929a41b")

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):
    message = text = event.message.text
    if "個股資訊" in message:
        stock_n = stock_id(message[5:])
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(stock_n)])
    elif re.match("個股新聞",message):
        flex_message = one_new(message[5:])
        # cont = con_af(message[5:])
        line_bot_api.reply_message(event.reply_token,[flex_message])
    elif re.match("新聞",message):
        flex_message = stock_new()
        line_bot_api.reply_message(event.reply_token,flex_message)
    elif re.match("頭條新聞",message):
        flex_message = headlines()
        line_bot_api.reply_message(event.reply_token,flex_message)
    elif re.match("台股新聞",message):
        flex_message = tw_stock()
        line_bot_api.reply_message(event.reply_token,flex_message)
    elif re.match("國際新聞",message):
        flex_message = wd_stock()
        line_bot_api.reply_message(event.reply_token,flex_message)
    elif re.match("平均股利",message):
        # mes = contuin_divided(message[5:])
        dividend_one = average_dividend(message[5:])
        line_bot_api.reply_message(event.reply_token,dividend_one)
    elif re.match("歷年股利",message):
        # mes = contuin_divided(message[5:])
        dividend_year = year_dividend(message[5:])
        line_bot_api.reply_message(event.reply_token,dividend_year)
    elif "股票" in message:
        button_template_message = TemplateSendMessage(
        alt_text= "股票資訊",
       template =CarouselTemplate(
            columns=[
                    CarouselColumn(
                            thumbnail_image_url="https://s.yimg.com/ny/api/res/1.2/sMdeik0X7732bNVG_MeBsQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNw--/https://s.yimg.com/os/creatr-uploaded-images/2019-09/d3e90a60-d788-11e9-bfb9-33efbef2955b",
                            title = message + "股票資訊",
                            text = "請點選想查詢的股票資訊",
                            actions = [
                                MessageAction(
                                    label = message[3:] + "個股資訊",
                                    text = "個股資訊" + message[2:]),
                                MessageAction(
                                    label = message[3:] + "個股新聞",
                                    text = "個股新聞" + message[2:])
                            ]
                    ),
                    CarouselColumn(
                            thumbnail_image_url="https://s.yimg.com/ny/api/res/1.2/sMdeik0X7732bNVG_MeBsQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNw--/https://s.yimg.com/os/creatr-uploaded-images/2019-09/d3e90a60-d788-11e9-bfb9-33efbef2955b",
                            title = message + "股票資訊",
                            text = "請點選想查詢的股票資訊",
                            actions = [
                                MessageAction(
                                    label = message[3:] + "最新分鐘圖",
                                    text = "最新分鐘圖" + message[3:]),
                                MessageAction(
                                    label = message[3:] + "日線圖",
                                    text = "日線圖" + message[3:])
                            ]
                    ),
                    CarouselColumn(
                            thumbnail_image_url="https://s.yimg.com/ny/api/res/1.2/sMdeik0X7732bNVG_MeBsQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNw--/https://s.yimg.com/os/creatr-uploaded-images/2019-09/d3e90a60-d788-11e9-bfb9-33efbef2955b",
                            title = message + "股利資訊",
                            text = "請點選想查詢的股票資訊",
                            actions = [
                                MessageAction(
                                    label = message[3:] + "平均股利",
                                    text = "平均股利" + message[2:]),
                                MessageAction(
                                    label = message[3:] + "歷年股利",
                                    text = "歷年股利" + message[2:])
                            ]
                    )            
                ]   
            )
        )
        line_bot_api.reply_message(event.reply_token,button_template_message)
    # else:
    #     line_bot_api.reply_message(event.reply_token,TemplateSendMessage(message))
 
    elif "大戶籌碼" in message:
        st = message[4:]
        flex_message = TextSendMessage(text="請選擇要顯示的買賣超資訊",
                                    quick_reply=QuickReply(items=[
                                        QuickReplyButton(action=MessageAction(label="最新法人",text="最新法人買賣超" + st)),
                                        QuickReplyButton(action=MessageAction(label="歷年法人",text="歷年法人買賣超" + st)),
                                        QuickReplyButton(action=MessageAction(label="外資",text="外資買賣超" + st)),
                                        QuickReplyButton(action=MessageAction(label="投信",text="投信買賣超" + st)),
                                        QuickReplyButton(action=MessageAction(label="自營商",text="自營商買賣超" + st)),
                                        QuickReplyButton(action=MessageAction(label="三大法人",text="三大法人買賣超" + st))
                                    ])
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif "最新法人買賣超 " in message:
        inv = investors(message[8:])
        # cont = continue_after_BS(message[8:])
        line_bot_api.reply_message(event.reply_token,[inv])
    elif "歷年法人買賣超 " in message:
        t_d = total_data(message[8:])
        # cont = continue_after_BS(message[8:])
        line_bot_api.reply_message(event.reply_token,[t_d])
    elif "外資買賣超 " in message:
        t_m = total_major(message[6:])
        f_i = foreign_inv(message[6:],t_m)
        # cont = continue_after_BS(message[6:])
        line_bot_api.reply_message(event.reply_token,[f_i])
    elif "投信買賣超 " in message:
        t_m = total_major(message[6:])
        c_i = credit_inv(message[6:],t_m)
        # cont = continue_after_BS(message[6:])
        line_bot_api.reply_message(event.reply_token,[c_i])
    elif "自營商買賣超 " in message:
        t_m = total_major(message[7:])
        s_i = self_employed_inv(message[7:],t_m)
        # cont = continue_after_BS(message[7:])
        line_bot_api.reply_message(event.reply_token,[s_i])      
    elif "三大法人買賣超 " in message:
        t_m = total_major(message[8:])
        m_i = major_inv(message[8:],t_m)
        # cont = continue_after_BS(message[8:])
        line_bot_api.reply_message(event.reply_token,[m_i])
        
    

    elif "使用說明" in message:
        mes = sendUse(message)
        line_bot_api.reply_message(event.reply_token,mes)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



