from flask import Flask, jsonify, request
app = Flask(__name__)

verySecureDatabase = {}

@app.route('/', methods=['GET'])
def test():
    return jsonify({"message" : "It works!"})

@app.route('/base', methods=['POST'])
def test3():
    global verySecureDatabase
    verySecureDatabase = request.get_json()
    return verySecureDatabase


@app.route('/base', methods=['GET'])
def test4():
    global verySecureDatabase
    print("this ran")
    return verySecureDatabase

if __name__ == '__main__':
    app.run(debug=True, port = 8000)