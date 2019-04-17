from flask import Flask, render_template,url_for
from flaskext.markdown import Markdown
import pandas as pd;
app=Flask(__name__)
############# Make Sure root folder is webapp ################
##set FLASK_APP=qbviz.py
##set FLASK_DEBUG=1
##flask run




@app.route("/")
@app.route("/home")
def home():
    tableau_api = open('static/js/tableau-2.min.js')
    return render_template('home.html',title='Home',tab_abi=tableau_api)


@app.route("/proposal")
def proposal():
    prop_file = open('static/text/proposal.md','r').read()
    return render_template('proposal.html',prop=prop_file)


Markdown(app)
