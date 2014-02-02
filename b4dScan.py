#!/usr/bin/env python3
'''
______  _____ ___________________                       
___  /_ __  // /______  /__  ___/_____________ ________ ®
__  __ \_  // /__  __  / _____ \ _  ___/_  __ `/__  __ \
_  /_/ //__  __// /_/ /  ____/ / / /__  / /_/ / _  / / /
/_.___/   /_/   \__,_/   /____/  \___/  \__,_/  /_/ /_/   - v0.1				
										
	This is a simple port scanner made in python 3.3
	over 'Tor' proxy socks5 - module required PySocks	

Easy step to install required module is, type in the Terminal:
	
	:$ pip install PySocks 

or download manually from here http://sourceforge.net/projects/pysocks/				
									
	Author: b4d_tR1p
				
	Date  : January 2014	
	Licence : GPL v3 or any later version

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import socket, socks, sys
from datetime import datetime

# Check what time the scan started
t1 = datetime.now()

class PortScan(object):
	def __init__(self, host=None):
		self.host = host or ''	
		
	def Scan(self):
		self.host = str(input('Please enter a host name:~$ '))
		try:
			for port in range(1, 1024):
				# Set default timeout
				socket.setdefaulttimeout(3)
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((self.host, port))
				if result == 0:
					print ('Port {}: \t Open'.format(port) + ' \t Service: \t' + socket.getservbyport(port))
					return port
				# Close socks channel	
				sock.close()
		# We also put in some error handling for catching errors		
		except KeyboardInterrupt:
			print(' You press Crtl+C')
			sys.exit()

		except socket.gaierror:
			print('Hostname could not be resolved. Exiting')
			sys.exit()

		except socket.error:
			print("Couldn't connect to server")
			sys.exit()


	def TorScan(self):
		self.host = str(input('Please enter a host name:~$ '))
		# Using the range function to specify ports (here it will scans all ports between 1 and 1024)
		try:
			for port in range(1, 1024):
				# Building socks channel over Tor proxy
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050, True)
				socket.socket = socks.socksocket
				# Set default timeout
				socket.setdefaulttimeout(3)
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((self.host, port))
				if result == 0:
					print ('Port {}: \t Open'.format(port) + ' \t Service: \t' + socket.getservbyport(port))
					return port
				# Close socks channel	
				sock.close()
		# We also put in some error handling for catching errors		
		except KeyboardInterrupt:
			print(' You press Crtl+C')
			sys.exit()

		except socket.gaierror:
			print('Hostname could not be resolved. Exiting')
			sys.exit()

		except socket.error:
			print("Couldn't connect to server")
			sys.exit()
	

def choice():
	choice = int(input('Choose your entry here:~$ '))
	return choice

# Check time again
t2 = datetime.now()

# Calculates the time for the scanning
total = t2 - t1

def main():
	print('''\n

 _       ___     _ _____                 
| |     /   |   | /  __/                
| |__  / /| | __| \ `--.  ___ __ _ _ __ ®
| '_ \/ /_| |/ _` |`--. \/ __/ _` | '_ \ 
| |_) \___  | (_| /\__/ / (_| (_| | | | |
|.____/   \_/\__,_\____/ \___\___|__| |_| - V0.1\n  
                                           
		1) Scan
		2) TorScan
		3) Exit
		''')
	a = PortScan()
	entry = choice()
	if entry == 1:
		a.Scan()
	elif entry == 2:
		a.TorScan()
	elif entry == 3:
		print('Tnks for using PortScan, bye bye')
		sys.exit()
	else:
		print('Make sure you get a rigth entry, like 1, 2 or 3\n')
		main()
	

if __name__ == '__main__':
	main()
	print('Scanning completed in: ', total)


	

		
	


	



