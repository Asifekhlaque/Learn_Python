password=input("Enter password")
sp="@#%&"
a=False
b=False
c=False
d=False

if len(password)>=8:
    for i in password:
        if i.isupper():
            a=True
        if i.islower():
            b=True
        if i.isdigit():
            c=True
        if i in sp:
            d=True
else:
    print("Enter 8 Char")
if a==True and b==True and c==True and d==True:
    print("Password correct")   
else:
    print("No correct")   