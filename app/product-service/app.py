from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.get("/products")
def products():
    return jsonify(
        [
            {
                "id": 1,
                "name": "Laptop",
                "price": 50000,
            },
            {
                "id": 2,
                "name": "Keyboard",
                "price": 2500,
            },
            {
                "id": 3,
                "name": "Mouse",
                "price": 1200,
            },
        ]
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)