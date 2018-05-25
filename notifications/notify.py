from main import notification
import telebot

class telegram(notification):

    def __init__(self):
        super(telegram, self).__init__()

    def setup(self, message):
        token = '584119079:AAGGf4g3iDFLlhbfp-Ii9e9SnDKOTRtU-_A'
        self.chatid = -217126603
        self.text = message
        self.tb = telebot.TeleBot(token)

    def send_message(self):
        self.tb.send_message(self.chatid, self.text)


if __name__ == "__main__":
    n=telegram()
    n.setup("El paco es un esser suprem")
    n.send_message()
