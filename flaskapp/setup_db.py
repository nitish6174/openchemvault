import os

from pymongo import MongoClient

import flaskapp.config as config
from flaskapp.process.doc_entry_handle import add_file_to_database

# Database configuration
db_host = config.mongo_host
db_port = config.mongo_port
db_name = config.mongo_name
db_user = config.mongo_user
db_pass = config.mongo_pass
# Data folder path
default_data_folder_path = config.data_folder


def main(data_folder_path=default_data_folder_path):
    try:
        db_conn = MongoClient(db_host, int(db_port))
        db = db_conn[db_name]
        if db_user != "":
            db.authenticate(db_user, db_pass)
        if data_folder_path != "" and os.path.isdir(data_folder_path):
            db_conn.drop_database(db_name)
            iterate(db, data_folder_path)
            print("\nDone!")
            print("-" * 50)
        else:
            print("This folder was not found")
    except Exception as e:
        print("\nCannot setup database")
        print("-" * 50)
        print(e.message)
        print("-" * 50)


# Recursively iterate through files in a directory
def iterate(db, dir_path):
    if not(dir_path.endswith("/")):
        dir_path = dir_path + "/"
    for file_name in os.listdir(dir_path):
        f = dir_path + file_name
        if os.path.isfile(f):
            add_file_to_database(db, f, True)
        elif os.path.isdir(f):
            iterate(db, f)
