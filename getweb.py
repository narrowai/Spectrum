import requests

def getweb(debug=False):

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


#dump = open('dump.txt','w')
#dump.write(str(all.text.encode('ascii', 'replace')))
#dump.close()

#grid = open('grid.txt','w')
#grid.write(str(all.text.encode('ascii', 'replace'))[79349:117440])
#grid.close()