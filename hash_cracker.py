import os

def cracker():
    try:
        print("Please input password hash from your clipboard")
        input_hash = input(": ")
        os.chdir("G:\cracking\hashcat-6.2.5")
        os.system("hashcat.exe -m 0 -a 0 "+input_hash+ " G:\cracking\wordlists.txt")
        print("\n")
        os.system("hashcat.exe -m 0 -a 0 "+input_hash+ " G:\cracking\wordlists.txt --show")
        print("\n")
    except Exception as error:
        print(error)
        
# cracker()