from keepalive import keep_alive # an included python scipt, for 24/7 running

from naipush import pushnote # my own cute little pushbullet cleanup <3
from getweb import updatew, lookw # an included python script, to refresh reference copies of the site

import time
starttime = time.time() # 

keep_alive() # set up webserver for uptime robot to ping

while True:
	hour = int(time.strftime("%H", time.localtime())) # save current hour as int 'hour', 0-24 format
	if hour > 7 and hour < 23: # is time between 8:00am and 10:59pm?
		print('DEBUG: running @ hour', hour)
		if open("doupdate.txt", "rt").read() == '1':
			updatew(True) # fetches comparison files, with option to spit out values to terminal
			with open('doupdate.txt','w') as upd: upd.write('0')
		look = lookw() # actually runs all the checking and notifying code
		if look != 'BLIP':
			pushnote(look[0],look[1])
		time.sleep(60.0 - ((time.time() - starttime) % 60.0)) # wait 1 minute (accounting for lag)
