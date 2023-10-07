def factor(a):
    b=0
    for i in range(1,a+1):
        if a%i==0 :
            print(i)
            if  i!=1 and i!=a:   
                b=b+1
    print("Num of fact are",b)

factor(10)    