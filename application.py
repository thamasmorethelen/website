from flask import (Flask, render_template)
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(application)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Project Name', db.String())
    date = db.Column('Completion Date', db.DateTime())
    description = db.Column('Description', db.Text)
    skills_list = db.Column('Skills', db.String())
    github = db.Column('GitHub Link', db.String())

    def __repr__(self):
        return f'''<Project(Project Title: {self.title},
                Date: {self.date}
                Description: {self.discription},
                Skills List: {self.skills_list},
                Github Link: {self.github})'''


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
    db.create_all()
    application.run()
