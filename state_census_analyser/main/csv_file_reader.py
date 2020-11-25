import csv
import logging
from state_census_analyser.main.csv_exceptions import *


class CSVFileReader:
    @staticmethod
    def check_for_delimiter(path):
        """
        takes path as input and checks for delimiter exception
        :rtype: raises exception if occured
        """
        with open(path, newline="") as csv_data:
            try:
                csv.Sniffer().sniff(csv_data.read(), delimiters=",")
            except Exception:
                logging.debug("invalid delimiter")
                raise WrongDelimiterException("invalid delimter")

    @staticmethod
    def check_for_header(path):
        """
        takes path as input and checks for header exception
        :rtype: raises exception if occured
        """
        with open(path, mode='r', newline='') as csv_file:
            if not csv.Sniffer().has_header(csv_file.read()):
                raise WrongHeaderException("incorrect header")

    @staticmethod
    def load_csv_file(path):
        """
        takes path as input and load csv file and returns list of dictionaries and raises exception if occured
        :rtype: returns list of dictionaries and raises exception if occured
        """
        if not path.endswith(".csv"):
            logging.debug("Wrong file extension")
            raise WrongFileType("wrong file extension")

        try:
            with open(path, mode='r', newline='') as csv_file:
                CSVFileReader.check_for_delimiter(path)
                CSVFileReader.check_for_header(path)
                csv_reader = csv.DictReader(csv_file, delimiter=',')
                census_list = []
                for row in csv_reader:
                    census_dictionary = {}
                    for key in row:
                        census_dictionary[key] = row.get(key)
                    census_list.append(census_dictionary)
                return census_list
        except FileNotFoundError:
            logging.debug("invalid file path")
            raise FileNotPresent("invalid file path")
