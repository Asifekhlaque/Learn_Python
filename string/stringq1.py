a="Asif is Rollno 59 He is a BCA From IIBM"
c=1
m=0
n=0
o=0
p=0
for i in a:
    if i==' ':
        c=c+1
print("Words",c)

for i in a:
    if i.isalpha():
        m=m+1
print("Letter",m)

for i in a:
    if i.isupper():
        n=n+1
print("Upper",n)    

for i in a:
    if i.islower():
        o=o+1
print("Lower",o)   

for i in a:
    if i.isdigit():
        p=p+1
print("Digit",p)    