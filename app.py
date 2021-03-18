"""This is the main flask app file"""
from flask import Flask, render_template
import names
import pytest
import unittest

app = Flask(__name__)

Nnummber = 10

def generate_names(numberofnames):
    """Generate random names"""
    nlist = []
    for i in range(numberofnames):
        nlist.append(names.get_full_name())
        print(i)

    return nlist

namelist = generate_names(Nnummber)

app = Flask(__name__)

@app.route('/')
def index():
    """Render home page"""
    return render_template("index.html", namelist=namelist)

def test_generate_names():
    assert type(generate_names(Nnummber)) == list
    assert len(generate_names(Nnummber)) == Nnummber