# -*- coding: utf-8 -*-
from flask import request, redirect, url_for

from .models import USERNAME, SKILLS
from .views import UserView


class UserController:
    def __init__(self):
        self.model = None
        self.view = UserView()

    def index(self):
        return self.view.render(USERNAME, SKILLS)

    def contact(self):
        if request.method == 'GET':
            return self.view.render_contact()

        if request.method == 'POST':
            email = request.form['email']
            full_name = request.form['full_name']
            whatsapp = request.form['whatsapp']
            message = request.form['message']

            print(email, full_name, whatsapp, message)

            return redirect(url_for('home'))
