import os
import json
import pytest
from state_census_analyser.main.state_census_analyse import *


@pytest.mark.parametrize('path, result', [("IndiaStateCensusData - IndiaStateCensusData.csv", 29)])
def test_for_matching_no_of_records(path, result):
    path = os.path.join(os.path.dirname(__file__), path)
    assert StateCensusAnalyser().no_of_states(path) == result


@pytest.mark.parametrize('path, result1, result2',
                         [("IndiaStateCensusData - IndiaStateCensusData.csv", "Andhra Pradesh", "West Bengal"),
                          ])
def test_for_matching_sort_by_states(path, result1, result2):
    path = os.path.join(os.path.dirname(__file__), path)
    json_list = json.loads(StateCensusAnalyser.sort_by_state(path))
    assert json_list[0].get("State") == result1
    assert json_list[len(json_list) - 1].get("State") == result2


@pytest.mark.parametrize('path, result1, result2',
                         [("IndiaStateCensusData - IndiaStateCensusData.csv", "Uttar Pradesh", "Sikkim"),
                          ])
def test_for_matching_sort_by_states_population(path, result1, result2):
    path = os.path.join(os.path.dirname(__file__), path)
    json_list = json.loads(StateCensusAnalyser.sort_by_state_population_descending(path))
    assert json_list[0].get("State") == result1
    assert json_list[len(json_list) - 1].get("State") == result2


@pytest.mark.parametrize('path, result1, result2',
                         [("IndiaStateCensusData - IndiaStateCensusData.csv", "Bihar", "Arunachal Pradesh"),
                          ])
def test_for_matching_sort_by_states_population_density(path, result1, result2):
    path = os.path.join(os.path.dirname(__file__), path)
    json_list = json.loads(StateCensusAnalyser.sort_by_state_population_density_descending(path))
    assert json_list[0].get("State") == result1
    assert json_list[len(json_list) - 1].get("State") == result2

@pytest.mark.parametrize('path, result1, result2',
                         [("IndiaStateCensusData - IndiaStateCensusData.csv", "Rajasthan", "Goa"),
                          ])
def test_for_matching_sort_by_states_population_density(path, result1, result2):
    path = os.path.join(os.path.dirname(__file__), path)
    json_list = json.loads(StateCensusAnalyser.sort_by_state_area_descending(path))
    assert json_list[0].get("State") == result1
    assert json_list[len(json_list) - 1].get("State") == result2


@pytest.mark.parametrize('path, result', [("IndiaStateCensusData - IndiaStateCensusData.txt", WrongFileType),
                                          ("IndiaStateCensusData - IndiaStateCensusData - WrongDelimter.csv",
                                           WrongDelimiterException),
                                          ("IndiaStateCensusData - IndiaStateData.csv", FileNotPresent),
                                          ("IndiaStateCensusData - IndiaStateCensusData - HeaderWrong.csv",
                                           WrongHeaderException)])
def test_for_matching_exceptions(path, result):
    path = os.path.join(os.path.dirname(__file__), path)
    with pytest.raises(result):
        assert StateCensusAnalyser().no_of_states(path)
        assert StateCensusAnalyser().sort_by_state(path)
