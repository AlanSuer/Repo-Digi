from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de dades temporal (memòria)
articles = []
seguent_id = 1

# --- GET: obtenir tots els articles ---
@app.route("/articles", methods=["GET"])
def obtenir_articles():
    article_id = request.args.get("id")

    if article_id is None:
        return jsonify(articles), 200

    try:
        article_id = int(article_id)
    except ValueError:
        return jsonify({"error": "El parametre 'id' ha de ser un enter"}), 400

    for a in articles:
        if a["id"] == article_id:
            return jsonify(a), 200

    return jsonify({"error": "Article no trobat"}), 404

# --- POST: afegir un article nou ---
@app.route("/articles", methods=["POST"])
def afegir_article():
    global seguent_id

    dades = request.get_json()

    # Validació bàsica
    if not dades or "nom" not in dades or "preu" not in dades:
        return jsonify({"error": "Falten camps obligatoris (nom, preu)"}), 400

    nom = str(dades["nom"]).strip()

    # Validar nom no buit
    if nom == "":
        return jsonify({"error": "El camp 'nom' no pot estar buit"}), 400

    # Validar preu positiu
    try:
        preu = float(dades["preu"])
    except (ValueError, TypeError):
        return jsonify({"error": "El camp 'preu' ha de ser un número"}), 400

    if preu <= 0:
        return jsonify({"error": "El 'preu' ha de ser positiu"}), 400

    # Crear i afegir article
    article = {
        "id": seguent_id,
        "nom": nom,
        "preu": preu
    }
    articles.append(article)
    seguent_id += 1

    return jsonify(article), 201


if __name__ == "__main__":
    app.run(debug=True)
