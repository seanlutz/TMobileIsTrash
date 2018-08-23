from flask import Flask
import requests
import sys
app = Flask(__name__)
def p(x):
    print(x, file=sys.stderr)

@app.route("/")
def health():
    return "up"

@app.route('/<path:subpath>')
def browse(subpath):
    p("going yay!!")
    p(subpath)
    res = requests.get(subpath).text
    p(type(res))
    return res
