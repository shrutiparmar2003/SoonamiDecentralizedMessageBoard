from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if verify_user(username, password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/messages', methods=['GET', 'POST'])
def manage_messages():
    if request.method == 'POST':
        message = request.json.get('message')
        messages.append(message)
        return jsonify({"message": "Message posted"}), 200
    elif request.method == 'GET':
        return jsonify({"messages": messages})

def verify_user(username, password):
    # Simple user verification (hardcoded for simplicity)
    return username == "user" and password == "pass"

if __name__ == '_main_':
    app.run(debug=True)