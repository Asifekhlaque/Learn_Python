n=[2,3,5,2,3,5,6,7,7,8,8]
dup=[]
for i in range(len(n)):
    for j in range(len(n)):
        if j+1< len(n):
                print(n[i])