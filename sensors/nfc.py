from main import sensor
import RPi.GPIO as GPIO
import MFRC522
import time
import sys



class rfid(sensor):
    """ Lector rfid """
    def __init__(self, name):
        super(rfid, self).__init__(name)

    def setup(self):
        self.nfcobject = MFRC522.MFRC522()
        self.estat = "a"
        self.dectect_card = "no oks"
    def detect_target(self):

            (status,TagType) = self.nfcobject.MFRC522_Request(self.nfcobject.PICC_REQIDL)
            if status == self.nfcobject.MI_OK:
                self.dectect_card = "OK"
                print "Card detected"

    def get_uid(self):
            (status,self.uid) = self.nfcobject.MFRC522_Anticoll()
            if status == self.nfcobject.MI_OK:
                print "Card read UID: %s,%s,%s,%s" % (self.uid[0], self.uid[1], self.uid[2], self.uid[3])
                self.estat = "Card detected"

            elif status == self.nfcobject.MI_ERR:
                self.estat = "No card"

if __name__ == "__main__":
    nfc = rfid("lector")
    nfc.setup()
    while True:
        try:
            time.sleep(4)
            nfc.detect_target()

            if nfc.estat == 'Card detected':
                nfc.get_uid()

        except KeyboardInterrupt:
            print '\ncaught keyboard interrupt!, bye'
            GPIO.cleanup()
            sys.exit()
