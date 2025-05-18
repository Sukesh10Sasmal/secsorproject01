#!pip install pymongo
from pymongo import MongoClient
import pandas as pd
import json
from urllib.parse import quote_plus

# Encode special characters in username and password
username = quote_plus("sukesh")
password = quote_plus("Sukesh@2000")

# MongoDB Atlas connection string
uri = f"mongodb+srv://{username}:{password}@cluster0.agcwdat.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to server
client = MongoClient(uri)

# Define database and collection names
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"

# Read and prepare data
df = pd.read_csv("C:\Users\SUKESH\Downloads\sensorproject\notebooks\wafer_23012020_041211.csv")
df = df.drop("Unnamed: 0", axis=1)
json_record = list(json.loads(df.T.to_json()).values())

# Insert into MongoDB
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
