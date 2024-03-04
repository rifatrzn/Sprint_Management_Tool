class SprintVelocityCalculator:
    def __init__(self, sprint_points=None):
        self.sprint_points = sprint_points if sprint_points else []

def input_sprint_points(calculator):
    print("Input sprint points (type 'done' to finish):")
    while True:
        points = input("> ")
        if points.lower() == 'done':
            break
        calculator.sprint_points.append(int(points))


def calculate_average_velocity(calculator):
    if not calculator.sprint_points:
        return 0
    return sum(calculator.sprint_points) / len(calculator.sprint_points)


def display_velocity(calculator):
    avg_velocity = calculate_average_velocity(calculator)
    print(f"Average Sprint Velocity: {avg_velocity} points")


def main_feature_a():
    initial_points = [30, 40, 50, 45]  # Example data
    calculator = SprintVelocityCalculator(initial_points)
    # Optionally, uncomment the next line to input more points
    input_sprint_points(calculator)
    display_velocity(calculator)

if __name__ == "__main__":
    main_feature_a()