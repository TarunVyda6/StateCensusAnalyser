import json
import os

import pytest
from state_census_analyser.main.state_code_analyser import StateCodeAnalyser


@pytest.mark.parametrize('path, result', [("IndiaStateCode - IndiaStateCode.csv", 37),
                                          ("state_census/IndiaStateCode - IndiaStateCode.csv",
                                           "invalid_file_path"),
                                          ("IndiaStateCode - IndiaStateCode.txt", "wrong file extension"),
                                          ])
def test_for_matching_no_of_records(path, result):
    path = os.path.join(os.path.dirname(__file__), path)
    assert StateCodeAnalyser.no_of_states(path) == result


@pytest.mark.parametrize('path, result1, result2',
                         [("IndiaStateCode - IndiaStateCode.csv", "AD", "WB"),
                          ])
def test_for_matching_sort_by_state_code(path, result1, result2):
    path = os.path.join(os.path.dirname(__file__), path)
    json_list = json.loads(StateCodeAnalyser.sort_by_state_code(path))
    print(json_list)
    assert json_list[0] == result1
    assert json_list[36] == result2
