from flask import Flask
from api_delivery import my_application_bp

app = Flask(__name__) 
app.register_blueprint(my_application_bp)

if __name__ == '__main__':
	app.run(debug=True, port=8080) #run app on port 8080 in debug model
