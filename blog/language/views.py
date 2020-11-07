# -*- coding: utf-8 -*-
from flask import render_template, url_for


class LanguageView:
    def __init__(self):
        self.template = 'language/language.html'

    def language_version(self, language):
        return '<h1>' + language + '</h1>'

    def year_show(self, year):
        return '<h1>' + str(year) + '</h1>'

    def render(self, language='', year=''):
        if not language or not year:
            context = {'message': '<h1>Dato no encontrado</h1>'}
        else:
            context = {
                'language': self.language_version(language),
                'year': self.year_show(year)
            }
        return render_template(self.template, **context)


class LanguageFormView:
    def __init__(self):
        self.template = 'language/language_form.html'

    def language_table(self, languages):
        tr = ''
        for key in languages:
            for column in languages[key]:
                year, version = column
                detail_view = url_for('language_pretty', language=key, year=year)
                tr += '''
                <tr>
                    <td>{version}</td>
                    <td>{year}</td>
                    <td><a href="{detail_view}">View</a></td>
                </tr>
                '''.format(version=version, year=year, detail_view=detail_view)
        return tr

    def render(self, languages):
        context = {
            'languages': self.language_table(languages)
        }
        return render_template(self.template, **context)
