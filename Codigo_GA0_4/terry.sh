#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
RED='\033[0;31m'
NC='\033[0m' 

echo -e "${BLUE}[INFO] Activando entorno virtual...${NC}"
source tervenv/bin/activate

echo -e "${BLUE}[INFO] Conectando el mando...${NC}"
bash utils/remote.sh

echo -e "${BLUE}[INFO] Lanzando Terry...${NC}"
python3 main.py
