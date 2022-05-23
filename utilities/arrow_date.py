import arrow
import datetime
#format
print(f'current time in PST: { arrow.now("US/Pacific").format("MMMM DD, YYYY HH:mm A")}');
print(f'current time in EST: { arrow.now("America/New_York").format("MMMM DD, YYYY HH:mm A")}');


print(f'Today is {arrow.now().format("dddd DD,MMM")} and time is {arrow.now().format("HH:mm")}')
event_date = arrow.now().shift(hours=2)
attend_date=event_date.shift(minutes=60)
print(f'Event will start in {event_date.humanize(arrow.now(), only_distance=True)}, Please reach venue in {event_date.humanize(attend_date, granularity=["hour"])}')

flight_schedule_date = arrow.now("America/New_York")
flight_landing_date = flight_schedule_date.shift(hours=28).to('+05:30')

print(f'flight scheduled departure is {flight_schedule_date.format("DD,MMM HH:mm A ZZZ")} and expected arrival at destination is {flight_landing_date.format("DD,MMM HH:mm A ZZ")}')


startdate = arrow.now("America/New_York")
enddate = startdate.shift(hours=23)
print(f'We move at: {startdate.format("DD,MMM HH:mm A ZZZ")} and will arrival at destination at {enddate.format("DD,MMM HH:mm A ZZZ")}')
assembledate = startdate.shift(minutes=120)
print(f'Team gathers at {startdate.humanize(assembledate)} at school gate')

#Output

#We move at: 23,May 12:10 PM EDT and will arrival at destination at 24,May 11:10 AM EDT
#Team gathers at 2 hours ago at school gate