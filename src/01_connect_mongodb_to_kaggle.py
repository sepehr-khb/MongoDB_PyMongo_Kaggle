# ▶ Install PyMongo¶
'''
To connect to MongoDB Atlas using a URI, we need to install pymongo[srv] instead of pymongo.
'''
pip install pymongo[srv]
---

# 🗃 Import Library¶
import pymongo
from pymongo import MongoClient
from urllib.parse import quote_plus # To Encoding
from IPython.core.display import display, HTML
---


# 💎 Connect MongoDB to Kaggle
'''
To connect Kaggle to MongoDB, I prefer using the recommended solution MongoDB Atlas. This is the popular free solution offered by MongoDB. Additionally, we must remember to encode the password using the quote_plus function. The connection steps outlined in the introduction and this section provide the necessary coding.
'''
username = "sepehrkhalilib"
password = quote_plus("SK13579")  # Use quote_plus to encoding password
cluster = "cluster0.kfxz3.mongodb.net"

uri = f"mongodb+srv://{username}:{password}@{cluster}/?appName=Cluster0" # The URI generated in MongoDB Atlas. 

# - Connect to the server and Create a new client
client = MongoClient(uri)

# - Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("✅ Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)