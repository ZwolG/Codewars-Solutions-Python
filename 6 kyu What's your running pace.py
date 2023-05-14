'''
What's your running pace?

DESCRIPTION:
In this Kata, we will calculate running pace. To do that, we have to know the distance and the time.

Create the following function:

runningPace(distance, time)

Where: distance - A float with the number of kilometres

time - A string containing the time it took to travel the distance. It will always be minutes:seconds. For example "25:00" means 25 minutes. You don't have to deal with hours.

The function should return the pace, for example "4:20" means it took 4 minutes and 20 seconds to travel one kilometre.

Note: The pace should always return only the number of minutes and seconds. You don't have to convert these into hours. Floor the number of seconds.
'''

def running_pace(distance, time):
    minutes, seconds = time.split(':')
    total_seconds = int(minutes) * 60 + int(seconds)
    seconds_per_mile = float(total_seconds) / float(distance)
    minutes_per_mile = int(seconds_per_mile / 60)
    seconds_reminder = int(seconds_per_mile - (minutes_per_mile * 60))
    return f'{minutes_per_mile}:0{seconds_reminder}' if seconds_reminder < 10 else  f'{minutes_per_mile}:{seconds_reminder}'
