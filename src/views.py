from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    Tech_images =[
        'Bootstrap.svg',
        'Flask.svg',
        'HTML5.svg',
        'Java.svg',
        'React.svg',
        'Python.svg',
        'SQLAlchemy.svg',
        'C# (CSharp).svg',
        'C++ (CPlusPlus).svg',
        'Selenium.svg',
        'Tailwind CSS.svg',
    ]
    return render_template("home.html", tech_images=Tech_images)

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/projects')
def projects():
    return render_template("projects.html")

@views.route('/theme')
def theme():
    return render_template("Theme.html")
