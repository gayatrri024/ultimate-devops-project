from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.get("/users")
def users():
    return jsonify(
        [
            {"id": 1, "name": "Alice", "role": "customer"},
            {"id": 2, "name": "Bob", "role": "customer"},
        ]
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)