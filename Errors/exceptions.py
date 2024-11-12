class MyAppException(Exception):
    pass

class ErrorTypeOfDatabase(MyAppException):
    def __init__(self, message="This database is not supported", *args):
        super().__init__(message, *args)

class ErrorUsernameOrPassword(MyAppException):
    def __init__(self, message="The username or password is invalid", *args):
        super().__init__(message, *args)

class IncorectCommand(MyAppException):
    def __init__(self, message="The command is invalid", *args):
        super().__init__(message, *args)