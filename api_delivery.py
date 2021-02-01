from flask import Flask, jsonify, request
app = Flask(__name__) 

deliveries = []

@app.route('/payload', methods=['POST'])
def payload():

	weight = request.json['peso']

	delivery = {
        "nome":"Entrega Ninja",
    	"valor_frete": (weight*0.3)/10,
    	"prazo_dias": 6
	},{
        "nome":"Entrega Especial",
    	"valor_frete": (weight*0.2)/10,
    	"prazo_dias": 4
	}
	return jsonify({'dimensão':delivery})

if __name__ == '__main__':
	app.run(debug=True, port=8080) 

#size = request.json['dimensao']
#height = (jsonify(size).json['altura'])
#width = (jsonify(size).json['largura'])
	