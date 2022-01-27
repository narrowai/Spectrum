import os
from keepalive import keep_alive # an included python scipt, for 24/7 running
from getweb import updatew, lookw # an included python script, to refresh reference copies of the site
import discord
import naifiles


from discord.ext import tasks


import time
starttime = time.time() # thing for timing thing. don't qestion me.

keep_alive() # set up webserver for uptime robot to ping

#----------------------------------------------------------------
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
	thisloop.start()

@tasks.loop(seconds=60)
async def thisloop():
	hour = int(time.strftime("%H", time.localtime())) # save current hour as int 'hour', 0-24 format
	if hour > 7 and hour < 23: # is time between 8:00am and 10:59pm?
		print('DEBUG: running @ hour', hour)
		if open("doupdate.txt", "rt").read() == '1':
			updatew(True) # fetches comparison files, with option to spit out values to terminal
			with open('doupdate.txt','w') as upd: upd.write('0') # resets the update instuction so it's not constanly fetching
		look = lookw() # actually runs all the checking and notifying code
		if look != 'BLIP':

			for i in naifiles.readlist('notifies.txt'):
				await client.get_channel(int(i)).send(f"<@541391046681034762> {look[1]}")
			print('NOTIFICATION ATTEMPTED:', look[1])

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
		channels = naifiles.readlist('notifies.txt')
		if str(message.channel.id) in channels:
			naifiles.sublist('notifies.txt',[str(message.channel.id)])
			await message.channel.send('notifications disabled for this channel')
		else:
			naifiles.addlist('notifies.txt',[str(message.channel.id)])
			await message.channel.send('notifications enabled for this channel')
	elif command[0] == 'update':
		updatew()
		await message.channel.send('updated')
	elif command[0] == 'test':
		await message.channel.send('<@541391046681034762> example notification')
	else: await message.channel.send(f'{command} command not recognised')

client.run(TOKEN)