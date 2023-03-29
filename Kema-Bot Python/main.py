import os
import subprocess

# Pide al usuario que ingrese la llave
key = input("Por favor ingrese la llave: ")

# Reemplaza la llave en los otros archivos
for filename in ['acrepi.py', 'estado.py', 'fun.py', 'streaming.py', 'tester.py', 'utilidades.py']:
    with open(filename, 'rb') as f:
        content = f.read().decode('latin-1')
    content = content.replace('LLAVE_SECRETA', key)
    with open(filename, 'w') as f:
        f.write(content)

# Ejecuta los archivos
procesos = []
for archivo in ['acrepi.py', 'estado.py', 'fun.py', 'streaming.py', 'tester.py', 'utilidades.py']:
    proceso = subprocess.Popen(['python', archivo])
    procesos.append(proceso)

# No se espera a que los procesos terminen
