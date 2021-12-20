# Spectrum

## running

this code is designed to be hosted on repl.it, using uptime robot to keep it online 24/7.

the purpose is to send a notification through pushbullet to my phone whenever a binder becomes available at https://spectrumoutfitters.co.uk/ as these are rarely in stock and sell out fast.

when you get updates about stock changes, you can have the code update its comparison sample by changeing doupdate.txt to 1. This will be automatically changed back to 0 once the code updates itself.


## future plans

there are plans to have it only check during a certain time frame (like crontab did when it was hosted on my rpi) however these are not yet in place.
the friend this is built for is also a size small so in future i'd like to check specifically small sizes, however this is difficult to implement as new styles are currently being released.
