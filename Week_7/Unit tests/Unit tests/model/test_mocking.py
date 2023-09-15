from unittest import mock
import numpy as np
from mocking import get_mean

@mock.patch('mocking.get_random_numbers')
def test_get_mean(mock_get_random_numbers):
    mock_get_random_numbers.return_value = np.asarray([1, 2, 3, 4, 5])
    expected_output = 3.0
    actual_output = get_mean(5)
    assert actual_output==expected_output