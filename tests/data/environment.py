import os


class Environment:
    STAGE = 'stage'
    PROD = 'prod'

    URLS = {
        STAGE: 'https://stage.my.rek.la/auth/',
        PROD: 'https://rek.la/'
    }

    def __init__(self):
        try:
            self.env = os.getenv('ENV')
        except KeyError:
            self.env = self.PROD

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")


host = Environment()
