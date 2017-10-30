import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def status():
    return 'Hello World - Bart-Slack !!. I will give you current Bart status.'
