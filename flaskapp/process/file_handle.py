import os
import random
import string
from flaskapp.process.chem_process import parse_file

# Directory where uploaded files will be saved temporarily
dir_path = "flaskapp/uploads/"


# Temporarily save uploaded file, parse it and return data
def process_uploaded_file(f):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    new_log_file_name = make_new_file_name()
    f.save(new_log_file_name)
    d = parse_file(new_log_file_name)
    os.remove(new_log_file_name)
    return d


# Utility to store uploaded file with a unique random name
def make_new_file_name():
    log_file_name = get_random_string()
    while os.path.isfile(dir_path + log_file_name + ".log"):
        log_file_name = get_random_string()
    return dir_path + log_file_name + ".log"


# Utility to get a random
def get_random_string():
    s = string.ascii_uppercase + string.ascii_lowercase + string.digits
    filekey = "".join(random.sample(s, 20))
    return filekey
