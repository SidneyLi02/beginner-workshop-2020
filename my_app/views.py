from my_app import app
from flask import render_template, request, redirect
import requests

name = "Sidney Li"
facts = {"Birthday":"May 18, 2002", "Favourite colour": "None"}
posts = [{"title":"this is my title", "description": "this is my description"}]


@app.route("/")
def index():
    return render_template("index.html", name=name, facts=facts, posts=facts)

@app.route("/change_name")
def change_name():
    global name
    new_name = request.args.get("name")
    name = new_name
    return redirect("/")

@app.route("/post", method = {"POST"})
def make_post():
    global posts
    post_info = request.get_json()
    posts.append(post_info)
    return redirect("/")