import json
import logging
import os
from state_census_analyser.main.csv_file_reader import *

file = os.path.join(os.path.dirname(__file__), 'census_analyser.log')
logging.basicConfig(filename=file, level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class StateCensusAnalyser:

    @staticmethod
    def no_of_states(path):
        """
        takes csv file path as input and load the csv data and return number of states
        :param path: takes csv file path as param
        :return: number of states
        """
        census_list = CSVFileReader.load_csv_file(path)
        return len(census_list)

    @staticmethod
    def sort_by_state(path):
        """
        takes csv file path as input and load the csv data and return list of data sorted by state in json format
        :param path: takes csv file path as param
        :return: list of csv state code analyser data in sorted order by state
        """
        census_list = CSVFileReader.load_csv_file(path)
        sorted_list = sorted(census_list, key=lambda x: x.get("State"), reverse=False)
        return json.dumps(sorted_list)

    @staticmethod
    def sort_by_state_population_descending(path):
        """
        takes csv file path as input and load the csv data and return list of data sorted by state population in json format
        :param path: takes csv file path as param
        :return: list of csv state code analyser data in sorted order by state population
        """
        census_list = CSVFileReader.load_csv_file(path)
        sorted_list = sorted(census_list, key=lambda x: int(x.get("Population")), reverse=True)
        return json.dumps(sorted_list)
