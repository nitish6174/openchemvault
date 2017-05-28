import os
import random
import string

# Directory where uploaded files will be saved temporarily
dir_path = "flaskapp/uploads/"


# Utility to store uploaded file with a unique random name
def newLogFileName():
    log_file_name = randomString()
    while os.path.isfile(dir_path + log_file_name + ".log"):
        log_file_name = randomString()
    return dir_path + log_file_name + ".log"


# Utility to get a random
def randomString():
    s = string.ascii_uppercase + string.ascii_lowercase + string.digits
    filekey = "".join(random.sample(s, 20))
    return filekey
