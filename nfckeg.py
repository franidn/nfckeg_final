"""
produced by: FAC0
"""

import sensors
#import notifications
import time, sys

class nfckeg(object):
    """ La tasca serveix per poder controlar un sortidor de cervesa mitjansant targetes nfc"""
    def __init__(self):
        super(nfckeg, self).__init__()
        self.sensor_flux = sensors.flowmeter("nom_sensor_flux")
        self.lector_nfc = sensors.rfid("nom_sensor_nfc")
        #self.notificacio = notifications.telegram("nom_notificacio_telegram")


    def setup(self):
        self.uid = None
        self.sensor_flux.setup()
        self.lector_nfc.setup()

    def main_loop(self):
        while True:
            self.lector_nfc.detect_target()
            time.sleep(2)
            if self.lector_nfc.estat == "Card detected":
                """
                Relay on
                """
                print "pene"
                self.sensor_flux.Relay = "Relay on"
                print self.sensor_flux.Relay
                while self.sensor_flux.Relay == "Relay on":
                    self.lector_nfc.detect_target()
                    time.sleep(1)
                    if self.lector_nfc.estat != "Card detected":
                        print "vagina"
                        """
                        Relay off
                        """
                        self.sensor_flux.Relay = "Relay off"
                        print self.sensor_flux.Relay
                        self.sensor_flux.get_data()

if __name__ == "__main__":
    n = nfckeg()
    n.setup()
    n.main_loop()
