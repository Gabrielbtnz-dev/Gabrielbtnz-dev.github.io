import requests
import base64

# URL base del servidor FastAPI
URL_BASE = "http://localhost:8001"

# URL del endpoint /update/
url = URL_BASE + "/update/"

# Ruta del archivo .p12 y la contraseña
#p12_file_path = "ruta/al/archivo.p12"  # Especifica la ruta del archivo .p12
file_base64 = base64.b64encode(b"FAKE_P12_CONTENT").decode('utf-8')
password = "tu_contraseña"  # Especifica la contraseña del archivo .p12

# Leer el archivo .p12 y codificarlo en base64
#with open(p12_file_path, "rb") as f:
  #  file_data = f.read()
 #   file_base64 = base64.b64encode(file_data).decode('utf-8')

# Crear el payload para la solicitud
payload = {
    "file": file_base64,
    "pass": password
}

# Hacer la solicitud POST al endpoint /update/
response = requests.post(url, json=payload)

# Verificar la respuesta del servidor
if response.status_code == 200:
    print("Archivo subido correctamente:", response.json())
else:
    print(f"Error al subir archivo: {response.status_code} - {response.text}")

# URL del endpoint /ruc/
url = URL_BASE + "/ruc/"

# Lista de RUCs a verificar
rucs = ["4303489", "43034890"]

# Hacer la solicitud GET por cada RUC
for ruc in rucs:
    response = requests.get(f"{url}{ruc}")

    # Verificar la respuesta para cada RUC
    if response.status_code == 200:
        print(f"Verificación del RUC {ruc} exitosa:", response.json())
    else:
        print(f"Error al verificar el RUC {ruc}: {response.status_code} - {response.text}")
    
    print("-" * 40)  # Separador entre las respuestas