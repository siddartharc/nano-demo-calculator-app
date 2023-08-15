from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Welcome to the calculator API!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json  # Assuming you're sending JSON data in the request
    if 'numbers' in data and isinstance(data['numbers'], list):
        result = sum(data['numbers'])
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Invalid data"}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    if 'numbers' in data and isinstance(data['numbers'], list) and len(data['numbers']) == 2:
        result = data['numbers'][0] - data['numbers'][1]
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
