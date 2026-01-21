import requests

url = "http://localhost:5000/sumar"
datos = {"numero": 7}

try:
    respuesta = requests.post(url, json=datos)

    if respuesta.status_code == 200:
        print("✅ Resposta correcta:")
        print(respuesta.json())
    elif respuesta.status_code == 400:
        print(f"⚠️ Error {respuesta.status_code}: {respuesta.text}")
    else:
        print(f"⚠️ Error {respuesta.status_code}: {respuesta.text}")

except requests.exceptions.RequestException as e:
    print(f"❌ Error en la connexió: {e}")
