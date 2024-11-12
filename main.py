from os import getenv
from dotenv import load_dotenv

from sqlalchemy import *

from connect_to_DB import connect_to_database
from CRUD import read
from console import console

load_dotenv()
DRIVER_DB = getenv("DIALECT_DB")
USERNAME_DB = getenv("USERNAME_DB")
PASSWORD_DB = getenv("PASSWORD_DB")
HOST_DB = getenv("HOST_DB")
NAME_OF_DB = getenv("NAME_OF_DATABASE")

if __name__ == "__main__":

    # Connect to Database
    engine = connect_to_database(type_of_DB="postgres" ,username=USERNAME_DB, password=PASSWORD_DB,
                                    host=HOST_DB, name_of_database=NAME_OF_DB)

    read(engine, "utilisateur", name_of_column="*")
