from flask import Flask, jsonify, request
app = Flask(__name__)

verySecureDatabase = []

@app.route('/', methods=['GET'])
def test():
    return jsonify({"message" : "It works!"})

@app.route('/base', methods=['POST'])
def test3():
    global verySecureDatabase
    requestData = request.form
    verySecureDatabase.append(requestData)

@app.route('/base', methods=['GET'])
def test4():
    global verySecureDatabase
    return verySecureDatabase

if __name__ == '__main__':
    app.run(debug=True, port = 8000)