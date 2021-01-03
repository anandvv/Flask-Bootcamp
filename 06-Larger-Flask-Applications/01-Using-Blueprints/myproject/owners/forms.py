from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from myproject import db
from myproject.models import Puppy


class AddForm(FlaskForm):

    puppyList = Puppy.query.all()
    choices = []
    for pup in puppyList:
        if not pup.owner:
            choice = (pup.id, pup.name)
            choices.append(choice)
    name = StringField('Name of Owner:')
    pup_id = IntegerField("Id of Puppy: ")
    puppies = SelectField("Select Puppy", choices=choices)
    submit = SubmitField('Add Owner')


#language = SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
