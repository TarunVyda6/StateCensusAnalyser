import csv

from state_census_analyser.csv_exceptions import WrongFileType


class StateCodeAnalyser:
    @staticmethod
    def no_of_states(path):
        try:
            if not path.endswith(".csv"):
                raise WrongFileType("wrong file extension")
        except WrongFileType as e:
            return e.message
        try:
            with open(path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                value = len(list(csv_reader))
                return value
        except FileNotFoundError:
            return "invalid_file_path"
