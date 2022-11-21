from flask import render_template, Blueprint, request, redirect, url_for
from webpersonal.project.models import Project

from webpersonal import db

project = Blueprint('project', __name__)

@project.route('/project/')
@project.route('/project/index')
def index():
   projects = Project.query.all()
   db.session.commit()
   return render_template('project/index.html', projects = projects)
   #return 'cargar modelo'

@project.route('/project/crear')
def crear():
    return render_template('project/crear.html')

@project.route('/project/insertar', methods=['POST'])
def insertar():
    titulo = request.form.get('titulo')
    descripcion = request.form.get('descripcion')

    project = Project(titulo, descripcion)

    db.session.add(project)
    db.session.commit()

    return redirect(url_for('project.index'))
   
@project.route('/project/editar/<int:id>')
def editar(id):
    project = Project.query.get_or_404(id)
    return render_template('project/editar.html', project=project)

@project.route('/project/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    project = Project.query.get_or_404(id)
    project.titulo = request.form.get('titulo')
    project.descripcion = request.form.get('descripcion')

    db.session.add(project)
    db.session.commit()

    return redirect(url_for('project.index'))

@project.route('/project/eliminar/<int:id>')
def eliminar(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()

    return redirect(url_for('project.index'))




