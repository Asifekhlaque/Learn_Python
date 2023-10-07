l1=[13,18,12,17,19,8,90]
l2=[]
l3=[]
for i in range(len(l1)):
    if l1[i]<18:
        l2.append(l1[i])
    else:
        l3.append(l1[i])    
print("less then 18",l2)
print("More then 18",l3)        