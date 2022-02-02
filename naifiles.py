import time # for logs

def writelist(file, inlist):
    with open(file,'w') as m:
        for i in inlist:
            m.write(i)
            m.write('\n')

def readlist(file):
    with open(file,'r') as n:
        return [links.rstrip() for links in n]

def exlist(inlist, exlist): # exlist is what you DON'T want in the result
    return [j for j in inlist if j not in exlist]

def addlist(file, inlist):
    oldlist = readlist(file)
    newlist = exlist(inlist, oldlist)
    writelist(file, oldlist+newlist)

def sublist(file, outlist):
    oldlist = readlist(file)
    newlist = exlist(oldlist, outlist)
    writelist(file, newlist)

def log(message, file='log.txt', stamp=True):
	with open(file,'a') as l:
		if stamp == True: l.write('\n' + time.strftime("%d/%m %H:%M:%S ") + message)
		else: l.write('\n' + message)