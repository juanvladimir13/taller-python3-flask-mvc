from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates', static_folder='public')

DATABASE = {
	'php': [(2019, 'php7.4'), (2020, 'php8.0')],
	'python': [(2019, 'python3.8'), (2020, 'python3.9')]
}


@app.route('/', endpoint='home', methods=['GET'])
def index():
	context = {
		'user_name': 'juanvladimir13',
		'skills': ['Pascal', 'Object pascal', 'C++', 'Java', 'C#', 'PHP', 'python', ]
	}
	return render_template('home.html', **context)


@app.route('/contact', endpoint='contact', methods=['GET', 'POST'])
def contact():
	if request.method == 'GET':
		return render_template('contact.html')

	if request.method == 'POST':
		email = request.form['email']
		full_name = request.form['full_name']
		whatsapp = request.form['whatsapp']
		message = request.form['message']
		print(email, full_name, whatsapp, message)
		return redirect(url_for('home'))


@app.route('/language', endpoint='language_form', methods=['GET'])
def language_form():
	context = {
		'database': DATABASE
	}
	return render_template('language_query.html', **context)


@app.route('/language/<string:language>/<int:year>', endpoint='language', methods=['GET'])
def language_version_front(language='php', year=2020):
	result = find_language_version(language, year)
	return render_template('language.html', **result)


@app.route('/language/query', endpoint='language_query', methods=['GET'])
def language_version():
	language = request.args.get('language')
	year = int(request.args.get('year'))

	result = find_language_version(language, year)
	return render_template('language.html', **result)


def find_language_version(language, year):
	result = {}
	language_data = DATABASE[language]
	if language:
		for item in language_data:
			if item[0] == year:
				result['language_version'] = item[1]
				result['year'] = year

	return result


@app.errorhandler(404)
def not_found(error):
	return render_template('error.html'), 404


if __name__ == '__main__':
	app.run(port=8000, debug=True)
