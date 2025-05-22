from flask import Flask

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'B2B2J21DB1J21BF3'

    from .views import views

    app.register_blueprint(views, url_prefix='/')
    
    return app