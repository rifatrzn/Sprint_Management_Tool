from feature_b import TeamMember, TeamCapacity, calculate_effort_minutes, display_team_capacity

# Scenario 1: Calculating and Displaying Team and Per Person Effort-Hours (Happy Path)
def scenario_1_feature_b():
    print("Scenario 1: Happy Path")
    team_capacity = TeamCapacity(10)
    team_capacity.add_team_member(TeamMember("Alex", 480, 1, 120))
    team_capacity.add_team_member(TeamMember("Reyal", 420, 2, 60))
    total_effort, per_person_effort = calculate_effort_minutes(team_capacity)
    # Add assertion or validation if necessary
    display_team_capacity(team_capacity)
    # Manual verification required for printed output

# Scenario 2: Handling No Team Members (Unhappy Path)
def scenario_2_feature_b():
    print("\nScenario 2: Unhappy Path")
    team_capacity_empty = TeamCapacity(10)
    total_effort, per_person_effort = calculate_effort_minutes(team_capacity_empty)
    assert total_effort == 0 and per_person_effort == 0, "Expected total and per person effort to be 0"
    display_team_capacity(team_capacity_empty)
    # Manual verification required for printed output

if __name__ == "__main__":
    scenario_1_feature_b()
    scenario_2_feature_b()
