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
