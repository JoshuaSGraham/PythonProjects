import crypt
import hashlib
def MD5crack(encryptedPassword):
    salt = encryptedPassword[0:2]
    passwordFile = open('password.txt', 'r')
    for password in passwordFile.readlines():
        password = password.strip('\n')
        encryptedWord = crypt.crypt(password,salt)
        if (encryptedWord == encryptedPassword):
            print("[+] Password Found: "+password +"\n")
            return
    print("[ - ] Password not found \n")
    return

def SHA512Crack(encryptedPassword):
    salt = encryptedPassword[0:2]
    passwordFile = open('password.txt','r')
    for password in passwordFile.readlines():
        password = password.strip('\n')
        encryptedWord = hashlib.sha512(password, salt)
        encryptedWord.hexdigest()
        if (encryptedWord == encryptedPassword):
            print("[+} Password Found: "+password+"\n")
            return
    print("[ - ] Password not found \n")

def main():
    passFile = open('crack.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            encryptedPassword = line.split(':')[1].strip(' ')
            print("[*] Cracking Password Hash for: "+user)
            MD5crack(encryptedPassword)
if __name__ == "__main__":
    main()

