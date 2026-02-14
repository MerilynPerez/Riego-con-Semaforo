import time
import random
from datetime import datetime

# ==============================
# ESTADOS DEL SEMÁFORO
# ==============================

class EstadoSemaforo:
    ROJO = "🔴 ROJO - Riego Apagado"
    VERDE = "🟢 VERDE - Riego Activado"
    AMARILLO = "🟡 AMARILLO - Falla del Sensor"


# ==============================
# SENSOR
# ==============================

def leer_humedad():
    time.sleep(0.05)  # 50 ms

    fallo = random.choice([False, False, False, True])
    if fallo:
        return None

    return random.randint(20, 90)


# ==============================
# CONTROLADOR
# ==============================

UMBRAL_MIN = 40
UMBRAL_MAX = 70

def decidir_riego(humedad):
    time.sleep(0.1)  # 100 ms

    if humedad < UMBRAL_MIN:
        return "ENCENDER"
    elif humedad > UMBRAL_MAX:
        return "APAGAR"
    else:
        return "MANTENER"


# ==============================
# BASE DE DATOS (archivo)
# ==============================

def registrar(evento):
    with open("registro_riego.txt", "a") as f:
        f.write(f"{datetime.now()} - {evento}\n")


# ==============================
# SISTEMA PRINCIPAL INTEGRADO
# ==============================

print("=== Sistema de Riego + Semáforo (STR Integrado) ===\n")

estado_riego = "APAGADO"
estado_semaforo = EstadoSemaforo.ROJO

while True:

    humedad = leer_humedad()

    # ---- FALLO ----
    if humedad is None:
        print("⚠️ Fallo del sensor")
        estado_riego = "APAGADO"
        estado_semaforo = EstadoSemaforo.AMARILLO
        registrar("Fallo del sensor - Riego APAGADO")

        print(estado_semaforo)
        print("----------------------------------")
        time.sleep(2)
        continue

    # ---- CONTROL ----
    accion = decidir_riego(humedad)

    if accion == "ENCENDER":
        estado_riego = "ENCENDIDO"
        estado_semaforo = EstadoSemaforo.VERDE

    elif accion == "APAGAR":
        estado_riego = "APAGADO"
        estado_semaforo = EstadoSemaforo.ROJO

    # ---- SALIDA ----
    print(f"Humedad: {humedad}%")
    print(f"Riego: {estado_riego}")
    print(f"Semáforo: {estado_semaforo}")

    registrar(f"Humedad {humedad}% - Riego {estado_riego}")

    print("----------------------------------")
    time.sleep(1)