#!/usr/bin/env python
# coding: utf-8

## checks all the possible states 

def all_possible_states(size):
    up = 1
    bits = []
    for i in range(size):
        up += 2**i
    for i in range(up):
        bits.append([(i >> bit) & 1 for bit in range(size - 1, -1, -1)])
    return bits

def check_sum_around(board_size, check_point, check_state):
    # the nine points around check_point
    nine_points = []
    for i in range(3):
        for j in range(3):
            nine_points.append((i+check_point[0]-1, j+check_point[1]-1))
            
    # map the nine points to the state list using -> b*(row-1)+col
    points_state_pos_map = [] 
    for point in nine_points:
        if point[1] > 0 and point[0] > 0 and point[0] <= board_size[0] and point[1] <= board_size[1]:
            points_state_pos_map.append((board_size[1]*(point[0]-1) + point[1]))
    
    sum_around = 0
    for pos in points_state_pos_map:
        sum_around += check_state[pos-1]
    return sum_around


def find_solution(board_size, board_config):
    # go through all the states one by one
    state_size = board_size[0] * board_size[1]
    all_states = all_possible_states(state_size)
    solution_states = []
    
    for state in all_states:
        is_solution = True
        for point in board_config:
            if point[0] != check_sum_around(board_size, point[1], state):
                is_solution = False
                break
        if is_solution:
            solution_states.append(state)
    return solution_states


# board_size = (2, 3)
# 4 at (1, 1) and 2 at (2, 3)
find_solution((2, 3), [(4, (1, 1)), (2, (2, 3))])


find_solution((3,3), [(9, (2,2))])


# find_solution((5, 5), [(1, (1, 5)), (9, (2, 2)), (8, (3, 2)), (8, (3, 3)), (4, (4, 5)), (4, (5, 1)), (5, (5, 3)), (2, (5, 5))])