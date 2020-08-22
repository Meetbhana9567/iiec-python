import pyttsx3
import os

print("Hi, How can i help ? : "  , end='')

pyttsx3.speak("Hi, How can i help?")

while True:
	p = input()

	if (("run" in p) or  ("execute" in p ) or ("start" in p) or ("open" in p) or ("exec" in p) or ("browse" in p))  and (("chrome" in p) or ("browser" in p)):
	  os.system("start chrome")

	elif (("run" in p) or  ("execute" in p ) or ("start" in p) or ("open" in p) or ("exec" in p) or ("browse" in p)) and  ("opera" in p) :
	  os.system("start opera")
	  
	elif (("run" in p) or  ("execute" in p ) or ("start" in p) or ("open" in p) or ("exec" in p)) and  (("notepad" in p) or ("editor" in p)) :
	  os.system("notepad")
	  
	elif (("run" in p) or  ("execute" in p ) or ("start" in p) or ("open" in p) or ("exec" in p))  and (("player" in p) or ("vlc" in p) or ("video" in p)):
	  os.system("start vlc")

	elif (("run" in p) or  ("execute" in p ) or ("start" in p) or ("open" in p) or ("exec" in p))  and (("player" in p) or ("media" in p) or ("music" in p) or ("sound" in p)):
	  os.system("start wmplayer")

	elif  ("exit" in p)  or ("quit" in p) or ("close" in p) or ("bye" in p):
	  break

	else:
	  print("Sorry, I can't understand")

	print("How can i help you ? : "  , end='')