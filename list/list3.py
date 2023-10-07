Name=["aa","bb","cc","dd"]
city=["patna","delhi","indore","mumbai"]
id=["ss002","mm002","mk002","sn002"]
inp=input("Enter id")
for i in range(0,4):
    if id[i]==inp:
        print(city[i])
        print(Name[i])