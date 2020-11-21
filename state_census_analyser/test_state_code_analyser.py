import os

import pytest
from state_census_analyser.state_code_analyser import StateCodeAnalyser


@pytest.mark.parametrize('path, result', [("IndiaStateCode - IndiaStateCode.csv", 37),
                                          ("state_census/IndiaStateCode - IndiaStateCode.csv",
                                           "invalid_file_path"),
                                          ("IndiaStateCode - IndiaStateCode.txt", "wrong file extension"),
                                          ])
def test_for_matching_no_of_records(path, result):
    path = os.path.join(os.path.dirname(__file__), path)
    assert StateCodeAnalyser.no_of_states(path) == result
