import numpy as np
import cv2


def find_wall_x(img, threshold, square_x, matrix, x_start, y_start, x_size, y_size, grid):
    b = 0
    labyrinth = np.copy(img)
    for j in range(grid):
        b += 1
        a = 0
        for i in range(grid - 1):
            a += 1
            sum_of_white_pixels = np.sum(threshold[y_start + j * square_x:(j + 1) * (square_x) + y_start + y_size,
                                         x_start + i * square_x:x_size + x_start + (i + 1) * square_x])
            if sum_of_white_pixels > 100:
                labyrinth[y_start + j * square_x:(j + 1) * (square_x) + y_start + y_size,
                x_start + i * square_x:x_size + x_start + (i + 1) * square_x] = (
                    0, 0, 255)
                matrix[j + b - 1, i + a] = 0
            else:
                labyrinth[y_start + j * square_x:(j + 1) * (square_x) + y_start + y_size,
                x_start + i * square_x:x_size + x_start + (i + 1) * square_x] = (
                    0, 255, 0)


def find_wall_y(img, threshold, square_x, matrix, x_start, y_start, x_size, y_size, grid):
    b = 0
    labyrinth = np.copy(img)
    for j in range(grid - 1):
        b += 1
        a = -1
        for i in range(grid - 1):
            a += 1
            sum_of_white_pixels = np.sum(threshold[y_start + j * square_x:(j + 1) * (square_x) + y_start + y_size,
                                         x_start + i * square_x:x_size + x_start + (i + 1) * square_x])
            if sum_of_white_pixels > 30:
                labyrinth[y_start + j * square_x:(j + 1) * (square_x) + y_start + y_size,
                x_start + i * square_x:x_size + x_start + (i + 1) * square_x] = (
                    0, 0, 255)
                matrix[j + b, i + a] = 0
            else:
                labyrinth[y_start + j * square_x:(j + 1) * (square_x) + y_start + y_size,
                x_start + i * square_x:x_size + x_start + (i + 1) * square_x] = (
                    0, 255, 0)
            matrix[j + b, i + a + 1] = 0


def main():
    img = cv2.imread("./labirynt.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    grid = 16
    square_x = int(img_gray.shape[0] / grid)

    _, threshold = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)

    x_start, y_start = (10, 6)
    x_size, y_size = (0, -15)
    matrix = np.ones(((grid - 1) * 2 + 1, (grid - 1) * 2 + 1), dtype='int')
    find_wall_x(img, threshold, square_x, matrix, x_start, y_start, x_size, y_size, grid)

    x_start, y_start = (10, 6)
    x_size, y_size = (-15, 5)
    find_wall_y(img, threshold, square_x, matrix, x_start, y_start, x_size, y_size, grid)
    matrix[0, 0] = 2  # start
    return matrix


main()
