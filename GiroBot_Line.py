from flask import Flask, request, abort

from linebot import (
     LineBotApi, WebhookHandler
)
from linebot.exceptions import (
   InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('WYLiL6rPwY0YQDlupODwf/8FnTgZFplWBnHznY3X/SXVyXZ0qYgqkuTGtsfaLcuEvTVOW0Fxyal5rwbEOWbRYaNl95coWOPEd3aSLn4iBHOSRhHmPDh+IEef4I1WUDflaNYDO5vkQFcn6Q17rlZeywdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6d8b4f4505eda4797feeeec6909d243c')



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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

try:
    line_bot_api.push_message('<to>', TextSendMessage(text='This is just a test'))
except LineBotApiError as e:
    # error handle

if __name__ == "_main_":
    app.run()