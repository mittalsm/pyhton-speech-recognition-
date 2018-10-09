#WAP to find the factorial of a number

n=int(raw_input("enter any number:"))
fact=1
while (n>0):
             fact=fact*n
             n=n-1
print "The factorial of a given number:",fact
