import os
import subprocess as system

def system_choice():
  system_ = input("1)WINDOWS , 2)LINUX / :")
  if system_ == "1" or "w":
    ip = input("[+]IP->")

    os.system("nmap -sS -sV -p- --min-rate 5000 -n "+ ip +" -Pn")
  elif system_ == "2" or "l":

      system.call("nmap -sS -sV -p- --min-rate 5000 -n "+ ip +" -Pn" , shell = True)


system_choice()

   
    
