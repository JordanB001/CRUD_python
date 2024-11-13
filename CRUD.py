from sqlalchemy import inspect, select, text, delete, values
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.persistence import delete_obj


def read(engine, name_of_table, name_of_column):

    with engine.connect() as engine_connected:
        result = engine_connected.execute(select(name_of_column).select_from(text(name_of_table))).fetchone()

        inspector = inspect(engine_connected)
        all_columns = inspector.get_columns(name_of_table)
        column_names = []
        for column in all_columns:
            column_names.append(column["name"])




        print(f"    ".join(column_names) + f"\n---------------------------------------")
        print(f"{result}")

def create(engine, name_of_table: str, columns_and_values: dict):
    columns = ", ".join(columns_and_values.keys())
    values = ', '.join([f"'{column}'" for column in columns_and_values.keys()])

    command = f"INSERT INTO {name_of_table} ({columns}) VALUES ({values})"

    try:
        with engine.connect() as engine_connected:
            with engine_connected.begin():
                result = engine_connected.execute(text(command), columns_and_values)
                if result.rowcount > 0:
                    print("Ligne insérée avec succès.")
                else:
                    print("Aucune ligne n'a été insérée.")
    except SQLAlchemyError as error:
        print(error)

def update(engine):
    pass

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


