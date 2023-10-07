# find the square root form 1 to 5. But only even number. And find the cube of odd number form 6 to 10 using single for loop
# solution 1:
for i in range(1,10,1):
    if i<=5:
        if i%2==0:
            print("Square",i*i)
    else:
        if i%2!=0:
            print("Cube",i*i*i)
# solution 2:
for i in range(1,10,1):
    if i<=5 and i%2:
            print("Square",i*i)
    elif i>5 and i%2!=0:
        print("Cube",i*i*i)
