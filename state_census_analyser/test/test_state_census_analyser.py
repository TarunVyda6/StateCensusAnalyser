import os
import json
import pytest
from state_census_analyser.main.state_census_analyse import *


@pytest.mark.parametrize('path, result', [("IndiaStateCensusData - IndiaStateCensusData.csv", 29),
                                          ("state_census/IndiaStateCensusData - IndiaStateCensusData.csv",
                                           "invalid_file_path"),
                                          ("IndiaStateCensusData - IndiaStateCensusData.txt", "wrong file extension"),
                                          ])
def test_for_matching_no_of_records(path, result):
    path = os.path.join(os.path.dirname(__file__), path)
    assert StateCensusAnalyser().no_of_states(path) == result


@pytest.mark.parametrize('path, result1, result2',
                         [("IndiaStateCensusData - IndiaStateCensusData.csv", "Andhra Pradesh", "West Bengal"),
                          ])
def test_for_matching_sort_by_states(path, result1, result2):
    path = os.path.join(os.path.dirname(__file__), path)
    json_list = json.loads(StateCensusAnalyser.sort_by_state(path))
    assert json_list[0] == result1
    assert json_list[28] == result2


