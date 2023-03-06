from fastapi import FastAPI
from datetime import date

import os


from sqlalchemy  import create_engine  
from urllib.parse import quote_plus

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

engine_connect = create_engine(f"mysql+pymysql://{os.environ['DB_USER']}:{(quote_plus(os.environ['DB_PASWORD']))}@{os.environ['DB_HOST']}:3000/{os.environ['DB_NAME']}") 
from .apis import *

@app.get('/')
def home_page():
    return "Home Page"

