import sys
from flaskapp.app import app
from flaskapp.setup_db import main as init_db

if len(sys.argv) > 3 and sys.argv[1] == '1':
    init_db(sys.argv[3])

debug = False
if len(sys.argv) > 2 and sys.argv[2] == '0':
    debug = True

app.run(host='0.0.0.0', debug=debug)
