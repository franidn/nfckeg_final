from main import sensor
import RPi.GPIO as GPIO
import time, sys

class flowmeter(sensor):
    """ Sensor de flux """
    def __init__(self, name):
        super(flowmeter, self).__init__(name)

    def setup(self):
        #Defenim pin BCM17 per conectar el sensor de flux
        FLOW_SENSOR_PIN = 17
        #Diem a la raspberry que ens referirem als pins com BCM
        GPIO.setmode(GPIO.BCM)
        #Definim en quin pin, quina funcio fara el pin i posem en down la resistencia interna del pin
        GPIO.setup(FLOW_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        #Cridem la funcio countPulse quan detectem una senyal al pin espentan
        GPIO.add_event_detect(FLOW_SENSOR_PIN, GPIO.RISING, callback=self.countPulse)
        #Inicialitzem una varialble global per contar voltes del sensor de flux
        self.count_cumulative = 0
        self.count_no_cumulative = 0

    def countPulse(self, channel):
            self.count_cumulative = self.count_cumulative + 1
            self.count_no_cumulative = self.count_no_cumulative + 1

    def get_data(self):
        if self.count_no_cumulative == 0:
            self.actual_liters = self.count_no_cumulative/float(400)
            print self.actual_liters
        else:
            self.count_no_cumulative = 0

    def get_cumulative(self):
        self.acumulate_liters = self.count_cumulative/float(400)
        print self.acumulate_liters

    def reset_cumulative():
        self.acumulate_liters = 0
        self.count_cumulative = 0

if __name__ == "__main__":
    s = flowmeter('prova')
    s.setup()
    while True:
        try:
            time.sleep(1)
            s.get_cumulative()
        except KeyboardInterrupt:
            print '\ncaught keyboard interrupt!, bye'
            GPIO.cleanup()
            sys.exit()
