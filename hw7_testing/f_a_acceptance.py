from feature_a import SprintVelocityCalculator, calculate_average_velocity, display_velocity

# Scenario 1: Calculating and Displaying Average Sprint Velocity (Happy Path)
def scenario_1_feature_a():
    print("Scenario 1: Happy Path")
    calculator = SprintVelocityCalculator([30, 40, 50, 45])
    avg_velocity = calculate_average_velocity(calculator)
    assert avg_velocity == 41.25, f"Expected average velocity to be 41.25, got {avg_velocity}"
    display_velocity(calculator)  # Expected to print "Average Sprint Velocity: 41.25 points"

# Scenario 2: Handling No Sprint Points (Unhappy Path)
def scenario_2_feature_a():
    print("\nScenario 2: Unhappy Path")
    calculator_empty = SprintVelocityCalculator([])
    avg_velocity = calculate_average_velocity(calculator_empty)
    assert avg_velocity == 0, f"Expected average velocity to be 0, got {avg_velocity}"
    display_velocity(calculator_empty)  # Expected to print "Average Sprint Velocity: 0 points"

if __name__ == "__main__":
    scenario_1_feature_a()
    scenario_2_feature_a()
