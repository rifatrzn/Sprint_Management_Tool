import unittest
from feature_a import SprintVelocityCalculator, calculate_average_velocity


class TestSprintVelocityCalculator(unittest.TestCase):
    def test_average_velocity_with_initial_points(self):
        calculator = SprintVelocityCalculator([30, 40, 50, 45])
        self.assertEqual(calculate_average_velocity(calculator), 41.25)

    def test_average_velocity_with_no_points(self):
        calculator = SprintVelocityCalculator([])
        self.assertEqual(calculate_average_velocity(calculator), 0)

if __name__ == '__main__':
    unittest.main()

