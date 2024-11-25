import pandas as pd 
from datetime import date
from pymongo import MongoClient
import yaml


def load_data(data, config_path='config/config.yaml'):

    try:
        """Load data into MongoDB."""
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)

        mongo_config = config['mongodb']
        client = MongoClient(f"mongodb://{mongo_config['host']}:{mongo_config['port']}")
        db = client[mongo_config['database']]
        collection = db[mongo_config['collection']]

        collection.insert_many(data.to_dict(orient='records'))
        collection.create_index("FullName")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the MongoDB connection
        client.close()
  
