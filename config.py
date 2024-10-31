import os
from dotenv import load_dotenv

load_dotenv()

user = os.environ.get("user")
p = os.environ.get("password")
h = os.environ.get("host")
p = os.environ.get("port")
db = os.environ.get("database")