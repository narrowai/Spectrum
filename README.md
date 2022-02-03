# Spectrum

## running

this code is designed to be hosted on my raspberry pi with screen in the terminal (although only check between 8:00am and 10:59pm).

the purpose is to send a notification through "pushbullet" to my discord whenever a binder becomes available at https://spectrumoutfitters.co.uk/ as these are rarely in stock and sell out fast.

~~when you get updates about stock changes, you can have the code refetch its comparison sample by changeing doupdate.txt to `1`. This will be automatically changed back to `0` once the code stores the more recent copy.~~

the `.update` command can now have the bot refresh its comparison from within discord with no need to open the code.

it now checks specifically the small black binder for availablity and gives a unique notification for that.

can output lines of log file to discord now to futher reduce need to use repl interface.

## future plans

the friend this is built for is also a size small so in future i'd like to check specifically small sizes, however this is difficult to implement as new styles are currently being released. (I'd probably have to screenscrape for the posistion of the small size option and then check for a sold-out marker on it).
