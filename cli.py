import os, git
import pyfiglet as figlet
from colorama import init, Fore
from sys import platform

init(autoreset=True)
banner = figlet.figlet_format('D4RK-CLI', font='small')
path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
path = path + "/tools"

if platform == "win32":
  clear = "cls"
else:
  clear = "clear"

print("Please wait installing requirements! This might take a while so sit back and relax! (Also depends on how fast your internet is...)")
try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain
pipmain(['install', 'pyfiglet'])
pipmain(['install', 'pyngrok'])
pipmain(['install', 'cryptography'])
pipmain(['install', 'colorama'])
pipmain(['install', 'random'])
pipmain(['install', 'screen_brightness_control'])
pipmain(['install', 'speech_recognition'])
os.system(clear)

while True:
  def download(read):
    tool_path = "tools"

    if os.path.exists(tool_path) and os.path.isdir(tool_path):
      os.chdir(tool_path)
      path_exists = 1
    else:
      os.mkdir(tool_path)
      os.chdir(tool_path)
      path_exists = 1

    print("[*] Created 'Tools' Directory at", path)
    if read == 1:
      if os.path.exists("gphish") and os.path.isdir("gphish"):
        print("[*] Tool is already Installed! If you want to Update the tool please update manually...")
      else:
        git.Git(path).clone("https://github.com/D4RKH0R1Z0N/gphish.git")
        print(Fore.BLUE + "[*] Download Done!" + Fore.RESET)
    elif read == 2:
      if os.path.exists("rdp-sploit") and os.path.isdir("rdp-sploit"):
        print("[*] Tool is already Installed! If you want to Update the tool please update manually...")
      else:
        git.Git(path).clone("https://github.com/D4RKH0R1Z0N/rdp-sploit.git")
        print(Fore.BLUE + "[*] Download Done!" + Fore.RESET)
    elif read == 3:
      if os.path.exists("d4rkcrypt") and os.path.isdir("d4rkcrypt"):
        print("[*] Tool is already Installed! If you want to Update the tool please update manually...")
      else:
        git.Git(path).clone("https://github.com/D4RKH0R1Z0N/d4rkcrypt.git")
        print(Fore.BLUE + "[*] Download Done!" + Fore.RESET)
    elif read == 4:
      if os.path.exists("d4rkobf") and os.path.isdir("d4rkobf"):
        print("[*] Tool is already Installed! If you want to Update the tool please update manually...")
      else:
        git.Git(path).clone("https://github.com/D4RKH0R1Z0N/d4rkobf.git")
        print(Fore.BLUE + "[*] Download Done!" + Fore.RESET)
    elif read == 5:
      if os.path.exists("delos") and os.path.isdir("delos"):
        print("[*] Tool is already Installed! If you want to Update the tool please update manually...")
      else:
        git.Git(path).clone("https://github.com/D4RKH0R1Z0N/delos.git")
        print(Fore.BLUE + "[*] Download Done!" + Fore.RESET)
    elif read == 6:
      if os.path.exists("blackout") and os.path.isdir("blackout"):
        print("[*] Tool is already Installed! If you want to Update the tool please update manually...")
      else:
        git.Git(path).clone("https://github.com/D4RKH0R1Z0N/blackout.git")
        print(Fore.BLUE + "[*] Download Done!" + Fore.RESET)
    elif read == 7:
      if os.path.exists("termux-docker") and os.path.isdir("termux-docker"):
        print("[*] Tool is already Installed! If you want to Update the tool please update manually...")
      else:
        git.Git(path).clone("https://github.com/D4RKH0R1Z0N/termux-docker.git")
        print(Fore.BLUE + "[*] Download Done!" + Fore.RESET)
    elif read == 8:
      if os.path.exists("heroku-termux-cli") and os.path.isdir("heroku-termux-cli"):
        print("[*] Tool is already Installed! If you want to Update the tool please update manually...")
      else:
        git.Git(path).clone("https://github.com/D4RKH0R1Z0N/heroku-termux-cli.git")
        print(Fore.BLUE + "[*] Download Done!" + Fore.RESET)
    elif read == 9:
      if os.path.exists("mp3-to-txt") and os.path.isdir("mp3-to-txt"):
        print("[*] Tool is already Installed! If you want to Update the tool please update manually...")
      else:
        git.Git(path).clone("https://github.com/D4RKH0R1Z0N/mp3-to-txt.git")
        print(Fore.BLUE + "[*] Download Done!" + Fore.RESET)
    elif read == 10:
      if os.path.exists("maths-trainer") and os.path.isdir("maths-trainer"):
        print("[*] Tool is already Installed! If you want to Update the tool please update manually...")
      else:
        git.Git(path).clone("https://github.com/D4RKH0R1Z0N/maths-trainer.git")
        print(Fore.BLUE + "[*] Download Done!" + Fore.RESET)
    else:
      print(Fore.RED + "[!] Unknown Error Occurred, Please report at " + Fore.BLUE + "https://github.com/D4RKH0R1Z0N/D4RK-CLI/issues/new" + Fore.RESET)

  print(banner + """  1. GPhish (Available for Web and All OS)
    2. RDP-Sploit (Available for Windows)
    3. D4RKCRYPT (Available for All OS)
    4. D4RKOBF (Available for All OS)
    5. DelOs (Available for All OS)""" + Fore.RED + " [Warning running this will Destroy you computer!] " + Fore.RESET + """
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
      print(Fore.RED + "[!] Please Enter a Valid Option!" + Fore.RESET)
  else:
    print(Fore.RED + "[!] Please Enter a Valid Option!"  + Fore.RESET)
