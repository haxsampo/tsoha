from flask_wtf import FlaskForm
from wtforms import StringField

class TaskForm(FlaskForm):
    name = StringField("Recipe name") 
    tekoaika = StringField("Tekoaika")
    vaikeusarvio = StringField("Vaikeusarvio")
 
    class Meta:
        csrf = False