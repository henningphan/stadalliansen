from icalendar import Calendar, Event
from datetime import datetime
from zoneinfo import ZoneInfo

tz = ZoneInfo("Europe/Stockholm")
calendar = Calendar()

event = Event()
event.add("name", "name")
event.add("description", "description")
event.add("summary", "summary")
event.add("uid", "1")
event.add("dtstart", datetime(2025, 11,11, tzinfo=tz))
event.add("dtend", datetime(2025, 11,11, tzinfo=tz))
calendar.add_component(event)
event = Event()
event.add("name", "name2")
event.add("summary", "summary2")
event.add("uid", "2")
event.add("description", "description2")
event.add("dtstart", datetime(2025, 12,12, tzinfo=tz))
event.add("dtend", datetime(2025, 12,12, tzinfo=tz))
calendar.add_component(event)
print(calendar.to_ical())
