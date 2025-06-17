from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    techstack = [
        {
            "section": "Programming Languages",
            "items": [
                {"name": "Python", "img": "Python.svg"},
                {"name": "C#", "img": "C# (CSharp).svg"},
                {"name": "C++", "img": "C++ (CPlusPlus).svg"},
                {"name": "Java", "img": "Java.svg"},
                {"name": "HTML5", "img": "HTML5.svg"},
                {"name": "CSS3", "img": "CSS3.svg"},  # Fixed SVG file
                {"name": "Sass", "img": "Sass.svg"},
            ]
        },
        {
            "section": "Frameworks and Libraries",
            "items": [
                {"name": "React", "img": "React.svg"},
                {"name": "Bootstrap", "img": "Bootstrap.svg"},
                {"name": "Tailwind CSS", "img": "Tailwind CSS.svg"},
                {"name": "Flask", "img": "Flask.svg"},
                {"name": "Django", "img": "Django.svg"},
                {"name": "SQLAlchemy", "img": "SQLAlchemy.svg"},
                {"name": "Selenium", "img": "Selenium.svg"}  # Moved here
            ]
        },
        {
            "section": "Collaboration and Version Control",  # Fixed typo
            "items": [
                {"name": "Git", "img": "Git.svg"},
                {"name": "Slack", "img": "Slack.svg"},        # Fixed SVG
                {"name": "Jira", "img": "Jira.svg"},          # Fixed SVG
                {"name": "DevOps", "img": "Azure.svg"}  # Fixed name/SVG
            ]
        }
    ]

    return render_template("home.html", techstack=techstack)



@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/projects')
def projects():
    return render_template("projects.html")

@views.route('/theme')
def theme():
    return render_template("Theme.html")
