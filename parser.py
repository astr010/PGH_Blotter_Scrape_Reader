import os
import urllib2
import time
from datetime import datetime, timedelta
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

def parsePDF(infile, outfile):
	
	password = ''
	pagenos = set()
	maxpages = 0
	# output option
	outtype = 'text'
	imagewriter = None
	rotation = 0
	stripcontrol = False
	layoutmode = 'normal'
	codec = 'utf-8'
	pageno = 1
	scale = 1
	caching = True
	showpageno = True
	laparams = LAParams()
	rsrcmgr = PDFResourceManager(caching=caching)
	
	if outfile:
		outfp = file(outfile, 'w+')
	else:
		outfp = sys.stdout
	
	device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams, imagewriter=imagewriter)
	fp = file(infile, 'rb')
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	for page in PDFPage.get_pages(fp, pagenos,
									  maxpages=maxpages, password=password,
									  caching=caching, check_extractable=True):
			
		interpreter.process_page(page)
	fp.close()
	device.close()
	outfp.close()
	return	

# Start of main code. Didn't put this in a "main" function since I'm not sure if you're using one

# Set time zone to EST
#os.environ['TZ'] = 'America/New_York'
#time.tzset()

# make sure folder system is set up
if not os.path.exists("../pdf/"):
	os.makedirs("../pdf/")
if not os.path.exists("../txt/"):
	os.makedirs("../txt/")

# Get yesterday's name and lowercase it
yesterday = (datetime.today() - timedelta(1))
yesterday_string = yesterday.strftime("%A").lower()

# Also make a numberical representation of date for filename purposes
yesterday_short = yesterday.strftime("%Y%m%d")

# Get pdf from blotter site, save it in a file
pdf = urllib2.urlopen("http://www.city.pittsburgh.pa.us/police/blotter/blotter_" + yesterday_string + ".pdf").read();
f = file("../pdf/" + yesterday_short + ".pdf", "w+")
f.write(pdf)
f.close()

# Convert pdf to text file
parsePDF("../pdf/" + yesterday_short + ".pdf", "../txt/" + yesterday_short + ".txt")

# Save text file contents in variable
parsed_pdf = file("../txt/" + yesterday_short + ".txt", "r").read()