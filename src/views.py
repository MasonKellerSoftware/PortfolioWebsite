from flask import Flask, Blueprint, render_template

app = Flask(__name__, template_folder='src')
views = Blueprint('views', __name__, template_folder='src')

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/projects')
def projects():
    return render_template("projects.html")

@views.route('/theme')
def theme():
    return render_template("Theme.html")

app.register_blueprint(views)
