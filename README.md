# PythonProjects
A collection of smaller python projects and scripts that I have written.

## HashCracker
HashCracker is a small script for offline cracking of passwords.

## Usage:
```
python3 Cracker.py -h/--hashlist <file containing hash/es to be cracked> -w/--wordlist <file>

Optional:
-c/--crack <SHA1, SHA256, SHA512> or no -c option for md5sum
```

## FTPCompromiser
A script designed to quickly automate the process of trying anonymous login and brute forcing users

## Usage:
### Linux
```
python3 FTPCompromiser.py -t <Ip address> -w <wordlist>

Optional:

-x sets extentions to look for in files on the ftp server once access has been gained
```

## Matching brackets
Matching brackets is a small program that I made that takes a user inputted string and checks if the brackets are equal on both sides using a stack data structure.

## Usage:

### Windows
```
py.exe main.py <string>
```

### Linux
```
python3 main.py <string>
```