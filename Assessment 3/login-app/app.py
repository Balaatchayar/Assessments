from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # Check username and password
    if data['username'] == 'admin' and data['password'] == 'password':
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'})

if __name__ == '__main__':
    app.run(debug=True)






