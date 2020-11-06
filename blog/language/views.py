# -*- coding: utf-8 -*-
from flask import render_template, url_for


class LanguageView:
    def __init__(self):
        self.template = 'language/language.html'

    def language_version(self, language):
        return '<h1>%s</h1>' % (language)

    def year_show(self, year):
        return '<h1>%s</h1>' % (year)

    def render(self, language, year):
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
                  <td>%s</td>
                  <td>%s</td>
                  <td><a href="%s">View</a></td>
                </tr>
                ''' %(version, year, detail_view)
        return tr

    def render(self, languages):
        context = {
            'languages': self.language_table(languages)
        }
        return render_template(self.template, **context)
