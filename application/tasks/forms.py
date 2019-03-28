from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=3, max=25)])
    tekoaika = StringField("Tekoaika", [validators.Length(min=1)])
    vaikeusarvio = StringField("Vaikeusarvio", [validators.Length(min=1)])
 
    class Meta:
        csrf = False