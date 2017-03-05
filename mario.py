import cs50
#prompt user for input
print("Input Height")
h=cs50.get_int()
#check to see if height is valid
if (h>1 or h<23):
    #iterate through rows
    for i in range(0,h):
        #print space characters
        for j in range(0,h-i-1):
            print(" ", end="")
        #print hashes
        for k in range(0,i+2):
            print("#", end="")
        print("\n", end="")
    
    
    

    
        