def getweb():

	import requests

	all = requests.get('https://spectrumoutfitters.co.uk/collections/short-binders')

	text = str(all.text.encode('ascii', 'replace'))


	dump = open('dump.txt','w')
	dump.write(text)
	dump.close()


	start,end='class="grid grid--uniform','</div></div></div>'
	start,end=text.find(start),text.find(end)+19
	print(start,end)

	grid = open('grid.txt','w')
	grid.write(text[start:end])
	grid.close()

	sold = open('sold.txt','w')
	sold.write(str(text.count('Sold Out')-1))
	sold.close()
	print(str(text.count('Sold Out')-1))


#dump = open('dump.txt','w')
#dump.write(str(all.text.encode('ascii', 'replace')))
#dump.close()

#grid = open('grid.txt','w')
#grid.write(str(all.text.encode('ascii', 'replace'))[79349:117440])
#grid.close()