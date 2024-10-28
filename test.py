from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import ssl

uri = "mongodb+srv://kim:Kimathi2022@cluster0.xxnli.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server with SSL configuration
client = MongoClient(uri, server_api=ServerApi('1'), ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
