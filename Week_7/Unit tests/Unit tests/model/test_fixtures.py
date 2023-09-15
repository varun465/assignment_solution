import pytest
import pandas as pd
from fixtures import is_all_pass, get_only_passes


@pytest.fixture
def get_results():
    return pd.read_csv(r'C:\Users\ME454XC\OneDrive - EY\Codes\Unit tests\mock_data\mock_student_results.csv')

def test_is_all_pass(get_results):
    actual_output = is_all_pass(get_results)
    expected_output = False
    assert actual_output == expected_output

def test_get_only_passes(get_results):
    actual_output = get_only_passes(get_results)
    expected_output = pd.read_csv(r'C:\Users\ME454XC\OneDrive - EY\Codes\Unit tests\expected_output\expected_student_results.csv')
    pd.testing.assert_frame_equal(actual_output, expected_output)
