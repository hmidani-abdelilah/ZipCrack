#!/usr/bin/env python3
# Author: @haithamaouati
# Version:1.0

import argparse
import colorama
import os
from termcolor import colored
from tqdm import tqdm
import zipfile

from colorama import Fore, Back, Style
colorama.init()

os.system('cls' if os.name == 'nt' else 'clear')

print('''\

  _______        _____                _      
 |___  (_)      / ____|              | |     
    / / _ _ __ | |     _ __ __ _  ___| | __  
   / / | | '_ \| |    | '__/ _` |/ __| |/ /  
  / /__| | |_) | |____| | | (_| | (__|   < _ 
 /_____|_| .__/ \_____|_|  \__,_|\___|_|\_(_)
         | |                                 
         |_|                                 
''')

print('Author: ' + Fore.CYAN + '@haithamaouati' + Fore.WHITE + ' Version: ' + Fore.YELLOW + '1.0\n' + Fore.WHITE)

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', metavar='<file>', type=str, help='Zip file (e.g. file.zip)')
parser.add_argument('-w', '--wordlist', metavar='<wordlist>', type=str, help='Wordlist file (e.g. wordlist.txt)')

args = parser.parse_args()

if args.file == None or args.wordlist == None:
  parser.print_help()
  exit();
file = args.file
wordlist = args.wordlist

var =""
listword = [passwords.strip() for passwords in open(wordlist)]
zip_file = zipfile.ZipFile(file)

for i in tqdm(listword,desc="[*] Craking password"):
  try:
    zip_file.extractall(pwd=i.encode())
    var=i
    break
  except:
    continue
print(colored("[+] Password Found: {}".format(var), 'green'))