import pandas as pd
import pymongo
import json
from pymongo.mongo_client import MongoClient
import os, sys
from schema import write_schema_yaml
from src.data_access.data_access import mongodb_client

# url = "mongodb+srv://<username>:<password>@cluster0.jpr9cyx.mongodb.net/?retryWrites=true&w=majority"

# DATA_FILE_PATH = r"C:\Python\End to End Project\New Series\Smart-Shipment-Price-Prediction\data\train.csv"
DATABASE = 'Machine_Learning'
COLLECTION_NAME = 'DATASET'

if __name__ == '__main__':

    ROOT_DIR = os.getcwd()
    DATA_FILE_PATH = os.path.join(ROOT_DIR, 'data','train.csv')

    FILE_PATH = os.path.join(ROOT_DIR, DATA_FILE_PATH)

    write_schema_yaml(csv_file = DATA_FILE_PATH)
    
    # Read data from CSV file into a Pandas Dataframe
    df = pd.read_csv(DATA_FILE_PATH)
    print(f'Rows and Columns: {df.shape}')

    # Convert the DataFrame to a list of dictionaries (JSON records)
    json_records = json.loads (df.to_json(orient = 'records'))
    print(json_records[0])

    # Establish a connection to MongoDB
    # client = pymongo.MongoClient(url)
    client = mongodb_client()

    # Access the desired database and collection
    db = client[DATABASE]
    collection = db[COLLECTION_NAME]

    # Insert the JSON records into the collection 
    collection.insert_many(json_records)

    # Close the MongoDB connection
    client.close()

