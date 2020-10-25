import os #operating systems related functions like opening, closing files
from Crypto.Cipher import AES # main packages installed
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(key,filename): #filename is the photo's name and conversion key is the password
    chunksize=64 *1024
    outputFile= "(encry)" + filename #we are saving the encrypted photo name with this extension
    filesize= str(os.path.getsize(filename)).zfill(16)  #gets the AES block size which is 16
    iv=Random.new().read(16) # generates a random initialization vector

    encryptor= AES.new(key, AES.MODE_CBC, iv) #defines the mode of AES which is cipher Block chaining mode

    with open(filename,'rb') as infile: #opens the photo
        with open(outputFile,'wb') as outfile:
            outfile.write(filesize.encode('utf-8')) #encrypts the photo
            outfile.write(iv)

            while True:
                chunk= infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 !=0: #checks if the length of the chunk is same as the AES block size; if not control comes out
                    chunk += b' '* (16-(len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk)) #the encrypted file is returned back

def decrypt(key,filename): #for decrypting the photo
    chunksize= 64 * 1024
    outputFile = filename[11:]

    with open(filename, 'rb') as infile: #reads the file name in binary format
        filesize= int(infile.read(16))
        iv= infile.read(16)

        decryptor= AES.new(key, AES.MODE_CBC, iv)

        with open(outputFile,'wb') as outfile:
            while True:
                chunk= infile.read(chunksize)

                if len(chunk)== 0:
                    break

                outfile.write(decryptor.decrypt(chunk)) #returns the decrypted file
            outfile.truncate(filesize) #removes any spaces in the file if any and truncates to the original size

def getKey(password): # gets the key for both encryption and decryption
    hasher=  SHA256.new(password.encode('utf-8')) #sha256 is a good way to store user's passwords
    return hasher.digest()

def Main(): #the user input part
    choice= input("Would you like to (E)ncrypt or (D)ecrypt?:") #takes the choice of the user
    if choice == 'E' or choice == 'e':
        filename = input("Photo to encrypt:")
        password = input("Password:")
        encrypt(getKey(password), filename)
        print("Done")
    elif choice == 'D' or choice == 'd':
        filename= input(" Photo to decrypt:")
        password= input("Password:")
        decrypt(getKey(password), filename)
        print("Done")
    else:
        print("No option selected. closing...")

if __name__ == '__main__':
    Main()
