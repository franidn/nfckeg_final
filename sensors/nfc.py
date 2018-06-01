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
    def detect_target(self):

            (status,TagType) = self.nfcobject.MFRC522_Request(self.nfcobject.PICC_REQIDL)
            if status == self.nfcobject.MI_OK:
                self.estat = "Card detected"

            else:
                self.estat = "No card"

            print self.estat
            return self.estat

    def get_uid(self):
            (status,self.uid) = self.nfcobject.MFRC522_Anticoll()
            if status == self.nfcobject.MI_OK:
                 print "Card read UID: %s,%s,%s,%s" % (self.uid[0], self.uid[1], self.uid[2], self.uid[3])

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
