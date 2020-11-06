# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from .views import UserView
from .models import USERNAME, SKILLS


class UserController:
    def __init__(self):
        self.model = None
        self.view = UserView()

    def index(self):
        return self.view.render(username=USERNAME, languages=SKILLS)

    def contact(self):
        if request.method == 'GET':
            return render_template('user/contact.html')

        if request.method == 'POST':
            email = request.form['email']
            full_name = request.form['full_name']
            whatsapp = request.form['whatsapp']
            message = request.form['message']
            print(email, full_name, whatsapp, message)
            return redirect(url_for('home'))
