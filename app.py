from flask import Flask, request, abort , g
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import re
import pyodbc




#function 功能
from blog import *
from news import *
from stock import *
from use import *
from stock_base import *
from stock_select import *
from stock_list import *
from new_famous_book import *


app = Flask(__name__)

line_bot_api = LineBotApi("")
handler = WebhookHandler("")
@app.before_request
def before_request():
    connection_string = "Driver=SQL Server;Server=35.229.143.23;Database={0};Trusted_Connection=Yes;Database={0};" 
    #g.cnxn = pyodbc.connect(connection_string.format("linebot"), autocommit=True)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):
    message = text = event.message.text
    user_id = event.source.user_id
    print("Message from userId: " + event.source.user_id)
    if "個股資訊" in message:
        stock_n = stock_id(message[5:])
        cont = continue_after(message[5:])
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(stock_n),cont])
    elif re.match("個股新聞",message):
        flex_message = one_new(message[5:])
        cont = continue_after(message[5:])
        line_bot_api.reply_message(event.reply_token,[flex_message,cont])
    elif re.match("新聞快報",message):
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
        dividend_one = average_dividend(message[5:])
        cont = continue_after(message[5:])
        line_bot_api.reply_message(event.reply_token,[dividend_one,cont])
    elif re.match("歷年股利",message):
        dividend_year = year_dividend(message[5:])
        cont = continue_after(message[5:])
        line_bot_api.reply_message(event.reply_token,[dividend_year,cont])
    elif "最新法人買賣超 " in message:
        inv = investors(message[8:])
        cont = continue_after_BS(message[8:])
        line_bot_api.reply_message(event.reply_token,[inv,cont])
    elif "歷年法人買賣超 " in message:
        t_d = total_data(message[8:])
        cont = continue_after_BS(message[8:])
        line_bot_api.reply_message(event.reply_token,[t_d,cont])
    elif "外資買賣超 " in message:
        t_m = total_major(message[6:])
        f_i = foreign_inv(message[6:],t_m)
        cont = continue_after_BS(message[6:])
        line_bot_api.reply_message(event.reply_token,[f_i,cont])
    elif "投信買賣超 " in message:
        t_m = total_major(message[6:])
        c_i = credit_inv(message[6:],t_m)
        cont = continue_after_BS(message[6:])
        line_bot_api.reply_message(event.reply_token,[c_i,cont])
    elif "自營商買賣超 " in message:
        t_m = total_major(message[7:])
        s_i = self_employed_inv(message[7:],t_m)
        cont = continue_after_BS(message[7:])
        line_bot_api.reply_message(event.reply_token,[s_i,cont])      
    elif "三大法人買賣超 " in message:
        t_m = total_major(message[8:])
        m_i = major_inv(message[8:],t_m)
        cont = continue_after_BS(message[8:])
        line_bot_api.reply_message(event.reply_token,[m_i,cont])
    elif "最新分鐘圖 " in message:
        m = min_close(message[6:])
        cont = continue_after(message[6:])
        line_bot_api.reply_message(event.reply_token,[m,cont])
    elif "日線圖 " in message:
        d = stock_day(message[4:])
        cont = continue_after(message[4:])
        line_bot_api.reply_message(event.reply_token,[d,cont])   
    elif "獲利能力 " in message:
        base = base_3(message)
        cont = continue_after_Basic(message[5:])
        line_bot_api.reply_message(event.reply_token,[base,cont])
    elif "償債能力 " in message:
        base = base_3(message)
        cont = continue_after_Basic(message[5:])
        line_bot_api.reply_message(event.reply_token,[base,cont]) 
    elif "經營能力 " in message:
        base = base_3(message)
        cont = continue_after_Basic(message[5:])
        line_bot_api.reply_message(event.reply_token,[base,cont])
    elif "地雷檢測 " in message:
        check = select_1(message[4:])
        cont = continue_after_Basic(message[5:])
        line_bot_api.reply_message(event.reply_token,check)
    elif re.match("查詢關注",message):
        find = find_list(user_id)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=find))
    elif "取消關注 " in message:
        delete = stock_database_del(message[5:], user_id)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=delete))
    elif "關注" in message:
        add = stock_database_add(message[3:], user_id)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=add))   
    elif "使用說明" in message:
        mes = sendUse(message)
        line_bot_api.reply_message(event.reply_token,mes)
    elif re.match("新書推薦", message):
        # line_bot_api.reply_message(event.reply_token, TextSendMessage("將給您最新理財新書......"))
        flex_message = getnewbook()
        line_bot_api.reply_message(event.reply_token, flex_message)  
    elif re.match("暢銷書推薦", message):
        # line_bot_api.reply_message(event.reply_token, TextSendMessage("將給您最新理財暢銷書......"))
        flex_message = getfamousbook()
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match("每周財經",message):
        mes = weekly_news()
        line_bot_api.reply_message(event.reply_token,mes)
    elif re.match("退出",message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage("先休息囉!!!"))
    
  
    #列表
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
                            title = message + "線圖資訊",
                            text = "請點選想查詢的股票資訊",
                            actions = [
                                MessageAction(
                                    label = message[3:] + "最新分鐘圖",
                                    text = "最新分鐘圖" + message[2:]),
                                MessageAction(
                                    label = message[3:] + "日線圖",
                                    text = "日線圖" + message[2:])
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
                    ),
                    CarouselColumn(
                            thumbnail_image_url="https://s.yimg.com/ny/api/res/1.2/sMdeik0X7732bNVG_MeBsQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNw--/https://s.yimg.com/os/creatr-uploaded-images/2019-09/d3e90a60-d788-11e9-bfb9-33efbef2955b",
                            title = message + "籌碼基本面",
                            text = "請點選想查詢的股票資訊",
                            actions = [
                                MessageAction(
                                    label = message[3:] + "大戶籌碼",
                                    text = "大戶籌碼" + message[2:]),
                                MessageAction(
                                    label = message[3:] + "基本面",
                                    text = "基本面" + message[2:])
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
    elif "基本面" in message:
        st = message[3:]
        flex_message = TextSendMessage(text="請選擇要顯示的基本面資訊",
                                    quick_reply=QuickReply(items=[
                                        QuickReplyButton(action=MessageAction(label="獲利能力",text="獲利能力" + st)),
                                        QuickReplyButton(action=MessageAction(label="償債能力",text="償債能力" + st)),
                                        QuickReplyButton(action=MessageAction(label="經營能力",text="經營能力" + st)),
                                      
                                    ])
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



