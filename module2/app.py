from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Cloud Native Patterns", "author": "Cornelia Davis"},
    {"id": 2, "title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann"}
]

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
