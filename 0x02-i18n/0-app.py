#!/usr/bin/env python3
from flask import Flask, render_template
"""A basic Flask app to show i18n/L10n"""


app = Flask(__name__)


@app.route('/')
def index():
    """A simple view for the index file"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
