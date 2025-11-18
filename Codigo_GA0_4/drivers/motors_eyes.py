import RPi.GPIO as GPIO
from rpi_hardware_pwm import HardwarePWM
import time

class Motors:
    def __init__(self,
                 in1_left=6, in2_left=7, pwm_channel_left=1, factor_correccion_1=0.433,
                 in1_right=4, in2_right=5, pwm_channel_right=0, factor_correccion_2=0.733,
                 STANDARD_SPEED=80, GIRO_SPEED=0, burst_time=0.1, wait_time=0.075):

        # Configuración de pines 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1_left, GPIO.OUT)
        GPIO.setup(in2_left, GPIO.OUT)
        GPIO.setup(in1_right, GPIO.OUT)
        GPIO.setup(in2_right, GPIO.OUT)

        self.in1_left = in1_left
        self.in2_left = in2_left
        self.in1_right = in1_right
        self.in2_right = in2_right


        self.speed_right = STANDARD_SPEED
        self.speed_left = STANDARD_SPEED

        self.STANDARD_SPEED = STANDARD_SPEED
        self.GIRO_SPEED = GIRO_SPEED

        self.burst_time = burst_time
        self.wait_time = wait_time

        # Inicialización PWM
        self.motor_left = HardwarePWM(pwm_channel=pwm_channel_left, hz=int(20_000 * factor_correccion_1))
        self.motor_right = HardwarePWM(pwm_channel=pwm_channel_right, hz=int(20_000 * factor_correccion_2))

        # self.motor_left.start(initial_duty_cycle=70)
        # self.motor_right.start(initial_duty_cycle=70)

    def start_motors(self):
        self.motor_left.start(initial_duty_cycle=70)
        self.motor_right.start(initial_duty_cycle=70)

    def stop_motors_and_wait(self):
        self.motor_left.stop()
        self.motor_right.stop()
        self.speed_left = 0
        self.speed_right = 0
        time.sleep(self.wait_time)
    
    def set_speed(self, left_speed, right_speed):
        self.speed_left = max(0, min(100, left_speed))
        self.speed_right = max(0, min(100, right_speed))
        self.motor_left.change_duty_cycle(self.speed_left)
        self.motor_right.change_duty_cycle(self.speed_right)

    def forward(self):
        GPIO.output(self.in1_left, GPIO.HIGH)
        GPIO.output(self.in2_left, GPIO.LOW)
        GPIO.output(self.in1_right, GPIO.HIGH)
        GPIO.output(self.in2_right, GPIO.LOW)
        self.speed_left = self.STANDARD_SPEED
        self.speed_right = self.STANDARD_SPEED
        self.set_speed(self.speed_left, self.speed_right)
        time.sleep(self.burst_time)

    def backward(self):
        GPIO.output(self.in1_left, GPIO.LOW)
        GPIO.output(self.in2_left, GPIO.HIGH)
        GPIO.output(self.in1_right, GPIO.LOW)
        GPIO.output(self.in2_right, GPIO.HIGH)
        self.speed_left = self.STANDARD_SPEED
        self.speed_right = self.STANDARD_SPEED
        self.set_speed(self.speed_left, self.speed_right)
        time.sleep(self.burst_time)

    def stop(self):
        self.speed_left = 0
        self.speed_right = 0
        self.set_speed(0, 0)
        self.motor_left.stop()
        self.motor_right.stop()
        time.sleep(0.1)

    def turn_left(self):
        GPIO.output(self.in1_left, GPIO.LOW)
        GPIO.output(self.in2_left, GPIO.LOW)
        GPIO.output(self.in1_right, GPIO.HIGH)
        GPIO.output(self.in2_right, GPIO.LOW)
        self.speed_left = self.GIRO_SPEED
        self.speed_right = self.STANDARD_SPEED
        self.set_speed(self.speed_left, self.speed_right)
        time.sleep(self.burst_time)

    def turn_right(self):
        self.speed_left = self.STANDARD_SPEED
        self.speed_right = self.GIRO_SPEED
        GPIO.output(self.in1_left, GPIO.HIGH)
        GPIO.output(self.in2_left, GPIO.LOW)
        GPIO.output(self.in1_right, GPIO.LOW)
        GPIO.output(self.in2_right, GPIO.LOW)
        self.set_speed(self.speed_left, self.speed_right)
        time.sleep(self.burst_time)

    def get_speed_left(self):
        return self.speed_left

    def get_speed_right(self):
        return self.speed_right

    def cleanup(self):
        self.motor_right.stop()
        self.motor_left.stop()
        GPIO.cleanup()
