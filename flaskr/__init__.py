import os

from flask import (Flask, g, render_template, flash, redirect, request, session, url_for)
from .make_drink import bar_tend

import sys
print(sys.path)
sys.path.append('./')

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/bar')
    
    def bar():
        flash(bar_tend(g.list1, g.list2, g.list3))
        g.lucky_number = None
        return render_template('base.html')

    @app.route('/enter', methods=('GET', 'POST'))
    def enter():
        if request.method == 'POST':
            g.lucky_number = request.form['Lucky Number']

        return render_template('base.html')

    @app.route('/ingredients')
    def ingredients():
        if not hasattr(g, 'list1'):
            g.list1 = ["double", "your choice", "Rum", "Whiskey", "Wine", "Vodka"]
        if not hasattr(g, 'list2'):
            g.list2 = ["nothing to dilute it", "Coke", "Club soda", "milk", "heavy cream", 
                       "Pineapple juice"]
        if not hasattr(g, 'list3'):
            g.list3 =["whatever evil the person to your right decides", "a dollop of honey", 
                      "salted rim", "a splash of lime juice", "some hot sauce", 
                      "a dash of Venilla"]
        flash(g.list1[2:])
        flash(g.list2[1:])
        flash(g.list3)
        return render_template('ingredients.html')

    return app