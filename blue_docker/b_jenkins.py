from flask import render_template, Blueprint, redirect, request
import jenkins as jkins
from pprint import pprint

jenkins = Blueprint('jenkins', __name__, url_prefix='/jenkins')


try:
    con = jkins.Jenkins('http://localhost:8080',
                        username='Fabio', password='urias!777')

except Exception as e:
    pprint('Error: {}'.format(e))
    exit()

@jenkins.route('')
def index():
    
    all_jobs = con.get_all_jobs()
    pprint(type(all_jobs))

    return render_template('jenkins.html', jobs=all_jobs)

@jenkins.route('/update/<job>')
def update(job):
    job = con.get_job_name(job)
    return render_template('jenkins_update.html',job=job)

@jenkins.route('/build/<job>')
def build_job(job):
    con.build_job(job)
    return redirect('/jenkins')

@jenkins.route('/reconfig', methods=['POST'])
def reconfig():
    data = request.form
    print(data)
    con.reconfig_job(data['name'], data ['xml'])
    with open ('/home/developer/Documentos/Dashoboards/teste_jenkins.txt', 'w') as e:
        file = e.readlines()
        e.write(file)
    return redirect('/jenkins')