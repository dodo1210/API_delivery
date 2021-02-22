from flask import Flask
from app.api_delivery import my_application_bp
import os

app = Flask(__name__) 
app.register_blueprint(my_application_bp)


if __name__ == '__main__':
	app.run(debug=True) 
