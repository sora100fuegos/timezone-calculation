import pytz
from timezonefinder import TimezoneFinder

# define the latitude and longitude
latitude = 37.7749
longitude = -122.4194

# create a timezone finder object
tf = TimezoneFinder()

# get the timezone at the given location
with open('US.txt', 'r') as infile:
    lines = infile.readlines()

with open('US-newTimezones.txt', 'w') as outfile:
    for line in lines:
        columns = line.strip().split('\t')
        latitude = columns[9]
        longitude = columns[10]
        timezone_str = tf.timezone_at(lat = float(latitude),lng = float(longitude))
        with open('US-Timezones.txt', 'r') as infile2:
         timeZoneLines = infile2.readlines()
         for timezone in timeZoneLines:
          columns = timezone.strip().split('\t')
          UStimeZone = columns[1]
          if timezone_str == UStimeZone:
           newline = line+timezone
           print(("{} {}\n".format(line.rstrip(), timezone.rstrip())))
           outfile.write("{} {}\n".format(line.rstrip(), timezone.rstrip()))

