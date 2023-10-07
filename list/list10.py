n=[2,3,5,2,3,5,6,7,7,8,8]
g={}#parameter String
for i in n:
    if i in g:
        g[i]+=1
    else:
        g[i]=1
print(g)            