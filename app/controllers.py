from flask import request, redirect, url_for
from .models import db, ExampleModel

def add_example(name):
    new_example = ExampleModel(name=name)
    db.session.add(new_example)
    db.session.commit()

def get_all_examples():
    return ExampleModel.query.all()
