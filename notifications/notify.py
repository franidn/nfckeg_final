import telepot
from main import notification

class telegram(notification):
    """ Sensor de flux """
    def __init__(self):
        super(telegram, self).__init__()
# Dades per connectar-se al bot
    def setup(self):
        self.token = '584119079:AAGGf4g3iDFLlhbfp-Ii9e9SnDKOTRtU-_A'
        self.chatId = -217126603
        self.message = " "
# Funcio que envia missatge al bot definit anteriorment
    def sendMessage(self):
        bot = telepot.Bot(self.token)
        bot.sendMessage(self.chatId, self.message)

if __name__ == "__main__":
    s = telegram()
    s.setup()
    for x in range(1,5):
        s.sendMessage()
