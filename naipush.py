import os # to securely store pushbullet api token
from pushbullet import Pushbullet

pb = Pushbullet(os.environ['TOKEN'])
#print(pb.devices)
a70 = pb.get_device('a70') # my phone

def pushnote(title, note):
    push = a70.push_note(title, note)

def pushlink(title, link):
    push = a70.push_link(title, link)