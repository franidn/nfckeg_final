"""
produced by: FAC0
"""

import sensors
import notifications
import time, sys

class nfckeg(object):
    """ La tasca serveix per poder controlar un sortidor de cervesa mitjansant targetes nfc"""
    def __init__(self):
        super(nfckeg, self).__init__()
        self.sensor_flux = sensors.flowmeter("nom_sensor_flux")
        self.lector_nfc = sensors.rfid("nom_sensor_nfc")
        self.notificacio = notifications.telegram()


    def setup(self):
        self.uid = None
        self.sensor_flux.setup()
        self.lector_nfc.setup()

    def main_loop(self):
        while True:
            self.lector_nfc.detect_target()
            time.sleep(2)
            if self.lector_nfc.dectect_card == "OK":
                """
                Relay on
                """
                self.sensor_flux.Relay = "Relay on"
                print self.sensor_flux.Relay
                while self.sensor_flux.Relay == "Relay on":

                    time.sleep(3)
                    self.lector_nfc.get_uid()

                    if self.lector_nfc.estat != "Card detected":
                        """
                        Relay off
                        """
                        self.sensor_flux.Relay = "Relay off"
                        self.lector_nfc.dectect_card = "NO OK"
                        print self.sensor_flux.Relay
                        self.sensor_flux.get_cumulative()
                        self.notificacio.setup("self.sensor_flux.acumulate_liters")

if __name__ == "__main__":
    n = nfckeg()
    n.setup()
    n.main_loop()
