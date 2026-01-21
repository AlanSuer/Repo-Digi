from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/sumar", methods=["POST"])
def sumar():
    dades = request.get_json()

    # Validación básica
    if not dades or "numero" not in dades:
        return jsonify({"error": "Falta el camp 'numero'"}), 400

    try:
        numero = int(dades["numero"])
    except (ValueError, TypeError):
        return jsonify({"error": "'numero' ha de ser un enter"}), 400

    # Ejemplo: devolvemos el número y su suma +10 (puedes cambiar la lógica)
    resultat = {
        "numero": numero,
        "resultat": numero + 10
    }
    return jsonify(resultat), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
