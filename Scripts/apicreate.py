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