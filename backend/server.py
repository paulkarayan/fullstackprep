from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route("/rand")
def random_number():
    response = jsonify({'data': str(random.randint(0, 100))})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/coinflips/<int:nums>")
def coin_flipper(nums):
    # naive way
    heads, tails = 0, 0 
    for idx in range(nums):
        if random.randint(0, 1):
            heads += 1
        else:
            tails += 1

    # or lets do it even easier
    heads = random.randint(0, nums)
    response = jsonify({'heads': heads,
                        'tails': nums - heads,
                        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug=True)