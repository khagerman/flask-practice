# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def calc_add():
    """Add given a and b params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = add(a, b)
    return str(res)


@app.route("/sub")
def calc_subtract():
    """""Subtract given a and b params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = sub(a, b)
    return str(res)


@app.route("/mult")
def calc_multiply():
    """Multiply given a and b params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = mult(a, b)
    return str(res)


@app.route("/div")
def calc_divide():
    """Divide given a and b params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = div(a, b)
    return str(res)


# Further Study

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<operation>")
def calc_math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = operations[operation](a, b)
    return str(res)
