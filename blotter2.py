import os

OddsnEnds = [ "PITTSBURGH BUREAU OF POLICE", "Incident Blotter", "Sorted by:", "DISCLAIMER:", "Incident Date", "assumes", "Page", "Report Name"]	


if not os.path.exists("../out/"):
	os.makedirs("../out/")	
with open("../txt/20140731.txt", 'r') as file:
	blotterList = file.readlines()
	
with open("../out/test2.txt", 'w') as outfile:
	cleanList = []
	incident = []
	while '\n' in blotterList:
		blotterList.remove('\n')
	for line in blotterList:
		line = line.rstrip('\n')
		if not any ([o in line for o in OddsnEnds]):
			cleanList.append(line)
		print (line)

			
		
		
		
		
		
'''		
	for line in cleanList:
		if any ([b in line for b in Buzz]):
	for i in [i for i, j in enumerate(cleanList) if j == 'ARREST\n']:
		print ('Incident:%s' % cleanList[i])
	for i in [i for i, j in enumerate(cleanList) if j == 'Incident Time\n']:
		print ('Time:%s' % cleanList[i+1])
'''		