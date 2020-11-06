# -*- coding: utf-8 -*-

from flask import render_template


class UserView(object):
    def __init__(self):
        self.template = 'user/home.html'

    def language_list(self, languages):
        li = ''
        for language in languages:
            li += '<li class ="list-group-item" >%s</li>' % (language)
        return li

    def username_line(self, username):
        return '<h3>%s</h3>' % (username)

    def render(self, username,languages):
        context = {
            'username': self.username_line(username),
            'languages': self.language_list(languages)
        }
        return render_template(self.template, **context)
