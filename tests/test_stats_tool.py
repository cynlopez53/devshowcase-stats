import pytest
from stats_tool import process_stats

def test_basic_stats():
    payload = {"numbers": [1, 2, 3]}
    result = process_stats(payload)
    assert result["count"] == 3
    assert result["sum"] == 6
    assert result["mean"] == 2

def test_verbose_summary():
    payload = {"numbers": [1, 2, 3], "verbose": True}
    result = process_stats(payload)
    assert "summary" in result
    assert isinstance(result["summary"], str)

def test_normalize_mode():
    payload = {"numbers": [1, 2, 3], "mode": "normalize"}
    result = process_stats(payload)
    assert "normalized" in result
    assert result["normalized"] == [0.0, 0.5, 1.0]

def test_cumsum_mode():
    payload = {"numbers": [1, 2, 3], "mode": "cumsum"}
    result = process_stats(payload)
    assert result["cumsum"] == [1, 3, 6]

def test_invalid_input():
    payload = {"numbers": "not a list"}
    with pytest.raises(Exception):
        process_stats(payload)

def test_empty_list():
    payload = {"numbers": []}
    result = process_stats(payload)
    assert result["count"] == 0
    assert "summary" not in result
