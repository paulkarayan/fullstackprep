from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route("/rand")
def random_number():
    response = jsonify({'data': str(random.randint(0, 100))})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)