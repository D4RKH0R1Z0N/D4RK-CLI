# Not working
print("This script is currently in development so this might not work and doesn't work")
print("Exitting... Remove exit statement in line 4, to countinue using this experimental not working useless unnecessary script")
exit()

import os
import pyfiglet as figlet
from colorama import init, Fore
from git_clone import git_clone

init(autoreset=True)
banner = figlet.figlet_format('D4RK-CLI', font='small')
path = "tools"

def download(read):
	tool_path = "tools"

	if os.path.exists(tool_path) and os.path.isdir(tool_path):
		os.chdir(tool_path)
		path_exists = 1
	else:
		os.mkdir(tool_path)
		path_exists = 1
	print("[*] Created 'Tools' Directory")
	if read == 1:
		# git_clone('https://github.com/D4RKH0R1Z0N/gphish.git', '/tools')
		print("Download Done!")
	elif read == 2:
		git_clone('https://github.com/D4RKH0R1Z0N/rdp-sploit.git')
		print("Download Done!")
	elif read == 2:
		git_clone('https://github.com/D4RKH0R1Z0N/gphish.git')
		print("Download Done!")
	elif read == 2:
		git_clone('https://github.com/D4RKH0R1Z0N/gphish.git')
		print("Download Done!")
	elif read == 2:
		git_clone('https://github.com/D4RKH0R1Z0N/gphish.git')
		print("Download Done!")
	elif read == 2:
		git_clone('https://github.com/D4RKH0R1Z0N/gphish.git')
		print("Download Done!")
	elif read == 2:
		git_clone('https://github.com/D4RKH0R1Z0N/gphish.git')
		print("Download Done!")
	elif read == 2:
		git_clone('https://github.com/D4RKH0R1Z0N/gphish.git')
		print("Download Done!")
	elif read == 2:
		git_clone('https://github.com/D4RKH0R1Z0N/gphish.git')
		print("Download Done!")
	elif read == 2:
		git_clone('https://github.com/D4RKH0R1Z0N/gphish.git')
		print("Download Done!")
	else:
		print(Fore.RED + "[!] Unknown Error Occurred, Please report at " + Fore.BLUE + "https://github.com/D4RKH0R1Z0N/D4RK-CLI/issues/new")

print(banner + """  1. GPhish (Available for Web and All OS)
  2. RDP-Sploit (Available for Windows)
  3. D4RKCRYPT (Available for All OS)
  4. D4RKOBF (Available for All OS)
  5. DelOs (Available for All OS)""" + Fore.RED + " [Warning runing this will Destroy you computer!] " + """
  6. blackout (Available for Windows)
  7. termux-docker (Available for Android)
  8. heroku-termux-cli (Available for Android)
  9. mp3-to-txt (Available for All OS)
  10. maths-trainer (Available for All OS)
""")

read = input("Enter Which Tool to Download : ")

if read.isdigit():
	read = int(read)
	if read == 1:
		download(1)
	elif read == 2:
		download(2)
	elif read == 3:
		download(3)
	elif read == 4:
		download(4)
	elif read == 5:
		download(5)
	elif read == 6:
		download(6)
	elif read == 7:
		download(7)
	elif read == 8:
		download(8)
	elif read == 9:
		download(9)
	elif read == 10:
		download(10)
	else:
		print(Fore.RED + "[!] Please Enter a Valid Option!")
else:
	print(Fore.RED + "[!] Please Enter a Valid Option!")
