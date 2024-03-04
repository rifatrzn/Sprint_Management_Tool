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
