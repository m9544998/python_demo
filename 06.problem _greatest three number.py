
def greatest(a,b,c):
    if(a>=b and a>=c):
        print(f"The greatest number is:{a}")
        return a
    elif(b>=a and b>=c):
        print(f"The greatest number is:{b}")
        return b
    else:
        print(f"The greatest number is:{c}")
        return c
a=1
b=89
c=33
print(greatest(a,b,c))
