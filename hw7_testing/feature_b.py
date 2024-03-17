class TeamMember:
    def __init__(self, name, available_minutes_per_day, days_off, minutes_committed_to_ceremonies):
        self.name = name
        self.available_minutes_per_day = available_minutes_per_day
        self.days_off = days_off
        self.minutes_committed_to_ceremonies = minutes_committed_to_ceremonies

class TeamCapacity:
    def __init__(self, sprint_days):
        self.sprint_days = sprint_days
        self.team_members = []

    def add_team_member(self, team_member):
        self.team_members.append(team_member)

def input_team_details(team_capacity):
    while True:
        name = input("Enter team member's name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        available_minutes_per_day = int(input("Enter available minutes per day: "))
        days_off = int(input("Enter number of days off during the sprint: "))
        minutes_committed_to_ceremonies = int(input("Enter minutes committed to ceremonies: "))
        team_member = TeamMember(name, available_minutes_per_day, days_off, minutes_committed_to_ceremonies)
        team_capacity.add_team_member(team_member)

def calculate_effort_minutes(team_capacity):
    total_effort_minutes = 0
    for member in team_capacity.team_members:
        effective_days = team_capacity.sprint_days - member.days_off
        total_effort_minutes += (effective_days * member.available_minutes_per_day) - member.minutes_committed_to_ceremonies
    return total_effort_minutes, total_effort_minutes / len(team_capacity.team_members) if team_capacity.team_members else 0

def display_team_capacity(team_capacity):
    total_effort_minutes, per_person_effort_minutes = calculate_effort_minutes(team_capacity)
    print(f"Total Available Effort-Minutes for Team: {total_effort_minutes}")
    print(f"Available Effort-Minutes per Person: {per_person_effort_minutes}")

def main_feature_b():
    sprint_days = int(input("Enter the number of sprint days: "))
    team_capacity = TeamCapacity(sprint_days)
    input_team_details(team_capacity)
    display_team_capacity(team_capacity)

if __name__ == "__main__":
    main_feature_b()
