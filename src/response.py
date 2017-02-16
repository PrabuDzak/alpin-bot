import requests, json

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from settings import Settings

class BaseResponse:

    line_bot_api = LineBotApi(Settings().LINE_CHANNEL_ACCESS_TOKEN)

    def __init__(self, event):
        self.reply_token = event.reply_token

    def reply(self):
        return 

    def send_text(self, str):
        BaseResponse.line_bot_api.reply_message(
            self.reply_token,
            TextSendMessage(text=str)
        )
        print(str)

    def send_image(self, url):
        BaseResponse.line_bot_api.reply_message(
            self.reply_token,
            ImageSendMessage(original_content_url=url, preview_image_url=url)
        )

    # def send_video(self, url):
    #     return

    def send_sticker(self, pkg, stick):
        print (pkg + " " + stick)


class KucingResponse(BaseResponse):

    def get_link(self):
        url = "http://random.cat/meow"
        resp = requests.get(url=url).json()
        return resp["file"]

    def reply(self):
        self.send_image(self.get_link())


class AsuResponse(BaseResponse):

    def get_link(self):
        # STUB METHOD
        return "http://i.imgur.com/uk8cuq2.png"

    def reply(self):
        self.send_image(url=self.get_link())

class KoranResponse(BaseResponse):

    def reply(self):
        self.send_image("koran")

class IstighfarResponse(BaseResponse):

    def reply(self):
        self.send_text("Astaghfirullah")

class NullResponse(BaseResponse):
    pass


#### koran
#headline koran lampu hijau
#### istighfar
#"Astaghfirullah"
#### jadwal kuliah
#jadwal kuliah hari itu dan ruangan
#### jancok
#kata kata mutiara / peribahasa
#### kucing
#http://thecatapi.com/api/images/get?size=med
# asu