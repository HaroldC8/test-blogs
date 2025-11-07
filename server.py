from flask import Flask, render_template, url_for
from waitress import serve
from markdown import markdown
import json
import os

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

app = Flask(__name__)

blogs = [
    "20251107"
]



@app.route('/')
@app.route('/index')
def index():
    return render_template(
        "index.html",
        blog_pages=blogs
    )

@app.route('/post/<path:path>')
def show_post(path):
    #html = markdown(infile.read())
    path = os.path.join(SITE_ROOT, "static/post_entries/configs", "config_20251107.json")
    data = json.load(open(path))

    return render_template(
        "post.html",
        title="title",
        content=data
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)