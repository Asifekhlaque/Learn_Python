Name=["ss","mm","zz","sp","sa"]
city=["patna","delhi","patna","delhi","mp"]
pa=[]
de=[]
p=0
d=0
for i in range(len(city)):
    if city[i]=="patna":
        pa.append(Name[i])
        p=p+1
    elif city[i]=="delhi":
        de.append(Name[i])
        d=d+1
print("patna",pa,p)
print("delhi",de,d)        