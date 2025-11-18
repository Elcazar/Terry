import threading
from evdev import InputDevice, list_devices, ecodes

class ProControllerReader:
    def __init__(self):
        self.device = self._find_controller()
        if not self.device:
            raise RuntimeError("No se encontró el Pro Controller.")

        self.running = True
        self.last_event = (None, None)
        self.event_condition = threading.Condition()

        self.code_map = {
            305: "A",
            304: "B",
            307: "X",
            308: "Y",
            313: "ZL",
            312: "ZR",
            310: "L",
            311: "R"
        }

        self.thread = threading.Thread(target=self._listen, daemon=True)
        self.thread.start()

    def _find_controller(self):
        for dev in [InputDevice(path) for path in list_devices()]:
            if "Pro Controller" in dev.name:
                return dev
        return None

    def _listen(self):
        for event in self.device.read_loop():
            if event.type == ecodes.EV_KEY:
                code = event.code
                if code in self.code_map:
                    pressed = event.value == 1
                    self._store_event(self.code_map[code], pressed)

            elif event.type == ecodes.EV_ABS:
                if event.code == ecodes.ABS_HAT0X:
                    if event.value == -1:
                        self._store_event("LEFT", True)
                    elif event.value == 1:
                        self._store_event("RIGHT", True)
                    elif event.value == 0:
                        self._store_event("LEFT", False)
                        self._store_event("RIGHT", False)
                elif event.code == ecodes.ABS_HAT0Y:
                    if event.value == -1:
                        self._store_event("UP", True)
                    elif event.value == 1:
                        self._store_event("DOWN", True)
                    elif event.value == 0:
                        self._store_event("UP", False)
                        self._store_event("DOWN", False)

    def _store_event(self, button_name, pressed):
        with self.event_condition:
            self.last_event = (button_name, pressed)
            self.event_condition.notify_all()

    def get_last_button(self):
        return self.last_event
