import os
import sys
from argparse import ArgumentParser

from flask import Flask, abort, request
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, JoinEvent

from settings import Settings
from response import *
import helper as help

app = Flask(__name__)

handler = WebhookHandler(Settings().LINE_CHANNEL_SECRET)

@app.route("/")
def index():
    return "alpin-bot"

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
def message_text(event):
    msg = event.message.text
    respond = NullResponse(event=event)

    if (msg.lower() == "pin"):
        respond.send_text("yuuhuu hadir")
        return

    if ("pin" in msg):
        command = help.extract_command(msg)

        if (command == "kucing"):
            respond = KucingResponse(event)
        elif (command == "koran"):
            respond = KoranResponse(event)
        elif (command == "istighfar"):
            respond = IstighfarResponse(event)
        elif (command == "asu") or (command == "anjing"):
            respond = AsuResponse(event)
        elif (command == "metu"):
            respond = MetuResponse(event)

        respond.reply()

    else:
        msg = msg.lower()
        if (msg == "tes"):
            respond.send_text("bisa tol")

@handler.add(JoinEvent)
def join_event(event):
    NullResponse(event).send_text("Hello fren")

def main():
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--host <host>] [--port <port>] [--help]'
    )
    # arg_parser.add_argument('-h', '--host', default='0.0.0.0', help='host')
    arg_parser.add_argument('-p', '--port', default=int(os.environ.get('PORT', 5000)), help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(host="0.0.0.0", debug=options.debug, port=options.port)
    