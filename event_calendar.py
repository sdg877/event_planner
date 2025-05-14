import pytz
import arrow

class UserProfile:
    def __init__(self, name, timezone="UTC", work_hours=(9, 17)):
        self.name = name
        self.timezone = pytz.timezone(timezone)
        self.work_hours = work_hours
        self.events = []  # List of events the user has created

    def add_event(self, event):
        self.events.append(event)

    def display_events(self):
        for event in self.events:
            print(event)


class Event:
    def __init__(self, title, start_time, end_time, category="General"):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.category = category  # e.g., Work, Personal, Meeting

    def __str__(self):
        return f"{self.title} ({self.start_time} - {self.end_time})"
