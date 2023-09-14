#Let's make the bill system for a food shop
m1=int(input("Enter the price of shahi panner"))
q1=int(input("Enter the quantity:"))
m2=int(input("Enter the price of Rajhma chaval"))
q2=int(input("Enter the quantity:"))
m3=int(input("Enter the price of Butter Naan"))
q3=int(input("Enter the quantity:"))
m4=int(input("Enter the price of Roti"))
q4=int(input("Enter the quantity:"))
#Add many more food item in the list
#Let's calculate the bill
total=(m1*q1)+(m2*q2)+(m3*q3)+(m4*q4)
print("Total is:",total)
#Let's add tax on it
serviceCharge=total*10/100
print("Service charge will be",serviceCharge)
sgst=total*6/100
print("SGST will be 6%",sgst)
cgst=total*8/100
print("CGST will be 8%",cgst)
gst=cgst+sgst
print("Total tax will in GST is:",gst)
gtotal=total+gst+serviceCharge
print("Total bill including all tax\nand service charge will be",gtotal)
