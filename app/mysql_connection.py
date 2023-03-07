from sqlalchemy  import create_engine  
from urllib.parse import quote_plus
import os

engine_connect = create_engine(f"mysql+pymysql://{os.environ['DB_USER']}:{(quote_plus(os.environ['DB_PASWORD']))}@{os.environ['DB_HOST']}:3000/{os.environ['DB_NAME']}") 

# engine_connect = create_engine(f"mysql+pymysql://root:{quote_plus('Master@123')}@localhost/sampledatabase") 