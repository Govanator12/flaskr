from app import app
from flask import render_template, jsonify, request
import requests


@app.route('/')
@app.route('/index')
def index():
    pass
