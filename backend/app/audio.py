import sounddevice as sd
import soundfile as sf
import numpy as np

# 16000 Hz, eso quiere decir que son 16000 muestras de audio por segundo
# Utilizamos este numero porque el modelo Whisper utiliza audio a ese numero.

# Con estos datos, esperariamos capturar 80000 muestras de audio por canal
sample_rate = 16000
duration = 5
frames = sample_rate * duration

# rec() = inicia la grabacion y devuelve un array numpy con los datos capturados
print("Iniciando grabacion...")
audio = sd.rec(frames=frames, samplerate=sample_rate, channels=1)

# Espera a que termine la grabacion antes de procesar los datos capturados
sd.wait()
print("Grabacion finalizada")

# Guardar datos en disco duro
filename = "samples/prueba.wav"
try:
    sf.write(file=filename, data=audio, samplerate=sample_rate)    
    print("Archivo .wac guardado exitosamente.")
except Exception as e:
    print(f"Error al guardar archivo: {e}")









