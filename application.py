from flask import (Flask, render_template)


application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/about')
def about():
    return render_template('about.html')


@application.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == '__main__':
    application.run()
