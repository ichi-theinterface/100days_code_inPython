from msilib.schema import Class


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = " "
TWITTER_EMAIL = "ichiro.sf.289@gmail.com"
TWITTER_PASSWORD = "replace before run it or upload it to github"

class InternetSpeedTwitterBot:
    def __init__(self, driver, up, down):
        self.browser_driver = driver
        self.up_speed = up
        self.down_speed = down
    
    def get_internet_speed(self):
        pass
    
    def tweet_at_provider(self):
        pass


MyBot = InternetSpeedTwitterBot()
