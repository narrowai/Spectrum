import requests # to get the html code from the websites
from naifiles import log


def updatew(debug=False):

	all = requests.get('https://spectrumoutfitters.co.uk/collections/short-binders')

	text = str(all.text.encode('ascii', 'replace'))

	start,end='class="grid grid--uniform','</div></div></div>'
	start,end=text.find(start),text.find(end)+19
	#if debug: print(start,end)

	with open('grid.txt','w') as grid:
		grid.write(text[start:end])

	with open('sold.txt','w') as sold:
		sold.write(str(text.count('Sold Out')-1))

	log('UPDATING sold out: ' + str(text.count('Sold Out')-1))


def lookw(debug=False):
	try:
		black = requests.get('https://spectrumoutfitters.co.uk/collections/short-binders/products/black-short-chest-binder?variant=15857211473963')
		all = requests.get('https://spectrumoutfitters.co.uk/collections/short-binders')

		'''if not '<span data-add-to-cart-text data-default-text="Add to cart">\n        Sold Out\n      </span>' in black.text:
			return "Spectrum", 'BLACK BINDER AVAILIBLE'
			print('BLACK BINDER AVAILABLE')'''

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
		else: return 'BLIP' # NULL return if request returns with no difference


def checkf():
	if open("doupdate.txt", "rt").read() == '1':
				updatew(True) # fetches comparison files, with option to spit out values to terminal
				with open('doupdate.txt','w') as upd: upd.write('0') # resets the update instuction so it's not constanly fetching