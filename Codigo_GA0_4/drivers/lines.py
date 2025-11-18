"""
lines.py
Actualiza su estado en función de los 2 sensores infrarrojos
State tiene varios estados:
    0 - STOP:          se ha detectado negro en los 2 sensores, así que se para el coche
    1 - RIHGT:         solo hay negro en el sensor derecho, así que hay que girar a la derecha
    2 - LEFT:          solo hay negro en el sensor izquierdo, así que hay que girar a la izquierda
    3 - STRAIGHT:      no se detecta negro, así que hay que continuar recto
"""
from time import sleep
from drivers.clase_infrarrojo import Infrarrojos

class Lines():
    def __init__(self, channel_1=0, threshold_1=0.9, 
                    channel_2=1, threshold_2=0.9):

        self.sensor_1 = Infrarrojos(channel_1, threshold_1)
        self.sensor_2 = Infrarrojos(channel_2, threshold_2)
        self.state = "STOP"

    def update_lines(self):
        self.sensor_1.check_black()
        self.sensor_2.check_black()
        left = self.sensor_1.state
        right = self.sensor_2.state

        if not left and not right:
            self.state = "STRAIGHT"
        elif left and not right:
            self.state = "LEFT"
        elif not left and right:
            self.state = "RIGHT"
        else:
            self.state = "END"   # caso último, y en caso de error salta a parada

            


