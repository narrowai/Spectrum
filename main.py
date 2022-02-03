import os
from getweb import updatew, lookw, checkf # an included python script, to refresh reference copies of the site
import discord
import naifiles

from discord.ext import tasks # George's library

import time

naifiles.log('', stamp=False)
naifiles.log('CODE TURNED ON')
#----------------------------------------------------------------

TOKEN = naifiles.readlist('token.txt')[0]
client = discord.Client()
notifs = 0

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
	naifiles.log(f'{client.user} has connected to Discord!')
	mainloop.start()

@tasks.loop(seconds=60)
async def mainloop():
	global notifs
	hour = int(time.strftime("%H", time.localtime())) # save current hour as int 'hour', 0-24 format
	if hour > 7 and hour < 23: # is time between 8:00am and 10:59pm?
		if int(time.strftime('%M', time.localtime())) == 0: naifiles.log('DEBUG: running')
		checkf() # checks the (depricated) update file
		look = lookw() # actually runs all the checking and notifying code

		if look != 'BLIP': #if it actually returns something
			for i in naifiles.readlist('channels.txt'):
				await client.get_channel(int(i)).send(f"<@541391046681034762> {look[1]} https://bit.ly/naispec")
			naifiles.log(f'NOTIFICATION ATTEMPTED: {look[1]}')
			notifs -=- 1
			if notifs == 5:
				updatew()
				notifs = 0



@client.event
async def on_message(message):
	if message.author == client.user: return
	if message.content[0] !='.': return
	command = message.content[1:].split()

	if command[0] == 'help':
		await message.channel.send('''notifyhere - toggle notificatins for this channel
update - refresh the grab of the spectrum webpage
test - no touchie pls ;)''')

	elif command[0] == 'notifyhere':
		channels = naifiles.readlist('channels.txt')
		if str(message.channel.id) in channels:
			naifiles.sublist('channels.txt',[str(message.channel.id)])
			await message.channel.send('notifications disabled for this channel')
		else:
			naifiles.addlist('channels.txt',[str(message.channel.id)])
			await message.channel.send('notifications enabled for this channel')

	elif command[0] == 'update':
		updatew()
		await message.channel.send('updated')

	elif command[0] == 'test':
		await message.channel.send('<@541391046681034762> example notification https://bit.ly/naispec')

	elif command[0] == 'logs':
		if len(command) < 2: command.append(10)
		sendlogs = naifiles.readlist('log.txt')[0-int(command[1]):]
		messagers = '```'
		for i in sendlogs: messagers += '\n'+i
		messagers += '```'
		await message.channel.send(f'last {int(command[1])} logs:\n{messagers}')

	else: await message.channel.send(f'{command} command not recognised')


client.run(TOKEN)