"""
main.py
"""

from drivers.car_eyes import Car
from web.app import app, set_car
import threading

def brain_loop(car: Car):
    while True:
        car.move() 
        if car.direction == "END":
            car.cleanup()
            break

def main():
    car = Car()
    set_car(car)

    thread = threading.Thread(target=brain_loop, args=(car,), daemon=True)
    thread.start()

    #Lanza el servidor web
    app.run(host='0.0.0.0', port=5000)


    print("FINISHED!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as error:
        print("\r")
        print("FIN")
    except Exception as error:
        print(error)