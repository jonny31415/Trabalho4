from flask import Flask, request, abort
from math import sqrt
from decimal import Decimal, getcontext, ROUND_UP

# Factorial function
def fact(n):
    # Check if n is an integer
    if not isinstance(n, int):
        abort(400)
    # Check if n is positive
    if n < 0:
        abort(400)
    # Check if n is too large
    if n > 980: # See README.md for more details
        abort(400)
    # Function
    if n == 0:
        return 1
    else: 
        return n*fact(n-1)

# Recursive Fibonacci function -> Not used
def fib(n):
    # Check if n is an integer
    if not isinstance(n, int):
        abort(400)
    # Check if n is positive
    if n <= 0:
        abort(400)
    # Function
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Optimal Fibonacci function - using Binet's formula
def optimal_fib(n):
    # Check if n is an integer
    if not isinstance(n, int):
        abort(400)
    # Check if n is positive
    if n <= 0:
        abort(400)
    # Check if n is too large
    if n > 19600: # See README.md for more details
        abort(400)
    # Function
    phi = (1 + Decimal(5).sqrt()) / 2
    getcontext().prec = 4096 # You need to tweak this number based on your precision requirements 
    c = Decimal(phi) ** n
    fib = (c - (Decimal(-1)** n) / c) / Decimal(5).sqrt()
    return fib.quantize(Decimal('1.'), rounding=ROUND_UP)

# Create Flask app
app = Flask(__name__) 

@app.route('/')
@app.route('/index')

def index():
    return "Index Page!"

# myapi: POST -> {'fact': n, 'fib': n} return {'fact': factorial(n), 'fib': fibonacci(n)}
@app.route('/myapi', methods = ['POST'])
def myapi():
    if request.method == 'POST':
        data = request.get_json(force=True)
        k = list(data.keys())
        return_data = {}
        # Check if fib in post data
        if 'fib' in k:
            return_data['fib'] = optimal_fib(data['fib'])
            k.remove('fib')
        # Check if fact in post data
        if 'fact' in k:
            return_data['fact'] = fact(data['fact'])
            k.remove('fact')
        # Check if there are other fields in post data
        if len(k) != 0:
            abort(400)

    return return_data
