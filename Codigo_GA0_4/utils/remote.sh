#!/bin/bash

# Colores ANSI
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
RED='\033[0;31m'
NC='\033[0m' # Reset

MAC="98:B6:4F:05:0C:73"
echo -e "${BLUE}[INFO] Verificando estado del mando $MAC...${NC}"

# Activar agente 
echo -e "agent on\ndefault-agent\n" | bluetoothctl > /dev/null
sleep 1

# Verificar si ya está conectado
info_output=$(echo -e "info $MAC\n" | bluetoothctl)
if echo "$info_output" | grep -q "Connected: yes"; then
  echo -e "${GREEN}[SUCCESS] Mando ya está conectado.${NC}"
  exit 0
fi

# Intentar conectar si no lo estaba
echo -e "${BLUE}[INFO] Mando no está conectado. Intentando conectar...${NC}"
connect_output=$(echo -e "connect $MAC\n" | bluetoothctl)

if echo "$connect_output" | grep -q "Connection successful"; then
  echo -e "${GREEN}[SUCCESS] Mando conectado correctamente.${NC}"
else
  echo -e "${RED}[FAIL] No se pudo conectar el mando. ¿Está encendido y cerca?${NC}"
fi
