import sys
import cs50
#reject anything other than 2 command line arguments
if len(sys.argv)!=2:
    print("Usage: python caesar.py k")
if len(sys.argv)==2:
    #take the key and convert it into an integer
    k=int(sys.argv[1])
    #prompt user for text and receive a string
    print("plaintext: ",end="")
    plaintext=cs50.get_string()
    print("ciphertext: ",end="")
    #convert only alphabetical characters in string and maintain case
    for letter in plaintext:
        if letter.isalpha():
            if letter.islower():
                print("{}".format(chr((ord(letter)-97+k)%26+97)), end="")
            else:
                print("{}".format(chr((ord(letter)-65+k)%26+65)), end="")
        else:
            #if not alphabetical just print character
            print(letter)
    print("\n", end="")
    