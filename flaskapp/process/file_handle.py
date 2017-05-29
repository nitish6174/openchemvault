import os
import random
import string

# Directory where uploaded files will be saved temporarily
dir_path = "flaskapp/uploads/"


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
