import requests # to get the html code from the websites


def updatew(debug=False):

	all = requests.get('https://spectrumoutfitters.co.uk/collections/short-binders')

	text = str(all.text.encode('ascii', 'replace'))

	if debug:
		with open('dump.txt','w') as dump:
			dump.write(text)

	start,end='class="grid grid--uniform','</div></div></div>'
	start,end=text.find(start),text.find(end)+19
	if debug: print(start,end)

	with open('grid.txt','w') as grid:
		grid.write(text[start:end])

	with open('sold.txt','w') as sold:
		sold.write(str(text.count('Sold Out')-1))
	if debug: print(str(text.count('Sold Out')-1))


def lookw(debug=False):
	try:
		all = requests.get('https://spectrumoutfitters.co.uk/collections/short-binders')
		if not open('grid.txt').read() in str(all.text.encode('ascii', 'replace')): # if grid file contents isn't in the copy of the website just fetched
			if all.text.count('Sold Out') - 1 > int(open("sold.txt", "rt").read()):
				return "Spectrum", 'BINDER SOLD OUT'
				print('BINDER SOLD OUT')
			else:
				return "Spectrum", str((all.text.count('span class=money') - 5) - (all.text.count('Sold Out') - 1)) + ' AVAILABLE'
				print(str((all.text.count('span class=money') - 5) - (all.text.count('Sold Out') - 1)) + ' AVAILABLE')

	except Exception as exception: # grab error name/type
		return "Spectrum", str(type(exception).__name__) + ' OCCURRED'

	else:
		if debug: return "Spectrum", 'RUN SUCCESSFUL'
		else: return 'BLIP'