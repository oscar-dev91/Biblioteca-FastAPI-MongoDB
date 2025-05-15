
from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

# URI = os.getenv("URI")
URI = os.environ.get('URI')

# Create a new client and connect to the server
client = AsyncIOMotorClient(URI)
engine = AIOEngine(client=client, database='biblioteca')
"""
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
"""