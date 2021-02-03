from flask import Flask, jsonify, request, Blueprint
my_application_bp = Blueprint('my_application',__name__)

@my_application_bp.route('/payload', methods=['POST'])
def payload():
	v = Validacao()
	size = request.json['dimensao']
	if request.json['peso'] <= 0:
		return jsonify([])
		height < 5 or height> 200 or width<6 or width>140
	if jsonify(size).json['altura']<5 or jsonify(size).json['altura']>140 or jsonify(size).json['largura'] < 6 or jsonify(size).json['largura'] > 200:
		return jsonify([])
	if  (jsonify(size).json['largura']>=6 and jsonify(size).json['largura']<=13) or (jsonify(size).json['largura']>=125 and jsonify(size).json['largura']<=140) or (jsonify(size).json['altura']>=140 and jsonify(size).json['altura']<=200):
		return jsonify({"nome":"Entrega Ninja","valor_frete": (request.json['peso']*0.3)/10,"prazo_dias": 6})
	if (jsonify(size).json['altura']>=5 and jsonify(size).json['altura']<10):
		return jsonify({"nome":"Entrega Especial","valor_frete": (request.json['peso']*0.2)/10,"prazo_dias": 4})	

	delivery = {"nome":"Entrega Ninja","valor_frete": (request.json['peso']*0.3)/10,"prazo_dias": 6},{"nome":"Entrega Especial","valor_frete": (request.json['peso']*0.2)/10,"prazo_dias": 4}
	return jsonify(delivery)



