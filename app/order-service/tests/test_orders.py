from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_orders():
    client = app.test_client()
    response = client.get("/orders")

    assert response.status_code == 200
    assert len(response.json) == 2


def test_create_order():
    client = app.test_client()

    response = client.post(
        "/orders",
        json={"product_id": 1, "quantity": 2},
    )

    assert response.status_code == 201
    assert response.json["message"] == "Order created"
    assert response.json["order"]["product_id"] == 1