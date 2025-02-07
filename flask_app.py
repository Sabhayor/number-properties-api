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
    # Ensure the request has JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    # Get JSON data from the request
    data = request.get_json()

    # Check if 'number' is present in the JSON payload
    if 'number' not in data:
        return jsonify({"error": "Missing 'number' in JSON payload"}), 400

    number = data['number']

    # Validate that the input is a valid integer
    if not isinstance(number, int):
        return jsonify({"error": "Input must be a valid integer"}), 400

    # Calculate properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Prepare response
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }

    # Return JSON response with correct Content-Type header
    return jsonify(response), 200

# Error handler for 404 (Not Found)
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

# Error handler for 500 (Internal Server Error)
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)