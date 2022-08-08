from flask import Flask
import re

app=secret_key="secretkey"
app=Flask(__name__)

DATABASE = "recipes_db"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 