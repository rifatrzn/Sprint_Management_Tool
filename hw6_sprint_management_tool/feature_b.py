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