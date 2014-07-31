def line_Parse(xline, str):
	if str in xline:
		Title = str
		outfile.write('%s\n' % Title)
		xline = xline.replace(str, '')		
		iTime = xline[:6]
		outfile.write('Time:%s\n' % iTime)
		xline = xline[6:]		
		for n in Neighborhood:
			if n in xline:
				iNeighborhood = n
				outfile.write('Neighborhood:%s\n' % iNeighborhood)
				NeighborhoodStart = xline.find(n)
				iAddress = xline[:(NeighborhoodStart)]
				outfile.write('Address:%s\n' % iAddress)
				xline = xline[(NeighborhoodStart + len(n)):]
				try:
					xline = xline.split(' ')
					Age = xline[2]
					outfile.write('Age:%s\n' % Age)
					Gender = xline[3]
					outfile.write('Gender:%s\n' % Gender)
					iNumber = xline[1]
					outfile.write('Incident Number:%s\n' % iNumber)
				except IndexError:
					iNumber = ''.join(x for x in line if x.isdigit())
					outfile.write('Incident Number:%s\n' % iNumber)
					print ("Danger Will Robinson!")					
				break	


with open('wednesday20140723.txt') as file:
	blotterString = file.read()
	blotterList = blotterString.split('\n')
	incidentDate = blotterList[2]
	
OddsnEnds = [ incidentDate, "PITTSBURGH BUREAU OF POLICE", "Incident Blotter", "Sorted by:", "DISCLAIMER:", "assumes", "Zone", "Report Name", "Section Description", "(hotels and restaurants)", "waters", "Abuse of emergency 911", "Tip Marker, or Similar)", "feet", "Enhanced", "permission of non-city own property", "Incident Date"]

Neighborhood = [
 "Mount Oliver Borough", "Allegheny Center", "Allegheny West", "Allentown", "Arlington", "Arlington Heights", "Banksville", "Bedford Dwellings", "Beechview",
 "Beltzhoover", "Bloomfield", "Bluff", "Bon Air", "Brighton Heights", "Brookline", "California-Kirkbride", "Carrick", "Central Business District", "Central Lawrenceville",
 "Central Northside", "Central Oakland", "Chartiers City", "Chateau", "Crafton Heights", "Crawford-Roberts", "Duquesne Heights", "East Allegheny",
 "East Carnegie", "East Hills", "East Liberty", "Elliott", "Esplen", "Fairywood", "Fineview", "Friendship", "Garfield", "Glen Hazel", "Greenfield", "Hays",
 "Hazelwood", "Highland Park", "Homewood North", "Homewood South", "Homewood West", "Knoxville", "Larimer", "Lincoln Place", "Lincoln-Lemington-Belmar",
 "Lower Lawrenceville", "Manchester", "Marshall-Shadeland", "Middle Hill", "Morningside", "Mt. Oliver", "Mount Washington", "New Homestead", "North Oakland",
 "North Shore", "Northview Heights", "Oakwood", "Overbrook", "Perry North", "Perry South", "Point Breeze North", "Point Breeze", "Polish Hill", "Regent Square",
 "Ridgemont", "Shadyside", "Sheraden", "South Oakland", "South Shore", "South Side Flats", "South Side Slopes", "Spring Garden", "Spring Hill-City View",
 "Squirrel Hill North", "Squirrel Hill South", "St. Clair", "Stanton Heights", "Strip District", "Summer Hill", "Swisshelm Park", "Terrace Village",
 "Troy Hill-Herrs Island", "Upper Hill", "Upper Lawrenceville", "West End", "West Oakland", "Westwood", "Windgap", "Outside City",
 "Golden Triangle/Civic", # Arena is on the next line
 "N/A", "Outside County", "Outside State", "Troy Hill"
 ]

with open("test.txt", 'w') as outfile:
	outfile.write('%s\n' % incidentDate)
	for line in blotterList:
		if not any([o in line for o in OddsnEnds]):
			#outfile.write('%s\n' % line)
			line_Parse(line, 'ARREST')
			line_Parse(line, 'OFFENSE 2.0')
'''			

			elif "OFFENSE 2.0" in line:
				Title = "OFFENSE 2.0:"
				line = line.replace("OFFENSE 2.0", '')
				iTime = line[:6]
				line = line[6:]
				for n in Neighborhood:
					if n in line:
						iNeighborhood = n
						NeighborhoodStart = line.find(n)
						iAddress = line[:(NeighborhoodStart)]
						line = line[(NeighborhoodStart + len(n)):]
						iNumber = ''.join(x for x in line if x.isdigit())
						outfile.write('%s\n' % Title)
						outfile.write('Time:%s\n' % iTime)
						outfile.write('Neighborhood:%s\n' % iNeighborhood)
						outfile.write('Address:%s\n' % iAddress)
						outfile.write('Incident Number:%s\n' % iNumber)
						break
'''
