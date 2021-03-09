from flask import Flask, request, render_template, jsonify
import logging
app = Flask(__name__)

logging.basicConfig(filename='log.log', level=logging.DEBUG)

@app.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
