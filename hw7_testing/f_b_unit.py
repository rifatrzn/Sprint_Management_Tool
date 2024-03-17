import unittest
from feature_b import TeamMember, TeamCapacity, calculate_effort_minutes  # Ensure correct import path

class TestTeamCapacity(unittest.TestCase):
    def setUp(self):
        self.team_capacity = TeamCapacity(10)  # Example: 10 sprint days
        self.team_capacity.add_team_member(TeamMember("Reyad", 480, 2, 120))
        self.team_capacity.add_team_member(TeamMember("Boben", 420, 1, 60))

    def test_effort_calculation_with_team_members(self):
        total_effort, per_person_effort = calculate_effort_minutes(self.team_capacity)
        expected_total_effort = (8*480 - 120) + (9*420 - 60)  # Adjust calculations as necessary
        expected_per_person_effort = expected_total_effort / 2
        self.assertEqual((total_effort, per_person_effort), (expected_total_effort, expected_per_person_effort))

    def test_effort_calculation_without_team_members(self):
        empty_team = TeamCapacity(10)
        total_effort, per_person_effort = calculate_effort_minutes(empty_team)
        self.assertEqual((total_effort, per_person_effort), (0, 0))

if __name__ == '__main__':
    unittest.main()
