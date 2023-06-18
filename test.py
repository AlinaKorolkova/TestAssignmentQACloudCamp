import requests


def test_get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_post():
    data = {
        "title": "Test",
        "body": "Test body",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
    assert response.status_code == 201
    assert response.json()["title"] == "Test"


def test_delete_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json() == {}


if __name__ == "__name__":
    test_get_posts()
    test_create_post()
    test_delete_post()
