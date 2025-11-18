from drivers.lines import Lines
from drivers.motors import Motors


class Car:
    def __init__(self):
        self.lines = Lines()
        self.motors = Motors()
        self.direction = "STOP"


    def update_all(self):
        self.lines.update_lines()

    def decide(self):
        self.update_all()
        if self.lines.state == "RIGHT":
            self.motors.turn_right()
            self.direction = "DERECHA"
        elif self.lines.state == "LEFT":
            self.motors.turn_left()
            self.direction = "IZQUIERDA"
        elif self.lines.state == "STRAIGHT":
            self.motors.forward()
            self.direction = "RECTO"
        else:
            self.motors.stop()
            self.direction = "END"

    def move(self):
        self.update_all()
        self.motors.start_motors()

        if self.lines.state == "RIGHT":
            self.motors.turn_right()
            self.direction = "DERECHA"
        elif self.lines.state == "LEFT":
            self.motors.turn_left()
            self.direction = "IZQUIERDA"
        elif self.lines.state == "STRAIGHT":
            self.motors.forward()
            self.direction = "RECTO"
        else:
            self.motors.stop()
            self.direction = "END"

        self.motors.stop_motors_and_wait()

    def cleanup(self):
        self.motors.cleanup()


    def get_car_data(self):
        ir_left_val = self.lines.sensor_1.sensor.value
        us_left_val = 100
        ir_right_val = self.lines.sensor_2.sensor.value
        us_right_val = 100

        return {
            # SENSORES IZQUIERDA
            'ir_left': ir_left_val,
            'us_left': us_left_val,
            'ir_left_active': self.lines.sensor_1.state,
            'us_left_active': 0,

            # SENSORES DERECHA
            'ir_right': ir_right_val,
            'us_right': us_right_val,
            'ir_right_active': self.lines.sensor_2.state,
            'us_right_active': 0,

            # MOTORES
            'motor_left': self.motors.speed_left,
            'direccion': self.direction,
            'motor_right': self.motors.speed_right,
        }
