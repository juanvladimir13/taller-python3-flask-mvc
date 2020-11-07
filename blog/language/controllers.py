# -*- coding: utf-8 -*-
from flask import request

from .models import DATABASE
from .views import LanguageView, LanguageFormView


class LanguageController:
    def __init__(self):
        self.model = None
        self.view_find = LanguageView()
        self.view_form = LanguageFormView()

    def language_form(self):
        return self.view_form.render(DATABASE)

    def language_get_pretty(self, language='php', year=2020):
        result = self.find_language_version(language, year)
        return self.view_find.render(**result)

    def language_get_params(self):
        language = request.args.get('language')
        year = request.args.get('year')

        result = self.find_language_version(language, year)
        return self.view_find.render(**result)

    def find_language_version(self, language, year):
        result = {}
        language_data = DATABASE.get(language)
        if language_data:
            for item in language_data:
                if str(item[0]) == str(year):
                    result['language'] = item[1]
                    result['year'] = year
        return result
