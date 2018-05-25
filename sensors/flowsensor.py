from .main import sensor

class flowmeter(sensor):
    """ Sensor de flux """
    def __init__(self, name):
        super(flowmeter, self).__init__(name)

    def setup():

        #Defenim pin BCM17 per conectar el sensor de flux
        FLOW_SENSOR_PIN = 17
        #Diem a la raspberry que ens referirem als pins com BCM
        GPIO.setmode(GPIO.BCM)
        #Definim en quin pin, quina funcio fara el pin i posem en down la resistencia interna del pin
        GPIO.setup(FLOW_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        #Cridem la funcio countPulse quan detectem una senyal al pin espentan
        GPIO.add_event_detect(FLOW_SENSOR_PIN, GPIO.RISING, callback=self.get_data)
        #Inicialitzem una varialble global per contar voltes del sensor de flux
        self.count = 0

    def get_data():


    def get_cumulative():


    def reset_cumulative():
