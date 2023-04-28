with open('timeZones.txt', 'r') as infile:
    lines = infile.readlines()

with open('US-Timezones.txt', 'w') as outfile:
    for line in lines:
        columns = line.strip().split('\t')
        countries = columns[0]
        if countries == 'US':
         outfile.write(line )
