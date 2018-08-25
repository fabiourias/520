#!/usr/bin/python3

from flask import Flask, render_template, Blueprint, redirect
from docker import DockerClient

b_docker = Blueprint('docker', __name__, url_prefix='/docker')

con = DockerClient('tcp://192.168.0.200:2376')

@b_docker.route('')
def index():
    containers = con.containers.list(all=True)
    #containers = con.containers.get('6d457534379f')
    return render_template('docker.html', containers=containers)

@b_docker.route('/start/<shortid>')
def start_container(shortid):
    container = con.containers.get(shortid)
    container.start()
    return redirect('/docker')

@b_docker.route('/stop/<shortid>')
def stop_container(shortid):
    container = con.containers.get(shortid)
    container.stop()
    return redirect('/docker')