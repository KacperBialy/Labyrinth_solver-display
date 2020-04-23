import labyrinth_finder
import numpy as np


def next_points(actually_points, direction, footpath, step):
    points = dict()
    for point in actually_points.keys():
        for value in direction.values():
            point = point[0] + value[0], point[1] + value[1]
            help_val = {point: step}
            if point in footpath:
                points.update(help_val)
                footpath.remove(point)
    return points


def find_the_shortest_path(actually_points, direction, step, all_points):
    the_shortest_path = []
    for point in actually_points:
        for value in direction.values():
            point = point[0] + value[0], point[1] + value[1]
            field_value = all_points.get(point)
            if field_value == step:
                the_shortest_path.append(point)
                return the_shortest_path


def main(matrix):
    # matrix = labirynth_finder.main()

    footpath = set()
    for j in range(matrix.shape[0]):
        for i in range(matrix.shape[1]):
            if matrix[i, j] == 1:
                footpath.add((i, j))
            elif matrix[i, j] == 2:
                start_position = (i, j)
            elif matrix[i, j] == 3:
                end_position = (i, j)
                footpath.add(end_position)
    direction = {'UP': (-1, 0), 'DOWN': (2, 0), 'RIGHT': (-1, 1), 'LEFT': (0, -2)}
    actually_points = {start_position: 0}
    all_points = {start_position: 0}
    step = 0

    while True:
        step += 1
        actually_points = next_points(actually_points, direction, footpath, step)
        all_points.update(actually_points)
        if end_position in actually_points.keys():
            break
    actually_points = []
    actually_points.append(end_position)
    the_shortest_path = []

    while True:
        step -= 1
        actually_points = find_the_shortest_path(actually_points, direction, step, all_points)
        the_shortest_path.append([actually_points[0][0], actually_points[0][1]])
        if start_position in actually_points:
            break

    the_shortest_path.sort()
    return the_shortest_path


