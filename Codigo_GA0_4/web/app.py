from flask import Flask, render_template, jsonify
import subprocess
app = Flask(__name__)

car = None  # variable global para almacenar el objeto Car

def set_car(car_instance):
    global car
    car = car_instance

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_state')
def get_state():
    car_data = car.get_car_data()
    return jsonify(car_data)

@app.route('/get_gamepad_status')
def get_gamepad_status():
    def get_battery():
        try:
            out = subprocess.check_output(['upower', '-d'], text=True)
            blocks = out.split('\n\n')
            for block in blocks:
                if "Pro Controller" in block:
                    for line in block.splitlines():
                        if "percentage" in line:
                            raw = line.strip().split(":")[1].strip()
                            return raw.split()[0]  

        except:
            return "N/D"
        return "N/D"

    battery = get_battery()
    return jsonify({
        'connected': battery != "N/D",
        'battery': battery
    })
