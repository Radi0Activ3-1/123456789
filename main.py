#Drake Pierce-Demksi
#

import math

def calculate_hypotenuse(sides):
    # Unpack the tuple
    a, b = sides
    # Calculate the hypotenuse
    c = math.sqrt(a**2 + b**2)
    return c

def calculate_distance(point1, point2):
    # Unpack the tuples
    x1, y1 = point1
    x2, y2 = point2
    # Calculate the distance
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

if __name__ == "__main__":
    # Example for Pythagorean Theorem
    sides = (3, 4)
    hypotenuse = calculate_hypotenuse(sides)
    print(f"The hypotenuse is: {hypotenuse}")

    # Example for Distance Formula
    point1 = (1, 2)
    point2 = (4, 6)
    distance = calculate_distance(point1, point2)
    print(f"The distance between the points is: {distance}")
