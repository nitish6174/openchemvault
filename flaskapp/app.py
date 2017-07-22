from flask import Flask, send_from_directory
from flask_compress import Compress
from flask_assets import Environment

import flaskapp.config as config
import flaskapp.shared_variables as var
from flaskapp.assets import get_assets
from flaskapp.routes import routes_module

# Initialize app
app = Flask(__name__)

# Gzip compression
Compress(app)

# App configuration
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = config.static_file_max_age
app.config['UPLOAD_FOLDER'] = "uploads/"

# MongoDB
app.config["MONGO_HOST"] = config.mongo_host
app.config["MONGO_PORT"] = config.mongo_port
app.config["MONGO_DBNAME"] = config.mongo_name
var.mongo.init_app(app, config_prefix="MONGO")

# Add assets to app
assets = Environment(app)
assets.register(get_assets())

# Add app routes
app.url_map.strict_slashes = False
app.register_blueprint(routes_module)


# Static XYZ data files
@app.route('/data/<path:filename>')
def loadXYZ(filename):
    return send_from_directory(app.static_folder + "/data_files", filename)
