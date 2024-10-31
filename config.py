import os
from dotenv import load_dotenv

load_dotenv()

u = os.environ.get("user")
psw = os.environ.get("password")
h = os.environ.get("host")
p = os.environ.get("port")
db = os.environ.get("database")