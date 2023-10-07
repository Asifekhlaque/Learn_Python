x=0
y=0
li=[40,60,85,25,8,12]
for i in range(6):
    if(li[i]%2==0):
        x=x+li[i]
    else:
        y=y+li[i]
print("Sum of odd",y)
print("sum of even",x)        