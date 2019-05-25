#coding:utf-8
# /usr/bin/env python3

"""
Author:Cobrax
Date of creation:12/02/2019
"""

import hashlib
import time
import sys
import os

begin = "\033[93m\033[1m[+]\033[1m\033[93m"     # [+] in Yellow
clear = lambda: os.system("clear")              #Create a function to clear the terminal

class hashFile:

    def __init__(self, file):
        self.name = file                        #Recover the name

    def hash(self):
        """hash()
        It is used to find the file hash md5
        And put it in self.hash
        """
        hasher = hashlib.md5()                  #Initialisation of hasher to md5
        try:
            with open(self.name, "rb") as file: #Open file
                data = file.read()              #Read data
                hasher.update(data)             #Update Hash
                self.hash = hasher.hexdigest()  #self.hash egal the hash of file
        except IOError:                         #File not found
            print("\033[91mFile not found.\033[91m")
            exit(0)                             #Exit the program


def display():                                  #Menu of program
    print(begin + "=" * 48 + "[+]")
    print(begin + "*" * 20 +  "  MENU  "  + "*" * 20 + "[+]")
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")
    return  file1, file2

def result(same, file1, file2, hash1, hash2):
    clear()                                     #Clear the terminal
    rest1, extension1 = file1.split(".")        #Get extension
    rest2, extension2 = file2.split(".")        #Get extension

    resultString = "\033[92mYes ! They are same !\033[92m" if same == True else "\033[91mNo, they are different. \033[91m"

    #Print the result
    print(begin + "File name:\t\033[93m{0}\t\t{1}\033[93m".format(file1,file2))
    print(begin + "File size:\t{0}\t\t{1}".format(str(os.path.getsize(file1)) + "B",str(os.path.getsize(file2)) + "B"))
    print(begin + "Extension:\t{0}\t\t{1}".format("." + extension1, "." + extension2))
    print(begin + "Hash Md5:\t\033[96m{0}\033[96m\t\033[96m{1}\033[96m".format(hash1, hash2))
    print(begin + "Same hash:\t{0}".format(resultString))

if __name__ == '__main__':
    sys.stdout.write("\x1b[8;{0};{1}t".format(20,54))                   #Terminal resize
    clear()                                                             #Clear the terminal
    file1, file2 = display()                                            #Recover the names of files
    hashingFile1, hashingFile2 = hashFile(file1), hashFile(file2)       #Create object
    hashingFile1.hash()                                                 #For each files, find their hash
    hashingFile2.hash()                                             
    same = all([hashFile.hash, hashingFile2.hash])                      #If hashFile.hash egal hashFile2.hash then same is True
    sys.stdout.write("\x1b[8;{0};{1}t".format(20,90))                   #Terminal resize
    result(same, file1, file2, hashingFile1.hash, hashingFile2.hash)    #Call result()
    print("\033[97m")                                                   #Reset normal color
