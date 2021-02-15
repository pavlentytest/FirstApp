a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c
if(d < 0):
    print("not")
elif(d > 0):
    print("two")
else:
    print("one")