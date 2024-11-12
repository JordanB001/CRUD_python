from sqlalchemy import create_engine, text

from sqlalchemy.exc import OperationalError
from Errors.exceptions import ErrorTypeOfDatabase, ErrorUsernameOrPassword


def connect_to_database(type_of_DB: str, driver="", username="", password="", host="localhost", port="",
                        name_of_database="", past_to_file=""):

    postgreSQL_default = {"dialect" : "postgresql", "driver" : "psycopg2", "port" : "5432"}
    mySQL_default = {"dialect" : "mysql", "driver" : "pymysql", "port" : "3306"}
    SQLite_default = {"dialect" : "sqlite"}
    microsoft_SQL_Server_default = {"dialect" : "mssql", "driver" : "pyodbc", "port" : "1433"}
    oracle_default = {"dialect" : "oracle", "driver" : "cx_oracle", "port" : "1521"}
    mariaDB_default = {"dialect" : "mariadb", "driver" : "mariadb", "port" : "3306"}
    amazon_redshift_default = {"dialect" : "redshift", "driver" : "psycopg2", "port" : "5439"}
    cockroachDB_default = {"dialect" : "cockroachdb", "driver" : "psycopg2", "port" : "26527"}

    list_db = [postgreSQL_default, mySQL_default, SQLite_default, microsoft_SQL_Server_default, oracle_default, mariaDB_default, amazon_redshift_default, cockroachDB_default]
    list_id: int

    dialect = ""

    match type_of_DB.lower():
        case "postgresql" | "postgres":
            list_id = 0
        case "mysql":
            list_id = 1
        case "sqlite" | "sql_lite":
            dialect = "sqlite"
        case "microsoftsqlserver" | "microsoft_sql_server" | "microsoft sql server":
            list_id = 3
        case "oracle" | "oracle sql" | "oracle_sql":
            list_id = 4
        case "mariadb" | "maria_db" | "maria db":
            list_id = 5
        case "redshift" | "amazon" | "amazon_redshift" | "amazon redshift":
            list_id = 6
        case "cockroachdb" | "cockroach" | "cockroach db" | "cockroach_db":
            list_id = 7
        case _:
            raise ErrorTypeOfDatabase

    if dialect == "sqlite":
        url_database = f"sqlite:///{past_to_file}"
    else:
        dialect = list_db[list_id]["dialect"]
        if driver == "":
            driver = "+" + list_db[list_id]["driver"]
        else:
            driver = "+" + driver.lower()
        if port == "":
            port = list_db[list_id]["port"]

        url_database = f"{dialect}{driver}://{username}:{password}@{host}:{port}/{name_of_database}"

    engine = create_engine(url_database)
    return engine











