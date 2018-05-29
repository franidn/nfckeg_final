"""
Classe pare de tots els tipus de sensors
"""

class sensor(object):

    """ Busquem que estigui definit al init"""
    def __init__(self, name):
        super(sensor, self).__init__()
        self.name = name
