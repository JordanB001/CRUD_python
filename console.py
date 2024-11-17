from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError

from Errors.exceptions import IncorectCommand


def console(engine, command):
    list_no_transaction = ["CREATE DATABASE", "DROP DATABASE", "BEGIN", "COMMIT", "ROLLBACK", "SET TRANSACTION",
                           "SAVEPOINT", "RELEASE SAVEPOINT", "VACUUM", "CLUSTER", "REINDEX DATABASE", "REINDEX SYSTEM",
                           "ANALYZE", "CREATE USER", "CREATE ROLE", "ALTER SYSTEM", ]

    if any(no_transaction in command.upper() for no_transaction in list_no_transaction):
        #command with no transaction
        try:
            with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as engine_connected:
                print(f"Command SQL : {text(command)}")
                result = engine_connected.execute(text(command))

                if result.returns_rows:
                    return result.fetchall()
                else:
                    return "Command execute successfully"

        except Exception as error:
            print(error)

    else:
        #command with transaction
        try:
            with engine.connect() as engine_connected:
                with engine_connected.begin():
                    print(f"Command SQL : {text(command)}")
                    result = engine_connected.execute(text(command))
                    return result
        except ProgrammingError:
            raise IncorectCommand


