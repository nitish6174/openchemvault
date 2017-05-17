from flask import Flask, send_from_directory
from flask_compress import Compress
from flask_assets import Environment

import config as config
import shared_variables as var
from assets import getAssets
from routes import routes_module

# Initialize app
app = Flask(__name__)

# Gzip compression
Compress(app)

# App configuration
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = config.static_file_max_age
app.config['UPLOAD_FOLDER'] = "uploads/"

# MongoDB
app.config["MONGO_DBNAME"] = config.mongo_name
var.mongo.init_app(app, config_prefix="MONGO")

# Add assets to app
assets = Environment(app)
assets.register(getAssets())

# Add app routes
app.url_map.strict_slashes = False
app.register_blueprint(routes_module)

# Static XYZ data files
@app.route('/data/<path:filename>')
def loadXYZ(filename):
    return send_from_directory(app.static_folder+"/data_files", filename)


# Click command for setting up database
@app.cli.command()
def setup_db():
    from setup_db_default import main as init_db
    init_db()


# Run the flask server
if __name__ == '__main__':
    #from setup_db_default import main as init_db
    #init_db()
    # from openbabel_test import main as test_ob
    # test_ob()
    app.run(host='0.0.0.0')
