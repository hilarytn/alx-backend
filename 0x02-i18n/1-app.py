#!/usr/bin/env python3
"""This module is a basic Flask
   app to show i18n/L10n and also
   install the Flask-Babel library
   and configure it
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """A simple view for the index file"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
