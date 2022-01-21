from keepalive import keep_alive # an included python scipt, for 24/7 running

from naipush import pushnote

import requests # to get the html code from the websites

from getweb import getweb # an included python script, to refresh reference copies of the site
import time
starttime = time.time()

keep_alive() # set up webserver for uptime robot to ping

def look():
	try:
		all = requests.get('https://spectrumoutfitters.co.uk/collections/short-binders')
		if not open('grid.txt').read() in str(all.text.encode('ascii', 'replace')): # if grid file contents isn't in the copy of the website just fetched
			if all.text.count('Sold Out') - 1 > int(open("sold.txt", "rt").read()):
				pushnote("Spectrum", 'BINDER SOLD OUT')
				print('BINDER SOLD OUT')
			else:
				pushnote("Spectrum", str((all.text.count('span class=money') - 5) - (all.text.count('Sold Out') - 1)) + ' AVAILABLE')
				print(str((all.text.count('span class=money') - 5) - (all.text.count('Sold Out') - 1)) + ' AVAILABLE')

	except Exception as exception: # grab error name/type
		pushnote("Spectrum", str(type(exception).__name__) + ' OCCURRED')

	else:
		#pushnote("Spectrum", 'RUN SUCCESSFUL') # DEBUG ONLY
		pass # here so I don't ever have to comment out the whole else statement during debugging

while True:
	hour = int(time.strftime("%H", time.localtime())) # save current hour as int 'hour', 0-24 format
	if hour > 7 and hour < 23: # is time between 8:00am and 10:59pm?
		print('DEBUG: running @ hour', hour)
		if open("doupdate.txt", "rt").read() == '1':
			getweb(True) # fetches comparison files, with option to spit out values to terminal
			with open('doupdate.txt','w') as upd: upd.write('0')
		look() # actually runs all the checking and notifying code
		time.sleep(60.0 - ((time.time() - starttime) % 60.0)) # wait 1 minute (accounting for lag)
