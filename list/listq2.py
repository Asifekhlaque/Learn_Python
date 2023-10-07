Name=["aa","bb","cc","dd"]
city=["patna","delhi","indore","mumbai"]
id=["ss002","mm002","mk002","sn002"]
inp=input("Enter id")
if inp=="ss002":
    print(id[0])
    print(Name[0])
    print(city[0])
elif inp=="mm002":  
    print(id[1])
    print(Name[1])
    print(city[1])
elif inp=="mk002":  
    print(id[2])
    print(Name[2])
    print(city[2])    
elif inp=="sn002":  
    print(id[3])
    print(Name[3])
    print(city[3])    
else:
    print("Enter correct input")    