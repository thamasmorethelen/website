from flask import (Flask, render_template)


application = Flask(__name__)


@application.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@application.route('/about')
def about():
    return render_template('about.html')


@application.route('/detail/<id>')
def detail(id):
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project)


@application.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == '__main__':
    application.run()
