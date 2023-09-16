#lets make a program to the salery of employer
empSal=int(input("Enter your salery"))
if empSal>10000:
    hra=empSal*0.1
    pf=empSal*0.2
    medical=500
    bonus=2500
    TempSal=hra+pf+medical+bonus+empSal
    print("Your Basic Salary is",empSal,
          "\nAnd you are consider as chart 1 type"
          "\nNow your salary is",TempSal)
else:
    hra=empSal*0.2
    pf=empSal*0.4
    medical=680
    bonus=280
    TempSal=hra+pf+medical+bonus+empSal
    print("Your Basic Salary",empSal,
          "\nAnd you are consider as chart 2 type"
          "\nNow your salary is",TempSal)
    
    

    
