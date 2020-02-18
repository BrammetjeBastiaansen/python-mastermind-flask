from app import app
from flask import Flask
from flask import render_template


@app.route('/')
def index():
    return "Test Page :ED"
