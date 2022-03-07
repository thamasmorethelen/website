from flask import (render_template)
from models import (app, Project, db)


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/detail/<id>')
def detail(id):
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == '__main__':
    db.create_all()
    app.run()
