a=int(input("Enter 1st value :"))
b=int(input("Enter 2nd value :"))
c=int(input("Enter 3rd value :"))
max=0
min=0
if(a==b==c):
    print("All values are equal")
elif(a>b)and (a>c):
    print(a, "is Maximum")
elif (b>c):
    print(b, "is Maximum")
else:
    print(c, "is Maximum")

if(a<b)and (a<c):
    print(a, " is Manimum")
elif (b<c):
    print(b, "is Manimum")
else:
    print(c, "is Manimum")
