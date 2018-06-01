"""
produced by: FAC0
"""

import sensors
import notification

class nfckeg(object):
    """ La tasca serveix per poder controlar un sortidor de cervesa mitjançant targetes nfc"""
    def __init__(self):
        super(nfckeg, self).__init__()
        self.sensor_flux = sensors.flowmeter("nom_sensor_flux")
        self.lector_nfc = sensors.rfid("nom_sensor_nfc")
        self.notificacio = notifications.telegram("nom_notificacio_telegram")


    def setup(self):
        self.uid = None
        self.sensor_flux.setup()
        self.lector_nfc.setup()

    def main_loop(self):
