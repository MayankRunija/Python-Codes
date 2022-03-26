
# print("Program for factorial of number ")
def fact(x):
    if(x==0 or x==1):
        y=1
        return (y)
    else:
        y=x*fact(x-1)
        return (y)
# val=int(input("Enter a value : "))
# funct_val=fact(val)
# print("factorial of {} is {} ".format(val,funct_val))
from ff import fact
n=int(input("Enter a total items : "))
r=int(input("Enter the no of item to be arrange : "))
fact_x=1
for i in range (1,(n-r)+1):
    fact_x*=1
p= fact(n)/fact(n-r)
print(p)

c= fact(n)/fact((n-r)*r)
print(c)
