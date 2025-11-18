"""
Módulo reservado para el modo de exhibición, sin que los motores funcionen
"""

from drivers.eyes import Eyes
from drivers.lines import Lines
from drivers.motors import Motors


class Car:
    def __init__(self):
        self.eyes = Eyes()
        self.lines = Lines()
        self.motors = Motors()
        self.direction = "STOP"


    def update_all(self):
        self.eyes.update_eyes()
        self.lines.update_lines()

    def decide(self):
        self.update_all()
        if self.eyes.state == 1:
            # self.motors.stop()
            self.direction = "PARADA"
        elif self.lines.state == "RIGHT":
            # self.motors.turn_right()
            self.direction = "DERECHA"
        elif self.lines.state == "LEFT":
            # self.motors.turn_left()
            self.direction = "IZQUIERDA"
        elif self.lines.state == "STRAIGHT":
            # self.motors.forward()
            self.direction = "RECTO"
        else:
            # self.motors.stop()
            self.direction = "PARADA"

    def get_car_data(self):
        ir_left_val = self.lines.sensor_1.sensor.value
        us_left_val = self.eyes.sensor_1.sensor.distance * 100
        ir_right_val = self.lines.sensor_2.sensor.value
        us_right_val = self.eyes.sensor_2.sensor.distance * 100

        return {

            # SENSORES IZQUIERDA
            'ir_left': ir_left_val,
            'us_left': us_left_val,
            'ir_left_active': self.lines.sensor_1.state,
            'us_left_active': self.eyes.sensor_1.state,

            # SENSORES DERECHA
            'ir_right': ir_right_val,
            'us_right': us_right_val,
            'ir_right_active': self.lines.sensor_2.state,
            'us_right_active': self.eyes.sensor_2.state,

            # MOTORES
            'motor_left': 0,
            'direccion': self.direction,
            'motor_right': 0,
        }
