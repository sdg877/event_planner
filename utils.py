import arrow
import pytz

# Parse a string into a datetime object in the user's timezone
def parse_event_time(date_string, user_timezone):
    naive_time = arrow.get(date_string, "YYYY-MM-DD HH:mm:ss")  # Adjust as needed
    return user_timezone.localize(naive_time)

# Convert event time to different time zones
def convert_to_timezone(event, target_timezone):
    return event.start_time.astimezone(pytz.timezone(target_timezone))
