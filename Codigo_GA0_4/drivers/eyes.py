"""
eyes.py
Actualiza su estado en función de los 2 sensores ultrasonidos
State solo tiene 2 estados:
    0: Ningún sensor detecta un objeto cerca
    1: Al menos un sensor detecta un objeto cerca
"""
from gpiozero import Buzzer
from drivers.clase_ultrasonidos import Ultrasonidos

class Eyes():
    def __init__(self, echo_1=16, trigger_1=21, threshold_distance_1=0.1,
                       echo_2=17, trigger_2=19, threshold_distance_2=0.1,
                       buzzer_pin=27):

        self.sensor_1 = Ultrasonidos(echo_1, trigger_1, threshold_distance_1)
        self.sensor_2 = Ultrasonidos(echo_2, trigger_2, threshold_distance_2)

        self.buzzer = Buzzer(buzzer_pin)

        self.state = 0

    def update_eyes(self):
        self.sensor_1.check_distance()
        self.sensor_2.check_distance()

        v1 = self.sensor_1.state
        v2 = self.sensor_2.state

        self.state = 1 if v1 or v2 else 0

        if self.state == 1:
            self.buzzer.on()
        else:
            self.buzzer.off()


