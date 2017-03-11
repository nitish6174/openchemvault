from flask import Blueprint,request,render_template,redirect
import os, json, random , string
from process import processFile

routes_module = Blueprint('routes_module', __name__)
dir_path = "uploads/"


@routes_module.route('/', methods=["GET"])
def homePage():
    if request.method == 'GET':
        return render_template('home.html')


@routes_module.route('/upload', methods=["POST"])
def uploadLogfile():
    if request.method == 'POST':
        logtype = request.form['logtype']
        f = request.files['file']
        new_log_file_name = newLogFileName()
        f.save(new_log_file_name)
        d = processFile(new_log_file_name,logtype)
        os.remove(new_log_file_name)
        return json.dumps(d, sort_keys=True)


def newLogFileName():
    log_file_name = randomString()
    while os.path.isfile(dir_path+log_file_name+".log"):
        log_file_name = randomString()
    return dir_path+log_file_name+".log"


def randomString():
    s = string.ascii_uppercase+string.ascii_lowercase+string.digits
    filekey = ''.join(random.sample(s,20))
    return filekey
