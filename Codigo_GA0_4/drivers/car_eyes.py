"""
car_eyes.py
"""

from drivers.eyes import Eyes
from drivers.motors_eyes import Motors
from drivers.controller import ProControllerReader


class Car:
    def __init__(self):
        self.eyes = Eyes(threshold_distance_1=0.3, threshold_distance_2=0.3)
        self.motors = Motors()
        self.mando = ProControllerReader()
        self.direction = "STOP"

    def move(self):
        self.eyes.update_eyes()
        self.motors.start_motors()

        button, pressed = self.mando.get_last_button()

        if button and pressed and button=="B":
            self.motors.stop()
            self.direction = "STOP"

        elif self.eyes.state == 1:
            self.motors.stop()
            self.direction = "STOP"

        else:
            # Si no hay obstáculo y hay entradas, seguir el mando
            button, pressed = self.mando.get_last_button()
            if not button and not pressed:
                self.direction = "STOP"   # inicial
            if button == "ZR" or button == "R":
                self.motors.turn_right()
                self.direction = "DERECHA"
            elif button == "ZL" or button == "L":
                self.motors.turn_left()
                self.direction = "IZQUIERDA"
            elif button == "A":
                self.motors.forward()
                self.direction = "RECTO"
            elif button == "B":
                self.motors.backward()
                self.direction = "ATRAS"
            elif button == "X":
                self.motors.stop() 
                self.direction = "STOP"   
            elif button == "Y":
                self.motors.stop() 
                self.direction = "END"   
        self.motors.stop_motors_and_wait()

    def cleanup(self):
        self.motors.cleanup()

    def get_car_data(self):
        ir_left_val = 0
        ir_right_val = 0
        us_left_val = round(self.eyes.sensor_1.sensor.distance, 3)
        us_right_val = round(self.eyes.sensor_2.sensor.distance, 3)

        return {
            # SENSORES IZQUIERDA
            'ir_left': ir_left_val,
            'us_left': us_left_val,
            'ir_left_active': 0,
            'us_left_active': self.eyes.sensor_1.state,

            # SENSORES DERECHA
            'ir_right': ir_right_val,
            'us_right': us_right_val,
            'ir_right_active': 0,
            'us_right_active': self.eyes.sensor_2.state,

            # MOTORES
            'motor_left': self.motors.speed_left,
            'direccion': self.direction,
            'motor_right': self.motors.speed_right,
        }
