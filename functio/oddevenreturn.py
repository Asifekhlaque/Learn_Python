def odd_even(x):
    if x%2==0:
        return True
a=int(input("Enter a number"))
b=odd_even(a)
if b:
    print("Even")
else:
    print("Odd")