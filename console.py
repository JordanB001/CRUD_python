from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError

from Errors.exceptions import IncorectCommand


def console(engine, command):

    try:
        with engine.connect() as engine_connected:
            with engine.connected.begin():
                engine_connected.execute(text(command))
    except ProgrammingError:
        raise IncorectCommand


