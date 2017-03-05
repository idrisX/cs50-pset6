import cs50
#prompt user for amount of change owed
print("How much change is owed?")
n=cs50.get_float()
#initialize counting variable for number of coins
i=0
#turn the amount of change into an integer 
n=int(n*100)
#collect quaters
while(n>=25):
    i=i+1
    n=n-25
    
#collect dimes
while(n>=10):
    i=i+1
    n=n-10
    
#collect nickles
while(n>=5):
    i=i+1
    n=n-5
#collect pennies
while(n>=1):
    i=i+1;
    n=n-5;
#show number of coins
if i==1:
    print("You get {} coin".format(i))
else:
    print("You get {} coins".format(i))