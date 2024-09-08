#!/usr/bin/env python3
""" Parametrize templates with translations.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """ Configuration class for Babel and supported languages. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Get locale from request and match with supported languages. """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def welcome() -> str:
    """ Render the home page with translated content. """
    return render_template('3-index.html', 
                           home_title=_('home_title'), 
                           home_header=_('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

