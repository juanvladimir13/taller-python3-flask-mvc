# -*- coding: utf-8 -*-
from flask import Flask, render_template

from blog.language.controllers import LanguageController
from blog.user.controllers import UserController

app = Flask(__name__, template_folder='templates', static_folder='public')


@app.route('/', endpoint='home', methods=['GET'])
def index():
    controller = UserController()
    return controller.index()


@app.route('/contact/', endpoint='contact', methods=['GET', 'POST'])
def contact():
    controller = UserController()
    return controller.contact()


@app.route('/language/', endpoint='language_form', methods=['GET'])
def language_form():
    language = LanguageController()
    return language.language_form()


@app.route('/language/<string:language>/<int:year>', endpoint='language_pretty', methods=['GET'])
def language_get_pretty(language='php', year=2020):
    controller = LanguageController()
    return controller.language_get_pretty(language, year)


@app.route('/language/query', endpoint='language_params', methods=['GET'])
def language_get_params():
    controller = LanguageController()
    return controller.language_get_params()


@app.errorhandler(404)
def route_not_found(error):
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(port=8000, debug=True)
