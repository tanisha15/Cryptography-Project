# Cryptography Project
Cryptographic Algorithms used in the Defence sector

## Methodology
* Basically we will be working on the AES and DES algorithms and observe which among the two would be better for military organizations. We would observe the time and the memory utilization of both the algorithms to come to the conclusion. Then we would be developing a secure file encryption and decryption using the Military grade encryption which is the AES 256 Encryption. We would be using a tkinter window for this purpose and it would help us to load our file for encryption or decryption. We would also be developing secure image encryption and decryption using the AES256 and SHA algorithms.

1.	First we import the dependencies and all the packages-pycryptodome and import the methods of the Crypto package like AES, SHA.
2.	First we generate a random key using SHA to encrypt and decrypt the images or files. We use only one key for both.
3.	Next we pad the message to obtain the message length same as that of the AES block size.
4.	Next we apply the encrypt function to the padded message and we make an initialization vector to prevent the repetition in encryption and generate the cipher key. We return the cipher key combined with the initialization vector.
5.	To decrypt the file/image we take the initialization vector part of the cipher text and convert it into plain text of AES block size. Now we return the plaintext after removing all extra padded parts using the rstrip function.
6.	Now we will encrypt a file, so we open the file and read it as binary and then we store the text/image from the file. We encrypt the text/image and create a new file with a different `encry`extension.
7.	Now we work on the GUI part where we load the text file from the user. First we open the file address and if a file is selected, we set the global variable to the selected file’s name.
8.	Next we encrypt the selected file and if no file is selected it shows an error.
9.	 Next we decrypt the encrypted file after loading it from the user.
10.	 Then we create a GUI window using the tkinter package. So first we are giving the title of the window with an icon photo and we fix the size of the window.
11.	 Then we load the buttons of the window with their respective commands.
12.	 And we attach the buttons to the window using the pack() method.

## Requirements/Tools~
* Python 3 installed
* DeV C++ installed
* `pycryptodome` package installed
* `pyautogui` package installed
* Test image is provided as well as the icon photo for the GUI window

## Contributors
Tanisha Rakshit 
Aayush Shrestha
Hemanth Vadlapudi
Kotha Hemanth Kumar


