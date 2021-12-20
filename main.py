from keepalive import keep_alive
import os

from pushbullet import Pushbullet
import requests

from getweb import getweb
import time
starttime = time.time()

keep_alive()
pb = Pushbullet(os.environ['TOKEN'])
#print(pb.devices)
a70 = pb.get_device('a70')

def look():
	try:
		binder = requests.get('https://spectrumoutfitters.co.uk/collections/short-binders/products/pastel-blue-short-chest-binder?variant=39500295635139')
		all = requests.get('https://spectrumoutfitters.co.uk/collections/short-binders')
		if not '<span data-add-to-cart-text data-default-text="Add to cart">\n        Sold Out\n      </span>' in binder.text:
			push = a70.push_note("Spectrum", 'BLUE BINDER AVAILABLE')
	#	else: push = a70.push_note("Spectrum",'BINDER UNAVAILABLE')
		if not open('grid.txt').read() in str(all.text.encode('ascii', 'replace')):
			if all.text.count('Sold Out') - 1 > int(open("sold.txt", "rt").read()):
				push = a70.push_note("Spectrum", 'BINDER SOLD OUT')
				print('BINDER SOLD OUT')
			else:
				push = a70.push_note("Spectrum", str((all.text.count('span class=money') - 5) - (all.text.count('Sold Out') - 1)) + ' AVAILABLE')
				print(str((all.text.count('span class=money') - 5) - (all.text.count('Sold Out') - 1)) + ' AVAILABLE')

	except Exception as exception:
		push = a70.push_note("Spectrum", str(type(exception).__name__) + ' OCCURRED')

	else:
		#push = a70.push_note("Spectrum", 'RUN SUCCESSFUL')
		pass

while True:
	print('DEBUG: running')
	if open("doupdate.txt", "rt").read() == '1':
		getweb(True)
		upd = open('doupdate.txt','w')
		upd.write('0')
		upd.close()
	look()
	time.sleep(60.0 - ((time.time() - starttime) % 60.0))
