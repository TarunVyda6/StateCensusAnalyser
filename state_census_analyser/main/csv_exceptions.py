class MainException(Exception):
    pass


class WrongFileType(MainException):
    def __init__(self, message):
        self.message = message


class WrongDelimiterException(MainException):
    def __init__(self, message):
        self.message = message


class FileNotPresent(MainException):
    def __init__(self, message):
        self.message = message


class WrongHeaderException(MainException):
    def __init__(self, message):
        self.message = message
