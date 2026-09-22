from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_products():
    client = app.test_client()

    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.json) == 3