#!/bin/bash

ENV_NAME="tervenv"

# Crear el entorno si no existe
if [ ! -d "$ENV_NAME" ]; then
    echo "Creando entorno virtual '$ENV_NAME'..."
    python3 -m venv "$ENV_NAME"

    # Activar el entorno
    source "$ENV_NAME/bin/activate"

    # Instalar los requisitos
    echo "Instalando dependencias desde requirements.txt..."
    pip install -r requirements.txt

    # Desactivar el entorno
    deactivate
else
    echo "El entorno '$ENV_NAME' ya existe."
fi


echo "Proceso completado. El entorno '$ENV_NAME' está listo."
