from flask import Flask, jsonify, make_response, Response
import json
from blueprints.usuarios import usuario

app = Flask(__name__)
app.register_blueprint(usuario)

@app.route('/teste', methods=['GET'])
def hello ():
    #headers = {"content-type":"application/json"}
    retorno = json.dumps({ "massage":"resposta usando make_response"})
    return Response(retorno, 777, content_type="application/json")

@app.route('/nomes')
def render_nomes():
    with open('nomes', 'r' ) as arq:
        retorno = {'nomes': [x.replace('\n', '') for x in arq.readlines()]}
        return jsonify(retorno)
    
if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5000, debug=True)

'''
exit()
# MakeResponse - manipula o status 
from flask import Flask, jsonify, make_response
import json
app = Flask(__name__)

@app.route('/teste', methods=['GET'])
def hello ():
    headers = {"content-type":"application/json"}
    retorno = json.dumps({ "massage":"resposta usando make_response"})
    return make_response(retorno, 200, headers)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5000, debug=True)

'''