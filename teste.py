from flask import Flask, Blueprint
import unittest
from api_delivery import my_application_bp
from validacao import Validacao
import flask_restful
import flask_restful.fields
from flask import request
import json

app = Flask(__name__)
app.register_blueprint(my_application_bp)


class HelloWorld(flask_restful.Resource):
    def get(self):
        return {}

class TestCaseDelivery(unittest.TestCase):


    def test_api_delayed_initialization(self):
        api = flask_restful.Api()
        api.init_app(my_application_bp)
        app = Flask(__name__)
        app.register_blueprint(my_application_bp)
        api.add_resource(HelloWorld, '/', endpoint="payload")

    def test_response_ok(self):
    	response = app.test_client().post('/payload',data=json.dumps({"dimensao": {"altura":12,"largura":124},"peso":10}),content_type='application/json')
    	data = json.loads(response.get_data(as_text=True))
    	self.assertEqual(response.status_code,200)

    def test_response_empty(self):
    	response = app.test_client().post('/payload',data=json.dumps({"dimensao": {"altura":2,"largura":124},"peso":10}),content_type='application/json')
    	data = json.loads(response.get_data(as_text=True))
    	self.assertEqual(data,[])

    def test_response_normal(self):
    	response = app.test_client().post('/payload',data=json.dumps({"dimensao": {"altura":102,"largura":40},"peso":400}),content_type='application/json')
    	data = json.loads(response.get_data(as_text=True))
    	self.assertEqual(data,[{"nome":"Entrega Ninja","valor_frete": 12.00,"prazo_dias": 6},{"nome":"Entrega Kabum","valor_frete": 8.00,"prazo_dias": 4}])

    def test_response_ninja(self):
    	response = app.test_client().post('/payload',data=json.dumps({"dimensao": {"altura":152,"largura":50},"peso":400}),content_type='application/json')
    	data = json.loads(response.get_data(as_text=True))
    	self.assertEqual(data,[{"nome":"Entrega Ninja","valor_frete": 12.00,"prazo_dias": 6}])

    def test_response_kabum(self):
    	response = app.test_client().post('/payload',data=json.dumps({"dimensao": {"altura":7,"largura":50},"peso":400}),content_type='application/json')
    	data = json.loads(response.get_data(as_text=True))
    	self.assertEqual(data,[{"nome":"Entrega Kabum","valor_frete": 8.00,"prazo_dias": 4}])

    def test_response_peso_zero(self):
    	response = app.test_client().post('/payload',data=json.dumps({"dimensao": {"altura":7,"largura":50},"peso":0}),content_type='application/json')
    	data = json.loads(response.get_data(as_text=True))
    	self.assertEqual(data,[])


















if __name__ == '__main__':
    unittest.main()