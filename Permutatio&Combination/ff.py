

def fact(x):
    if(x==0 or x==1):
        y=1
        return (y)
    else:
        y=x*fact(x-1)
        return (y)
