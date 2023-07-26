# Space Defense
# 26/07/2023, by Antoine Boutet

import random
import math

# Define constants for fleet and grid size
FLEET_SIZE = 50
GRID_SIZE = 100

# Function to calculate Euclidean distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Function to generate random positions for the fleet
def generate_random_positions(fleet_size, grid_size):
    # Generate all possible positions on the grid
    all_positions = [(x, y) for x in range(grid_size) for y in range(grid_size)]

    # Randomly shuffle the positions
    random.shuffle(all_positions)

    # Take the first fleet_size positions from the shuffled list
    fleet_positions = all_positions[:fleet_size]

    # Assign positions to vessels (first half of the list are offensive ships, second half are support ships)
    offensive_ship_positions = fleet_positions[:fleet_size//2]
    support_ship_positions = fleet_positions[fleet_size//2:]
    return offensive_ship_positions, support_ship_positions

# Function to pair up the ships and find their goal locations
def pair_ships_and_find_goal_locations(offensive_ship_positions, support_ship_positions):
    pairs = []

    # For each offensive ship, find the nearest support ship that is not already paired
    for offensive_position in offensive_ship_positions:
        min_distance = float('inf')
        nearest_support_position = None
        for support_position in support_ship_positions:
            if support_position not in [pair[1] for pair in pairs]:
                distance = calculate_distance(offensive_position, support_position)
                if distance < min_distance:
                    min_distance = distance
                    nearest_support_position = support_position

        # Pair the offensive ship with the nearest support ship
        pairs.append((offensive_position, nearest_support_position))
    
    # Move the support ships to be adjacent to their paired offensive ship
    for i, pair in enumerate(pairs):
        offensive_position, support_position = pair

        # Calculate new position for the support ship to be adjacent to the offensive ship
        # We simply move the support ship one unit to the right of the offensive ship if it's within the grid
        if offensive_position[0] < GRID_SIZE - 1:
            new_support_position = (offensive_position[0] + 1, offensive_position[1])
        else:
            new_support_position = (offensive_position[0] - 1, offensive_position[1])

        # Update the pair with the new position for the support ship
        pairs[i] = (offensive_position, new_support_position)
    
    return pairs

# Generate initial random positions for the fleet
offensive_ship_positions, support_ship_positions = generate_random_positions(FLEET_SIZE, GRID_SIZE)

# Calculate goal locations for the fleet
goal_locations = pair_ships_and_find_goal_locations(offensive_ship_positions, support_ship_positions)