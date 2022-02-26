from flask import Flask, render_template
from post import Post
import requests

response = requests.get("https://api.npoint.io/916a0a371a1a2e5d8fdc").json()

objects=[]
for items in response:
    obj = Post(items["id"], items["title"], items["subtitle"], items["body"])
    objects.append(obj)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", my_data=objects)

@app.route("/blog/<int:pid>")
def get_blog(pid):
    requested_post = None
    for dt in objects:
        if dt.id == pid:
            requested_post = dt
    return render_template("blogy.html", mine_data = requested_post)

if __name__== "__main__":
    app.run(port=5500, debug=True)