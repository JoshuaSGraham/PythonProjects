import crypt
import hashlib
import argparse
# Displays to the user a success message or failiure message depedning on if the password is found
def printOutput(passwordFound, passwordCracked, username):
    if(passwordFound):
        print("[+] Password Found: "+username + ":"+passwordCracked)
    else:
        print("[ - ] No password found for "+username)
# Cracks a md5 hash
def MD5crack(encryptedPassword, wordlist, username):
    # Gets the hash salt from 2 position of the password passed through
    salt = encryptedPassword[0:2]
    # Reads in all of the passwords from the file
    passwordFile = open(wordlist, 'r')
    for password in passwordFile.readlines():
        password = password.strip('\n')
        # Hashes all of the passwords with their salt and compares to the password hash that we are trying to find
        encryptedWord = crypt.crypt(password,salt)
        # If they match we have found the password we are trying to find
        if (encryptedWord == encryptedPassword):
            printOutput(True, encryptedWord, username)
            return
    printOutput(False, encryptedPassword, username)
# Cracks a sha512 hash
def SHA512crack(encryptedPassword, wordlist, username):
    # Gets the hash salt from the 2nd position of the password passed through
    salt = encryptedPassword[0:2]
    # Reads in all of the passwords from the file
    passwordFile = open(wordlist,'r')
    for password in passwordFile.readlines():
        password = password.strip('\n')
        # Hashes all of the passwords with their salt and compares to the password hash that we are trying to find
        encryptedWord = hashlib.sha512(password, salt)
        encryptedWord.hexdigest()
        # If they match we have found the password we are trying to find
        if (encryptedWord == encryptedPassword):
            printOutput(True, encryptedWord, username)
            return
    printOutput(False, encryptedPassword, username)
# Cracks a sha1 hash
def SHA1crack(encryptedPassword, wordlist, username):
    # Gets the hash salt from the 2nd position of the password passed through
    salt = encryptedPassword[0:2]
    # Reads in all of the passwords from the file
    passwordFile = open(wordlist,'r')
    for password in passwordFile.readlines():
        password = password.strip('\n')
        # Hashes all of the passwords with their salt and compares to the password hash that we are trying to find
        encryptedWord = hashlib.sha1(password, salt)
        encryptedWord.hexdigest()
        # If they match we have found the password we are trying to find
        if (encryptedWord == encryptedPassword):
            printOutput(True, encryptedWord, username)
            return
    printOutput(False, encryptedPassword, username)
# Cracks a sha256 hash
def SHA256crack(encryptedPassword, wordlist, username):
    # Gets the hash salt from the 2nd position of the password passed through
    salt = encryptedPassword[0:2]
    # Reads in all of the passwords from the file
    passwordFile = open(wordlist,'r')
    for password in passwordFile.readlines():
        password = password.strip('\n')
        # Hashes all of the passwords with their salt and compares to the password hash that we are trying to find
        encryptedWord = hashlib.sha256(password, salt)
        encryptedWord.hexdigest()
        # If they match we have found the password we are trying to find
        if (encryptedWord == encryptedPassword):
            printOutput(True, encryptedWord, username)
            return
    printOutput(False, encryptedPassword, username)


def readFile(hashFile, wordlist, algorithm):
    # Reads in username, password hashes and their salts to be cracked
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