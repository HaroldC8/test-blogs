from flask import Flask, render_template, url_for
from waitress import serve
from markdown import markdown
from post_urls import POST_URLS
import json
import os

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
SITE_JSON = os.path.join(SITE_ROOT, "static/post_entries/configs")
SITE_POSTS = os.path.join(SITE_ROOT, "static/post_entries/posts")

app = Flask(__name__)

post_data = []
for url in POST_URLS:
    json_url = os.path.join(SITE_JSON, "config_"+ url  + ".json")
    json_data = json.load(open(json_url))
    post_data.append([url, json_data["title"]])

@app.route('/')
@app.route('/index')
def index():
    return render_template(
        "index.html",
        pages=post_data
    )

@app.route('/post/<path:path>')
def show_post(path):
    if(path not in POST_URLS):
        return "Too bad. Post not found." # TODO
    
    #html = markdown(infile.read())
    json_url = os.path.join(SITE_JSON, "config_"+ path  + ".json")
    json_data = json.load(open(json_url))
    post_url = os.path.join(SITE_POSTS, "post_"+ path  + ".md")
    post_data = markdown(open(post_url).read())

    return render_template(
        "post.html",
        title=json_data["title"],
        content=post_data
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)