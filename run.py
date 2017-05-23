from flaskapp.app import app
from flaskapp.setup_db_default import main as init_db

init_db()
app.run(host='0.0.0.0')
