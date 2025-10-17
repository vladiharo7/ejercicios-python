# ⚙️ Cómo crear y usar un ambiente virtual

## 1. Crear un ambiente virtual
python -m venv nombre_del_entorno


Por convención, se suele usar .venv o env como nombre:
python -m venv .venv


Esto crea una carpeta .venv/ con una copia aislada de Python.

## 2. Activar el ambiente virtual
- Windows (CMD o PowerShell):
.venv\Scripts\activate


- macOS/Linux:
source .venv/bin/activate


Verás que el prompt cambia, indicando que estás dentro del entorno.

## 3. Instalar paquetes dentro del entorno
Una vez activado, puedes instalar paquetes sin afectar el sistema global:
pip install requests


Y guardar dependencias con:
pip freeze > requirements.txt


## 4. Salir del ambiente virtual
deactivate


Esto te devuelve al entorno global de Python.

## 5. Recrear el ambiente en otra máquina
python -m venv .venv
source .venv/bin/activate  # o .venv\Scripts\activate en Windows
pip install -r requirements.txt

