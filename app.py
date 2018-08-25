#!/usr/bin/python3
from flask import Flask, render_template
from blue_docker.b_docker import b_docker
from blue_docker.b_jenkins import jenkins

app = Flask(__name__)
app.register_blueprint(b_docker)
app.register_blueprint(jenkins)

@app.route('/')
def index():

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5000, debug=True)