from flask import Flask, render_template

from blog.language.controllers import LanguageController
from blog.user.controllers import UserController

app = Flask(__name__, template_folder='templates', static_folder='public')


@app.route('/', endpoint='home', methods=['GET'])
def route_index():
    controller = UserController()
    return controller.index()


@app.route('/contact/', endpoint='contact', methods=['GET', 'POST'])
def route_contact():
    controller = UserController()
    return controller.contact()


@app.route('/language/', endpoint='language_form', methods=['GET'])
def route_language_form():
    language = LanguageController()
    return language.language_form()


@app.route('/language/<string:language>/<int:year>', endpoint='language_pretty', methods=['GET'])
def route_language_version_front(language='php', year=2020):
    controller = LanguageController()
    return controller.language_version_front(language, year)


@app.route('/language/query', endpoint='language_params', methods=['GET'])
def route_language_version():
    controller = LanguageController()
    return controller.language_version()


@app.errorhandler(404)
def route_not_found(error):
    return render_template('error.html'), 4040


if __name__ == '__main__':
    app.run(port=8000, debug=True)
