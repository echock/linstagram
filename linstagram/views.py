# -*- encoding=UTF-8 -*-

from linstagram import app


@app.route('/')
def index():
    return 'Hello'
