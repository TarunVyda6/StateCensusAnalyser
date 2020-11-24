import json
import os

import pytest
from state_census_analyser.main.state_code_analyser import StateCodeAnalyser
from state_census_analyser.main.csv_exceptions import *


@pytest.mark.parametrize('path, result', [("IndiaStateCode - IndiaStateCode.csv", 37)])
def test_for_matching_no_of_records(path, result):
    path = os.path.join(os.path.dirname(__file__), path)
    assert StateCodeAnalyser.no_of_states(path) == result


@pytest.mark.parametrize('path, result1, result2',
                         [("IndiaStateCode - IndiaStateCode.csv", "AD", "WB"),
                          ])
def test_for_matching_sort_by_state_code(path, result1, result2):
    path = os.path.join(os.path.dirname(__file__), path)
    json_list = json.loads(StateCodeAnalyser.sort_by_state_code(path))
    assert json_list[0].get("StateCode") == result1
    assert json_list[len(json_list) - 1].get("StateCode") == result2


@pytest.mark.parametrize('path, result', [("IndiaStateCode - IndiaStateCode.txt", WrongFileType),
                                          ("IndiaStateCode - IndiaStateCode - DelimiterWrong.csv",
                                           WrongDelimiterException),
                                          ("IndiaCode - IndiaStateCode.csv", FileNotPresent),
                                          ("IndiaStateCode - IndiaStateCode - HeaderWrong.csv", WrongHeaderException)])
def test_for_matching_exceptions(path, result):
    path = os.path.join(os.path.dirname(__file__), path)
    with pytest.raises(result):
        assert StateCodeAnalyser().no_of_states(path)
        assert StateCodeAnalyser().sort_by_state_code(path)
