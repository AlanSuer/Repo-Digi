import requests

BASE_URL = "http://localhost:5000/articles"

# --- GET: obtenir tots els articles ---
print("GET /articles →")
resposta = requests.get(BASE_URL)
print("Codi d'estat:", resposta.status_code)
print("Resposta JSON:", resposta.json())

# --- POST: afegir un article nou ---
print("\nPOST /articles →")
nou_article = {"nom": "Ratolí USB", "preu": 12.99}
resposta = requests.post(BASE_URL, json=nou_article)
print("Codi d'estat:", resposta.status_code)
print("Resposta JSON:", resposta.json())

# --- Afegir un segon article (activitat complementària 1) ---
print("\nPOST /articles (segon) →")
nou_article2 = {"nom": "Teclat mecànic", "preu": 45.50}
resposta = requests.post(BASE_URL, json=nou_article2)
print("Codi d'estat:", resposta.status_code)
print("Resposta JSON:", resposta.json())

# Tornem a fer un GET per comprovar que s’han afegit
print("\nGET /articles (després dels POST) →")
resposta = requests.get(BASE_URL)
print("Codi d'estat:", resposta.status_code)
print("Resposta JSON:", resposta.json())

res = requests.get(BASE_URL, params={"id": 1})
print(res.status_code, res.json())

