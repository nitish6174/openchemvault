from flask import Flask,request,send_from_directory
from flask_compress import Compress
from flask_assets import Bundle, Environment

from assets import getAssets
from routes import routes_module

app = Flask(__name__)
Compress(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600

assets = Environment(app)
assets.register(getAssets())

app.register_blueprint(routes_module)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
