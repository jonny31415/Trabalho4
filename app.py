from flask import Flask, request, abort
import json

def fact(n):
    assert isinstance(n, int)
    if n == 1:
        return 1
    else: 
        return n*fact(n-1)


def fib(n):
    assert isinstance(n, int)
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

app = Flask(__name__) 

@app.route('/')
@app.route('/index')

def index():
    return "Index Page!"

# myapi: POST -> {'fact': n, 'fib': n} return {'fact': factorial(n), 'fib': fibonacci(n)}
@app.route('/myapi', methods = ['POST'])
def myapi():
    if request.method == 'POST':
        data = request.get_json(force=True) # a multidict containing POST data
        k = list(data.keys())
        return_data = {}
        # Check if fib in post data
        if 'fib' in k:
            return_data['fib'] = fib(data['fib'])
            k.remove('fib')
        # Check if fact in post data
        if 'fact' in k:
            return_data['fact'] = fact(data['fact'])
            k.remove('fact')
        # Check if there are other fields in post data
        if len(k) != 0:
            abort(400)
        
    elif request.method == 'GET':
        return_data = 'Access via GET request'

    return return_data
