import json
import logging
import os
from state_census_analyser.main.csv_file_reader import CSVFileReader

file = os.path.join(os.path.dirname(__file__), 'census_analyser.log')
logging.basicConfig(filename=file, level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class StateCodeAnalyser:
    @staticmethod
    def no_of_states(path):
        """
        takes csv file path as input and loads the data from csv file and returns number of states
        :rtype: number of states
        """
        census_list = CSVFileReader.load_csv_file(path)
        return len(census_list)

    @staticmethod
    def sort_by_state_code(path):
        """
        takes csv file path as input and load the csv data and return list of data sorted by state code in json format
        :param path: takes csv file path as param
        :return: list of csv state code analyser data in sorted order by state code
        """
        census_list = CSVFileReader.load_csv_file(path)
        sorted_list = sorted(census_list, key=lambda x: x.get("StateCode"))
        return json.dumps(sorted_list)
