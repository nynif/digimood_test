import pytest
from part_3 import calculate_distance, generate_random_positions, pair_ships_and_find_goal_locations

def test_calculate_distance():
    # Test avec des points dans un plan à deux dimensions
    p1 = [0, 0]
    p2 = [3, 4]
    expected_result = 5  # La distance entre (0,0) et (3,4) est 5 d'après le théorème de Pythagore.
    assert calculate_distance(p1, p2) == expected_result

# Test pour la fonction generate_random_positions
def test_generate_random_positions():
    fleet_size = 4
    grid_size = 5
    offensive_ship_positions, support_ship_positions = generate_random_positions(fleet_size, grid_size)
    
    assert len(offensive_ship_positions) == fleet_size // 2
    assert len(support_ship_positions) == fleet_size // 2
    
    # Vérifiez qu'il n'y a pas de positions en double
    assert len(set(offensive_ship_positions + support_ship_positions)) == fleet_size

# Test pour la fonction pair_ships_and_find_goal_locations
def test_pair_ships_and_find_goal_locations():
    offensive_ship_positions = [(0, 0), (2, 2)]
    support_ship_positions = [(1, 1), (3, 3)]
    expected_pairs = [((0, 0), (1, 0)), ((2, 2), (3, 2))]
    assert pair_ships_and_find_goal_locations(offensive_ship_positions, support_ship_positions) == expected_pairs