import os

import pytest
from state_census_analyser.state_census_analyser import StateCensusAnalyser


@pytest.mark.parametrize('path, result', [("IndiaStateCensusData - IndiaStateCensusData.csv", 29),
                                          ("state_census/IndiaStateCensusData - IndiaStateCensusData.csv",
                                           "invalid_file_path"),
                                          ("IndiaStateCensusData - IndiaStateCensusData.txt", "wrong file extension"),
                                          ])
def test_for_matching_no_of_records(path, result):
    path = os.path.join(os.path.dirname(__file__), path)
    assert StateCensusAnalyser.no_of_states(path) == result
