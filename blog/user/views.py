# -*- coding: utf-8 -*-
from flask import render_template


class UserView(object):
    def __init__(self):
        self.template = 'user/home.html'

    def language_list(self, languages):
        li = ''
        for language in languages:
            li += '<li class ="list-group-item" >' + language + '</li>'
        return li

    def username_line(self, username):
        return '<h3>' + username + '</h3>'

    def render_contact(self):
        return render_template('user/contact.html')

    def render(self, username, skills):
        context = {
            'username': self.username_line(username),
            'skills': self.language_list(skills)
        }
        return render_template(self.template, **context)
