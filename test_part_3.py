import pytest
from part_3 import calculate_distance 

def test_calculate_distance():
    # Test avec des points dans un plan à deux dimensions
    p1 = [0, 0]
    p2 = [3, 4]
    expected_result = 5  # La distance entre (0,0) et (3,4) est 5 d'après le théorème de Pythagore.
    assert calculate_distance(p1, p2) == expected_result
