"""
clase_ultrasonidos.py
Tomamos la clase DistanceSensor y añadimos un método check_distance que actualiza el 
estado del sensor a 0 o 1 en función de si se supera un umbral de distancia.
State solo tiene 2 estados:
    0: No hay objeto cerca
    1: Sí hay objeto cerca
"""

from gpiozero import DistanceSensor


class Ultrasonidos():
    """
    Toma la clase DistanceSensor y añade un método check_distance que actualiza el 
    estado del sensor a 0 o 1 en función de si se supera un umbral de distancia.
    State solo tiene 2 estados:
        0: No hay objeto cerca
        1: Sí hay objeto cerca
    """
    def __init__(self, echo: int, trigger:int, threshold_distance:float):
        self.echo = echo
        self.trigger = trigger
        self.threshold_distance = threshold_distance
        self.sensor = DistanceSensor(echo=echo, trigger=trigger)

        self.state = 0  


    def check_distance(self):
        self.state = 1 if self.sensor.distance < self.threshold_distance else 0

    
