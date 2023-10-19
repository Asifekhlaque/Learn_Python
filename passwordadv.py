password=input("Enter password")
sp="@#%&"
m=0

if len(password)>=8:
        if not any(i.isupper() for i in password):
            m=m+1
            print("Upper case not found")
        if not any(i.islower() for i in password):
            m=m+1
            print("Lower case not found")
        if not any(i.isdigit() for i in password):
            m=m+1
            print("Digit not found")
        if not any(i in sp for i in password):
            m=m+1
            print("Special char not found")
else:
    print("Enter 8 Char")
if m==0:
    print("Password correct")   
else:
    print("No correct")   