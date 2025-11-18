"""
main.py
"""

from drivers.car import Car
from web.app import app, set_car
import threading
import time

def brain_loop(car: Car):
    while True:
        car.decide() 
        #time.sleep(0.001)


if __name__ == "__main__":
    try:
        car = Car()
        set_car(car)

        thread = threading.Thread(target=brain_loop, args=(car,), daemon=True)
        thread.start()
    except Exception as error:
        pass

    # Lanza el servidor web
    app.run(host='0.0.0.0', port=5000)