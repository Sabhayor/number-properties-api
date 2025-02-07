from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 1:
        return False
    sum_divisors = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    return n == sum(d ** num_digits for d in digits)

def digit_sum(n):
    return sum(int(d) for d in str(n))

def get_fun_fact(n):
    # Placeholder for fetching a fun fact from an external API
    return f"{n} is an interesting number."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": str(number), "error": True}), 400

    number = int(number)
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    return jsonify(response), 200


 

if __name__ == '__main__':
    app.run(debug=True)

