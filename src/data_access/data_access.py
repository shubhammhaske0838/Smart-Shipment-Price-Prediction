import pandas as pd
import json
import os, sys
from dotenv import load_dotenv
import pymongo


def mongodb_client():

    # Access current directory
    ROOT_DIR = os.getcwd()
    # Create .env file path
    ENV_FILE_PATH = os.path.join(ROOT_DIR, '.env')

    #load .env file
    load_dotenv(dotenv_path = ENV_FILE_PATH)

    # Access username, password and cluster name from .env
    username = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    cluster_name = os.getenv("CLUSTER_LABEL")

    # MongoDB Url
    mongo_db_url = f"mongodb+srv://{username}:{password}@{cluster_name}.mongodb.net/?retryWrites=true&w=majority"
    
    client = pymongo.MongoClient(mongo_db_url)

    return client