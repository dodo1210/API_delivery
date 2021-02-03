from flask import Flask, jsonify, request, Blueprint
from validacao import Validacao

my_application_bp = Blueprint('my_application',__name__)

@my_application_bp.route('/payload', methods=['POST'])
def payload():
	v = Validacao()
	size = request.json['dimensao']
	if v.weight_most_zero(request.json['peso']) == []:
		return jsonify([])
	if v.min_max((jsonify(size).json['altura']),(jsonify(size).json['largura'])) == 0:
		return jsonify([])
	if v.min_max((jsonify(size).json['altura']),(jsonify(size).json['largura'])) == 2:
		return jsonify({"nome":"Entrega Ninja","valor_frete": (request.json['peso']*0.3)/10,"prazo_dias": 6})
	if v.min_max((jsonify(size).json['altura']),(jsonify(size).json['largura'])) == 1:
		return jsonify({"nome":"Entrega Especial","valor_frete": (request.json['peso']*0.2)/10,"prazo_dias": 4})	

	delivery = {"nome":"Entrega Ninja","valor_frete": (request.json['peso']*0.3)/10,"prazo_dias": 6},{"nome":"Entrega Especial","valor_frete": (request.json['peso']*0.2)/10,"prazo_dias": 4}
	return jsonify(delivery)



