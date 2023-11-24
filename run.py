import os

print("Ejecutando servidor Django...")
os.system("pip install -r requirements.txt")
os.system("python Calculadora/manage.py runserver")