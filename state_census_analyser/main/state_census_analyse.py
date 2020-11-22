import csv
import logging
import os
from state_census_analyser.main.csv_exceptions import *
import json

file = os.path.join(os.path.dirname(__file__), 'census_analyser.log')

logging.basicConfig(filename=file, level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class StateCensusAnalyser:

    @staticmethod
    def no_of_states(path):
        if not path.endswith(".csv"):
            logging.debug("wrong file extension")
            raise WrongFileType("wrong file extension")
        try:
            with open(path, mode='r', newline="") as csv_file:
                StateCensusAnalyser.check_for_delimiter(path)
                csv_reader = csv.DictReader(csv_file)
                value = len(list(csv_reader))
                logging.debug(value)
                return value
        except FileNotFoundError:
            logging.debug("Wrong file path")
            raise FileNotPresent("Wrong file path")
        except KeyError:
            logging.debug("incorrect header")
            raise WrongHeaderException("incorrect header")

    @staticmethod
    def sort_by_state(path):
        if not path.endswith(".csv"):
            logging.debug("Wrong file extension")
            raise WrongFileType("wrong file extension")
        try:
            with open(path, mode='r') as csv_file:
                StateCensusAnalyser.check_for_delimiter(path)
                csv_reader = csv.DictReader(csv_file)
                census_dictionary = {}
                for row in csv_reader:
                    for column, value in row.items():
                        census_dictionary.setdefault(column, []).append(value)
                return json.dumps(sorted(census_dictionary.get("State")))

        except FileNotFoundError:
            logging.debug("invalid file path")
            raise FileNotPresent("invalid file path")
        except Exception:
            raise WrongHeaderException("incorrect header")

    @staticmethod
    def check_for_delimiter(path):
        with open(path, newline="") as csv_data:
            try:
                csv.Sniffer().sniff(csv_data.read(), delimiters=",")
            except:
                logging.debug("invalid delimiter")
                raise WrongDelimiterException("invalid delimter")
