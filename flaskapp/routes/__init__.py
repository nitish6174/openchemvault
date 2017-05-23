from flask import Blueprint

routes_module = Blueprint("routes_module", __name__)


# Redirect to non-trailing slash path
@routes_module.before_request
def clear_trailing():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1], code=301)


from flaskapp.routes.api_routes import *
from flaskapp.routes.view_routes import *
