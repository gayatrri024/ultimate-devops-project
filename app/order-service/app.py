from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.get("/orders")
def orders():
    return jsonify(
        [
            {"id": 101, "product_id": 1, "quantity": 1, "status": "confirmed"},
            {"id": 102, "product_id": 2, "quantity": 2, "status": "processing"},
        ]
    )


@app.post("/orders")
def create_order():
    data = request.get_json()

    return jsonify(
        {
            "message": "Order created",
            "order": data,
        }
    ), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)