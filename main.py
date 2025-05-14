from event_calendar import UserProfile, Event
from utils import parse_event_time, convert_to_timezone

def main():
    user_name = input("Enter your name: ")
    user_timezone = input("Enter your timezone (e.g., 'UTC', 'US/Eastern'): ")

    user = UserProfile(user_name, user_timezone)

    while True:
        event_title = input("\nEnter event title: ")
        start_time = input("Enter start time (YYYY-MM-DD HH:mm:ss): ")
        end_time = input("Enter end time (YYYY-MM-DD HH:mm:ss): ")
        event_category = input("Enter event category (e.g., Work, Personal, Meeting): ")

        start_time_parsed = parse_event_time(start_time, user.timezone)
        end_time_parsed = parse_event_time(end_time, user.timezone)

        event = Event(event_title, start_time_parsed, end_time_parsed, event_category)
        user.add_event(event)

        print("\nEvent added successfully!")

        more_events = input("\nDo you want to add another event? (yes/no): ")
        if more_events.lower() != 'yes':
            break

    print("\nYour events:")
    user.display_events()

    # Optionally, convert and display events in a different time zone
    convert = input("\nDo you want to view events in a different time zone? (yes/no): ")
    if convert.lower() == "yes":
        target_timezone = input("Enter target time zone: ")
        for event in user.events:
            new_time = convert_to_timezone(event, target_timezone)
            print(f"Event: {event.title}, Time in {target_timezone}: {new_time}")
    

if __name__ == "__main__":
    main()
