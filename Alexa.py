from scripts.record import *

hot_word=False
while(1):
	try:
		if hot_word==True:
			success=record_command()
			hot_word=success
		else:
			hot_word=record_alexa()
	except (KeyboardInterrupt, SystemExit):
	    raise
