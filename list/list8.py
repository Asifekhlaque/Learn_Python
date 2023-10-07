lis=[]
for i in range(11):
    n=input("Enter")
    lis.append(n)
for j in range(11):
    print(lis[j],end=" ")
lis.sort()
print(lis)