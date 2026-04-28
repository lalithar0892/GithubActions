from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Raj"},
    {"id": 2, "name": "Kiran"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

if __name__ == "__main__":
    app.run(debug=True)
# import requests
# import sys

# method = sys.argv[1]

# def test_get():
#     response = requests.get("https://jsonplaceholder.typicode.com/users/1")
#     assert response.status_code == 200
#     print("GET Passed")

# def test_post():
#     payload = {"title": "API", "body": "Test", "userId": 1}
#     response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
#     assert response.status_code == 201
#     print("POST Passed")

# def test_put():
#     payload = {"id": 1, "title": "Updated", "body": "Updated", "userId": 1}
#     response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=payload)
#     assert response.status_code == 200
#     print("PUT Passed")

# def test_patch():
#     payload = {"title": "Patched"}
#     response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=payload)
#     assert response.status_code == 200
#     print("PATCH Passed")

# def test_delete():
#     response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
#     assert response.status_code == 200
#     print("DELETE Passed")


# if __name__ == "__main__":
#     print(f"Running method: {method}")

#     if method == "GET":
#         test_get()
#     elif method == "POST":
#         test_post()
#     elif method == "PUT":
#         test_put()
#     elif method == "PATCH":
#         test_patch()
#     elif method == "DELETE":
#         test_delete()
#     else:
#         print("❌ Invalid Method")