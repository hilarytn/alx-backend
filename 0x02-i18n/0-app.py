#!/usr/bin/env python3
"""Set up flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """A simple view for the index file"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
