import os
import sys
from argparse import ArgumentParser

from flask import Flask, abort, request
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

from .settings import Settings

from .models.response import KucingResponse 

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
    command = extract_command(event.message.text)

def extract_command(str):
    
    return str
        


def main():
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--host <host>] [--port <port>] [--help]'
    )
    arg_parser.add_argument('-h', '--host', default='0.0.0.0', help='host')
    arg_parser.add_argument('-p', '--port', default=int(os.environ.get('PORT', 5000)), help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(host=options.host, debug=options.debug, port=options.port)
