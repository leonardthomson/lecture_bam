import pytest
"""
This module contains test functions for the homework03 module.

Functions:
    test_first_entree_time_of_rolling_six: Tests the first_entree_time_of_rolling_six function to ensure it returns a value between 1 and 6.
    test_simulate_n_draws: Tests the simulate_n_draws function to ensure it returns a list of n values, each between 1 and 6.

You can run this test module by running `pytest test_homework03.py` in the terminal.
"""
from homework03 import first_entree_time_of_rolling_six, simulate_n_draws


# test_homework03.py
def test_first_entree_time_of_rolling_six():
    """
    Test the first_entree_time_of_rolling_six function to ensure it returns a value between 1 and 6.
    """
    for _ in range(100):
        result = first_entree_time_of_rolling_six()
        assert isinstance(result, int)

def test_simulate_n_draws():
    """
    Test the simulate_n_draws function to ensure it returns a list of n values, each between 1 and 6.
    """
    n = 10
    results = simulate_n_draws(n)
    assert len(results) == n
    for result in results:
        assert isinstance(result, int)

if __name__ == "__main__":
    pytest.main()