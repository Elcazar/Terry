# PROYECTO FINAL DE SISTEMAS ELECTRÓNICOS: TERRY

## Autores  
Alejandro Alcázar Mendoza

Jorge Gonzélez Pérez

---

## Instalación

Antes de ejecutar el proyecto, asegúrate de tener instalado Python 3 y de crear un entorno virtual con las dependencias necesarias.

Puedes hacerlo ejecutando el siguiente script desde la raíz del proyecto:

```bash
bash utils/setup.sh
```
---

## Modos de funcionamiento
El proyecto dispone de tres modos de operación principales:

1. **Modo Exhibición**

Archivo: `main.sh`

Modo pensado para demostraciones sin necesidad de motores. Permite mostrar el sistema sin movimiento físico para comprobar el funcionamiento de los sensores.

2. **Modo Mando a Distancia**

Archivo: `terry_eyes.sh`

El coche puede ser controlado a través de un mando conectado por Bluetooth.
Utiliza sensores ultrasónicos para detectar obstáculos. `A` para seguir en línea recta, `B` para marcha atrás, `ZR` y `ZL` para giros a derecha e izquierda, `X` para parar e `Y` para finalizar. 

3. **Modo Autónomo**

Archivo: `terry_lines.sh`

El coche sigue una línea automáticamente mediante sensores infrarrojos.

---
## Interfaz Gráfica

El proyecto cuenta con una interfaz web desarrollada con Flask.
Desde ella, es posible visualizar el estado del vehículo desde el navegador para observar el estado del vehículo. 

---
## Estructura del proyecto

.
├── drivers/                      # Módulos del coche, sensores y lógica de control
│   ├── __init__.py
│   ├── car.py                    # Clase base de coche
│   ├── car_eyes.py               # Modo con mando
│   ├── car_lines.py              # Modo sigue líneas
│   ├── clase_infrarrojo.py       # Clase base infrarrojos
│   ├── clase_ultrasonidos.py     # Clase base ultrasonidos
│   ├── controller.py             # Gestión del mando
│   ├── eyes.py                   # Control de los ultrasonidos juntos
│   ├── lines.py                  # Control de los infrarrojos juntos
│   ├── motors.py                 # Motores en modo sigue líneas
│   └── motors_eyes.py            # Motores en modo manual (mando)
│
├── tervenv/                      # Entorno virtual de Python
│
├── utils/                        # Scripts auxiliares
│   ├── requirements.txt          # Dependencias necesarias del proyecto
│   ├── setup.sh                  # Instalación automática del entorno virtual y dependencias
│   └── remote.sh                 # Conexión al mando
│
├── web/                          # Interfaz web con Flask
│   ├── app.py                    # Aplicación principal de Flask
│   ├── templates/
│   │   └── index.html            # Plantilla HTML de la interfaz
│   └── static/
│       ├── css/
│       │   └── style.css         # Estilos personalizados
│       └── images/
│           └── ghibli_car.png   # Imagen decorativa
│
├── main.py                       # Modo Exhibición
├── main_eyes.py                  # Modo con mando + sensores ultrasónicos
├── main_lines.py                 # Modo sigue líneas
│
├── terry.sh                      # Lanzador modo Exhibición
├── terry_eyes.sh                 # Lanzador modo Mando + Obstáculos
├── terry_lines.sh                # Lanzador modo Autónomo (líneas)
│
└── README.md                     # Documentación general