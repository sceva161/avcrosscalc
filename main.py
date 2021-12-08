import datetime as dt

# show current date/time
utc = dt.datetime.utcnow()
print(utc.day, '/', utc.hour, ':', utc.minute)

# user input requested time to cross waypoint
cross = int(input("Crosstime: "))

#convert utc to minutes only
now = utc.minute

#calc minutes difference from now to crossing time and invert time if after 00minutes:
diff = cross - now

if diff <= 0:
	diff = diff + 60
else:
	diff = diff


# diff check:
#print(diff)


# distance to waypoint:
dist = float(input("Distance to run: "))

#calc GroundSPeed required to cross at given time:
speed = (dist / diff) * 60

# end result:
print("Groundspeed required: ", speed)