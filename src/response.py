import requests, json

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, SourceRoom, SourceGroup, SourceUser
from settings import Settings

class BaseResponse:

    line_bot_api = LineBotApi(Settings().LINE_CHANNEL_ACCESS_TOKEN)

    def __init__(self, event):
        self.reply_token = event.reply_token
        self.source = event.source

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
        url = "https://i.redditmedia.com/ldPvM97iIq9pM7cIn58ux3N2Mn67lasD5fiXIEqn9KY.jpg?s=74fef387f903f5bed5d4087e7518e10f"
        pre = "https://i.redditmedia.com/ldPvM97iIq9pM7cIn58ux3N2Mn67lasD5fiXIEqn9KY.jpg?fit=crop&crop=faces%2Centropy&arh=2&w=216&s=fb649af2603f08ec039d2b455548c176"
        BaseResponse.line_bot_api.reply_message(
            self.reply_token, 
            ImageSendMessage(url,pre)
        )


class AsuResponse(BaseResponse):

    def get_link(self):
        # STUB METHOD
        return "http://i.imgur.com/uk8cuq2.png"

    def reply(self):
        self.send_image(url=self.get_link())

class KoranResponse(BaseResponse):

    def reply(self):
        self.send_text("koran_lampu_hijau.png")

class IstighfarResponse(BaseResponse):

    def reply(self):
        self.send_text("Astaghfirullah")

class MetuResponse(BaseResponse):
    
    def reply(self):
        if(isinstance(self.source, SourceGroup)):
            self.send_text("good bye my fren")
            BaseResponse.line_bot_api.leave_group(self.source.group_id)
        elif (isinstance(self.source, SourceRoom)):
            self.send_text("good bye my fren")
            BaseResponse.line_bot_api.leave_room(self.source.room_id)
        else:
            self.send_text("metu ndiass mu")

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