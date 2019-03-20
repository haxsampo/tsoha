from application import app
from flask import render_template, request

@app.route("/reseptit/new")
def reseptit_form():
    return render_template("tasks/new.html")

@app.route("/reseptit/", methods=["POST"])
def reseptit_create():
    print(request.form.get("name"))

    return "hello world!"