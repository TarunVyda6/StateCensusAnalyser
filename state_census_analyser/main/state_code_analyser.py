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
        if not path.endswith(".csv"):
            raise WrongFileType("wrong file extension")
        StateCodeAnalyser.check_for_delimiter(path)
        try:
            with open(path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                value = len(list(csv_reader))
                return value
        except FileNotFoundError:
            logging.debug("invalid file path")
            raise FileNotPresent("invalid file path")
        except Exception:
            raise WrongHeaderException("incorrect header")

    @staticmethod
    def sort_by_state_code(path):
        if not path.endswith(".csv"):
            raise WrongFileType("wrong file extension")
        StateCodeAnalyser.check_for_delimiter(path)
        try:
            with open(path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                census_dictionary = {}
                for row in csv_reader:
                    for column, value in row.items():
                        census_dictionary.setdefault(column, []).append(value)
                return json.dumps(sorted(census_dictionary.get("StateCode")))

        except FileNotFoundError:
            logging.debug("invalid file path")
            raise FileNotPresent("invalid file path")
        except Exception:
            logging.debug("invalid header")
            raise WrongHeaderException("incorrect header")

    @staticmethod
    def check_for_delimiter(path):
        with open(path, newline="") as csv_data:
            try:
                csv.Sniffer().sniff(csv_data.read(), delimiters=",")
            except:
                logging.debug("invalid delimiter")
                raise WrongDelimiterException("invalid delimiter")
