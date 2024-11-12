from sqlalchemy import inspect, select, text


def read(engine, name_of_table, name_of_column):
    with engine.connect() as engine_connected:
        result = engine_connected.execute(select(name_of_column).select_from(text(name_of_table))).fetchone()

        inspector = inspect(engine_connected)
        all_columns = inspector.get_columns(name_of_table)

        column_names = []
        for column in all_columns:
            column_names.append(column["name"])

        # Afficher les noms des colonnes sur une seule ligne
        print(f"    ".join(column_names) + f"\n---------------------------------------")
        print(f"{result}")