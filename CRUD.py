from sqlalchemy import inspect, select, text, delete, values
from sqlalchemy.exc import SQLAlchemyError

def read(engine, list_of_tables, list_of_columns):
    tables = ", ".join(list_of_tables)
    columns = ", ".join(list_of_columns)

    command = f"SELECT {columns} FROM {tables}"

    try:
        with engine.connect() as engine_connected:
            with engine_connected.begin():
                result = engine_connected.execute(text(command)).fetchall()
                return result
    except SQLAlchemyError as error:
        print(error)

def create(engine, name_of_table: str, columns_and_values: dict):
    columns = ", ".join(columns_and_values.keys())
    values = ', '.join([f"'{column}'" for column in columns_and_values.keys()])

    command = f"INSERT INTO {name_of_table} ({columns}) VALUES ({values})"

    try:
        with engine.connect() as engine_connected:
            with engine_connected.begin():
                engine_connected.execute(text(command), columns_and_values)
    except SQLAlchemyError as error:
        print(error)

def update(engine, name_of_table, columns_and_values, condition=""):
    attribution = ", ".join([f"{column} = :{column}" for column in columns_and_values.keys()]) #compréhension de liste
    command = f"UPDATE {name_of_table} SET {attribution}"

    if condition:
        command += f" WHERE {condition}"

    try:
        with engine.connect() as engine_connected:
            with engine_connected.begin():
                engine_connected.execute(text(command), columns_and_values)
    except SQLAlchemyError as error:
        print(error)

def delete(engine, name_of_table, condition=""):
    if condition == "":
        command = f"DELETE FROM {name_of_table}"
    else :
        command = f"DELETE FROM {name_of_table} WHERE {condition};"

    with engine.connect() as engine_connected:
        result = engine_connected.execute(text(command))

        try:
            engine_connected.commit()
        except SQLAlchemyError as error:
            print(f"Error during commit : {error}")


