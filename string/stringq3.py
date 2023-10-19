def is_upper(a):
        m=0
        if a<='Z' and a>='A':
            m+=1
        return m

def vowels(a):
    o=0
    x=0
    for i in a:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            o=o+1
        else:
            x=x+1
    print("Vowels",o)        
    print("Consonants",x) 

def is_lower(a):
    c=0
    for i in a:
        if i<='z' and i>='a':
            c=c+1
        
    return c

def is_digit(a):
    n=0
    for i in a:
        if i<='9' and i>='0':
            n=n+1
    return n
a=input("Enter the string")

while True:
    b=int(input("Press 1 to check upper\nPress 2 to check lower\nPress 3 to check digit\nPress 4 to check total\nPress 5 to check vowels and consonants\nPress 6 to exit"))
    if b==1:
        d=is_upper(a)
        print("Upper",d)
    elif b==2:
        c=is_lower(a)
        print("Lower",c)
    elif b==3:
        e=is_digit(a)
        print("Digit",e)
    elif b==4:
        f=0
        f=is_upper(a)+is_lower(a)+is_digit(a)
        print("Total",f)
    elif b==5:
        print(vowels(a))
    elif b==6:
        exit()
    else:
        print("Wrong input")