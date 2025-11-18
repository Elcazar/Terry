"""
clase_infrarrojo.py
Tomamos la clase MCP3008 y añadimos un método check-black que actualiza el 
estado del sensor a 0 o 1 en función de si se supera un umbral.
State solo tiene 2 estados:
    0: El color del suelo no es negro
    1: El color del suelo sí es negro
"""
from gpiozero import MCP3008

class Infrarrojos():
    """
    Toma la clase MCP3008 y añade un método check-black que actualiza el 
    estado del sensor a 0 o 1 en función de si se supera un umbral.
    State solo tiene 2 estados:
        0: El color del suelo no es negro
        1: El color del suelo sí es negro
    """
    def __init__(self, channel: int, threshold: float):
        self.sensor = MCP3008(channel=channel)
        self.threshold = threshold
        self.state = 0

    def check_black(self):
        self.state = 1 if self.sensor.value > self.threshold else 0

