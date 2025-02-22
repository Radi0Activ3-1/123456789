import unittest
from main import calculate_hypotenuse, calculate_distance

class TestMathFunctions(unittest.TestCase):
    def test_hypotenuse(self):
        # Test case 1
        sides = (3, 4)
        expected = 5.0
        result = calculate_hypotenuse(sides)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")
        print(f"Hypotenuse test case 1 passed: {result} == {expected}")

        # Test case 2
        sides = (5, 12)
        expected = 13.0
        result = calculate_hypotenuse(sides)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")
        print(f"Hypotenuse test case 2 passed: {result} == {expected}")

        # Test case 3
        sides = (8, 15)
        expected = 17.0
        result = calculate_hypotenuse(sides)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")
        print(f"Hypotenuse test case 3 passed: {result} == {expected}")

    def test_distance(self):
        # Test case 1
        point1 = (1, 2)
        point2 = (4, 6)
        expected = 5.0
        result = calculate_distance(point1, point2)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")
        print(f"Distance test case 1 passed: {result} == {expected}")

        # Test case 2
        point1 = (0, 0)
        point2 = (3, 4)
        expected = 5.0
        result = calculate_distance(point1, point2)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")
        print(f"Distance test case 2 passed: {result} == {expected}")

        # Test case 3
        point1 = (-1, -1)
        point2 = (2, 3)
        expected = 5.0
        result = calculate_distance(point1, point2)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")
        print(f"Distance test case 3 passed: {result} == {expected}")

if __name__ == "__main__":
    unittest.main()
