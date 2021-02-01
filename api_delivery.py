from flask import Flask, jsonify, request
app = Flask(__name__) 


def weight_most_zero(weight):
	if weight<=0:
		return []
	return weight

def min_max(height,width):
	print(height,width)
	if height < 5 or height> 200 or width<6 or width>140:
		return 0
	if height>=5 and height<10:
		return 1
	if (width>=6 and width<=13) or (width>=125 and width<=140) or (height>=140 and height<=200):
		return 2


@app.route('/payload', methods=['POST'])
def payload():
	size = request.json['dimensao']
	if weight_most_zero(request.json['peso']) == []:
		return jsonify([])
	if min_max((jsonify(size).json['altura']),(jsonify(size).json['largura'])) == 0:
		return jsonify([])
	if min_max((jsonify(size).json['altura']),(jsonify(size).json['largura'])) == 2:
		return jsonify({"nome":"Entrega Ninja","valor_frete": (request.json['peso']*0.3)/10,"prazo_dias": 6})
	if min_max((jsonify(size).json['altura']),(jsonify(size).json['largura'])) == 1:
		return jsonify({"nome":"Entrega Especial","valor_frete": (request.json['peso']*0.2)/10,"prazo_dias": 4})	

	delivery = {"nome":"Entrega Ninja","valor_frete": (request.json['peso']*0.3)/10,"prazo_dias": 6},{"nome":"Entrega Especial","valor_frete": (request.json['peso']*0.2)/10,"prazo_dias": 4}
	return jsonify(delivery)


if __name__ == '__main__':
	app.run(debug=True, port=8080) #run app on port 8080 in debug model

#size = request.json['dimensao']
#height = (jsonify(size).json['altura'])
#width = (jsonify(size).json['largura'])
	