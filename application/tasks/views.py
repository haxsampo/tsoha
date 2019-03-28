from flask import redirect, render_template, request, url_for
from sqlalchemy import text
from flask_login import login_required

from application import app, db
from application.tasks.models import Task
from application.tasks.forms import TaskForm


@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all())

@app.route("/tasks/new/")
@login_required
def tasks_form():
    return render_template("tasks/new.html", form = TaskForm())


# @app.route("/tasks/<task_id>/", methods=["POST"])
# def tasks_set_done(task_id):

#     t = Task.query.get(task_id)
#     t.tekoaika = 13
#     db.session().commit()
  
#     return redirect(url_for("tasks_index"))


@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    form = TaskForm(request.form)

    if not form.validate():
        return render_template("tasks/new.html", form = form)

    name = request.form.get("name")
    tekoaika = request.form.get("tekoaika")
    vaikeusarvio = request.form.get("vaikeusarvio")
    t = Task(name, tekoaika, vaikeusarvio)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_delete(task_id):

    t = Task.query.get(task_id)
    db.session.delete(t)
    db.session.commit()


    return redirect(url_for("tasks_index"))
    