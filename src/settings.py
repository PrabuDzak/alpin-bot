import os, sys

class Settings: 

    def __init__(self):
        self.LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET', None)
        self.LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

        if self.LINE_CHANNEL_SECRET is None:
            print('Specify LINE_CHANNEL_SECRET as environment variable.')
            sys.exit(1)
        if self.LINE_CHANNEL_ACCESS_TOKEN is None:
            print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
            sys.exit(1)