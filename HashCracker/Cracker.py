import crypt
import hashlib
import argparse
def printOutput(passwordFound, passwordCracked, username):
    if(passwordFound):
        print("[+] Password Found: "+username + ":"+passwordCracked)
    else:
        print("[ - ] No password found for "+username)

def MD5crack(encryptedPassword, wordlist, username):
    salt = encryptedPassword[0:2]
    passwordFile = open(wordlist, 'r')
    for password in passwordFile.readlines():
        password = password.strip('\n')
        encryptedWord = crypt.crypt(password,salt)
        if (encryptedWord == encryptedPassword):
            printOutput(True, encryptedWord, username)
            return
    printOutput(False, encryptedPassword, username)

def SHA512crack(encryptedPassword, wordlist, username):
    salt = encryptedPassword[0:2]
    passwordFile = open(wordlist,'r')
    for password in passwordFile.readlines():
        password = password.strip('\n')
        encryptedWord = hashlib.sha512(password, salt)
        encryptedWord.hexdigest()
        if (encryptedWord == encryptedPassword):
            printOutput(True, encryptedWord, username)
            return
    printOutput(False, encryptedPassword, username)

def SHA1crack(encryptedPassword, wordlist, username):
    salt = encryptedPassword[0:2]
    passwordFile = open(wordlist,'r')
    for password in passwordFile.readlines():
        password = password.strip('\n')
        encryptedWord = hashlib.sha1(password, salt)
        encryptedWord.hexdigest()
        if (encryptedWord == encryptedPassword):
            printOutput(True, encryptedWord, username)
            return
    printOutput(False, encryptedPassword, username)
    
def SHA256crack(encryptedPassword, wordlist, username):
    salt = encryptedPassword[0:2]
    passwordFile = open(wordlist,'r')
    for password in passwordFile.readlines():
        password = password.strip('\n')
        encryptedWord = hashlib.sha256(password, salt)
        encryptedWord.hexdigest()
        if (encryptedWord == encryptedPassword):
            printOutput(True, encryptedWord, username)
            return
    printOutput(False, encryptedPassword, username)


def readFile(hashFile, wordlist, algorithm):

    passFile = open(hashFile, 'r')
    for line in passFile.readlines():
            if ":" in line:
                user = line.split(':')[0]
                encryptedPassword = line.split(':')[1].strip(' ')
                print("[*] Cracking Password Hash for: "+user)
                if(algorithm == ""):
                     MD5crack(encryptedPassword, wordlist, user)
                elif (algorithm == "sha1"):
                    SHA1crack(encryptedPassword, wordlist, user)
                elif (algorithm == "sha256"):
                    SHA256crack(encryptedPassword, wordlist, user)
                elif (algorithm == "sha512"):
                    SHA512crack(encryptedPassword, wordlist, user)

def main():

    parser = argparse.ArgumentParser(description="Crack Hashses")
    parser.add_argument("-h", "--hashlist", metavar="HashList", type=str, required=True, help="Hashfile containing hashes to be cracked with their salts")
    parser.add_argument("-w", "--wordlist", metavar="WordList", type=str, required=True, help="Word list for cracking the hash")
    parser.add_argument("-c", "--crack", metavar="Crack", type=str, required=False, help="Specify what hashing algorithm is to be used")
    args = parser.parse_args()
    readFile(args.hashlist,args.wordlist, args.crack)

if __name__ == "__main__":
    main()