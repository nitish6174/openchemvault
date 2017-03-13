from flask import Flask,request,send_from_directory
from flask_compress import Compress
from flask_assets import Bundle, Environment

from assets import getAssets
from routes import routes_module

app = Flask(__name__)
Compress(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600
app.config['UPLOAD_FOLDER'] = "uploads/"

assets = Environment(app)
assets.register(getAssets())

app.register_blueprint(routes_module)

@app.route('/data/<path:filename>')
def loadXYZ(filename):
    return send_from_directory(app.static_folder+"/data_files", filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
