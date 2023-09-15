import pytest

from parameteric import weekday_or_weekend

@pytest.mark.parametrize(
    'cob, expected', [('2023-01-15', 'Weekend'), ('2023-01-16', 'Weekday')]
)
def test_weekday_or_weekend(cob, expected):
    actual = weekday_or_weekend(cob)
    assert actual==expected