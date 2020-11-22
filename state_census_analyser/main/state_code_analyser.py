import csv
import json
import logging
import os

from state_census_analyser.main.csv_exceptions import *

file = os.path.join(os.path.dirname(__file__), 'census_analyser.log')

logging.basicConfig(filename=file, level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


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

    @staticmethod
    def sort_by_state_code(path):
        try:
            if not path.endswith(".csv"):
                raise WrongFileType("wrong file extension")
        except WrongFileType as e:
            logging.debug(e.message)
            return e.message
        try:
            with open(path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                census_dictionary = {}
                for row in csv_reader:
                    for column, value in row.items():
                        census_dictionary.setdefault(column, []).append(value)
                return json.dumps(sorted(census_dictionary.get("StateCode")))

        except FileNotFoundError:
            logging.debug("invalid_file_path")
            return "invalid_file_path"
