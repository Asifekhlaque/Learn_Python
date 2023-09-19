# Lets make a programe an electricty bill
unit=int(input("Enter the unit:"))
if unit<=0 or unit<=199:
    print("No Bill")
elif unit>=200 or unit<=299:
    print("Bill is:",(unit-199)*4)
elif unit>=300 or unit<=499:
    print("Bill is:",(unit-299)*8)
else:
    print("Bill is:",(unit-399)*10)
