import os
from json import dumps

from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap

from vendfinder.viewmodels.vendfinderviewmodel import VendFinderViewModel
import vendfinder

class VendFinderView(object):
    def __init__(self):
        self.view_model = VendFinderViewModel()

        tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
        self.app = Flask('VendFinder', template_folder=tmpl_dir)
        Bootstrap(self.app)

        @self.app.route('/<user>/get_vendors')
        def get_vendors(user):
            return dumps(self.view_model.get_vendors(user))

        @self.app.route('/<user>/edit', methods=['GET', 'POST'])
        def edit(user):
            if (request.method == 'POST'):
                self.view_model.save_config(user, request.form['config'])
                return redirect(url_for('index', user=user))

            return render_template('edit.html', user=user)

        @self.app.route('/<user>/get_config')
        def get_config(user):
            return dumps(self.view_model.get_config(user))

        @self.app.route('/<user>')
        def index(user):
            return render_template('index.html', user=user)

        @self.app.route('/')
        def nouser():
            return redirect(url_for('index', user='default'))
