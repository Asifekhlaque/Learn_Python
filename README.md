<img src="https://github.com/Asifekhlaque/Learn_Python/assets/132199879/7d6e16cd-23e8-4b91-bb29-1f63f3bbe65c" with="300" height="300"/>


# Learn_Python
Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python is designed to emphasize code readability and ease of use, making it a popular choice for both beginners and experienced programmers.
# Need of Python
Python is used in a wide range of applications, including web development, scientific computing, data analysis, automation, artificial intelligence, machine learning, and more.
# Let's Python
# Python Print Statement
    print("Hello, Python!")
# Operater
An operator is a symbol or keyword used to perform operations on data. Operators are used to manipulate values and variables to produce a result.
# Arithmetic Operators in python
Arithmetic operators are used to perform mathematical operations on numeric values.
  # Addition (+):
    #Adds two values together
    result = 5 + 3  # result will be 8
  # Subtraction (-):
    #Subtracts the right operand from the left operand
    result = 10 - 4  # result will be 6
  # Multiplication (*):
    #Multiplies two values.
    result = 6 * 7  # result will be 42
  # Division (/):
    #Divides the left operand by the right operand, and the result is a floating-point number.
    result = 15 / 3  # result will be 5.0
  # Floor division(//):
    #Divides the left operand by the right operand, and the result is a Not floating-point number.
    result= 5 // 2  # result will be 1 
  # #Modulus (%):
    Returns the remainder of the division of the left operand by the right operand.
    result = 17 % 5  # result will be 2
  # Exponentiation (**):
    #Raises the left operand to the power of the right operand.
    result = 2 ** 3  # result will be 8
# Relational operators in python
Relational operators are used for comparing the values. It either returns True or False according to the condition. These operators are also known as Comparison Operators.
  # Greater than (>):
    #True if the left operand is greater than the right	
    x > y
  # Less than (<):
    #True if the left operand is less than the right	
    x < y
  # Equal to (==):
    #True if both operands are equal	
    x == y
  # Not equal to (!=)
    #True if operands are not equal 
    x != y
  # Greater than or equal to (>=)
    #True if left operand is greater than or equal to the right	
    x >= y
  # Less than or equal to (<=)
    #True if left operand is less than or equal to the right	
    x <= y
#  Logical Operators in python
  # and 
    #Returns True if both statements are true
    x = 5
    print(x > 3 and x < 10)
    #returns True because 5 is greater than 3 AND 5 is less than 10
 # or
    #Returns True if one of the statements is true
    x = 5
    print(x > 3 or x < 4)
    #returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
 # not
    #Reverse the result, returns False if the result is true
    x = 5
    print(not(x > 3 and x < 10))
    #returns False because not is used to reverse the result
# Control Statement
# Condition Statement
 # if
    #If you have only one statement to execute, you can put it on the same line as the if statement.
    a = 200
    b = 33
    if a > b: print("a is greater than b")
 # else
    #The else keyword catches anything which isn't caught by the preceding conditions.
    a = 200
    b = 33
    if b > a:
    print("b is greater than a")
    else:
    print("b is not greater than a")
 # If ... Else
    #If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
    a = 2
    b = 330
    print("A") if a > b else print("B")
  # Looping Statement
    # For Loop
      # for i(variable name) in range(Starting point,Ending point,interval)
       for i in range(1,10,1):
          print("Hello",i)

    # While loop
      i = 1
      while i < 6:
        print(i)
        i += 1

   # Break For
     fruits = ["apple", "banana", "cherry"]
     for x in fruits:
       print(x) 
      if x == "banana":
       break
   # Continue Statement For
      fruits = ["apple", "banana", "cherry"]
      for x in fruits:
       if x == "banana":
         continue
       print(x) 

   # Break while
    i = 1
    while i < 6:
      print(i)
     if (i == 3):
      break
     i += 1
# Continue Statement while
    i = 0
    while i < 6:
     i += 1
     if i == 3:
      continue
     print(i)

# Function in Python
  A function is a block of code which only runs when it is called.
  
    def my_function():
      print("Hello from a function")

    my_function()

    def sq(x):
       print("Value is",x)
       return x*x

    print(sq(x=10))

# Python Lambda
  A lambda function is a small anonymous function.
  A lambda function can take any number of arguments, but can only have one expression.

    x = lambda a, b: a * b
    print(x(5, 6))

# String 
Strings in python are surrounded by either single quotation marks, or double quotation marks.
Collection of charactor 12sfhghcjvj/,=+*
# String Method
   
    print("a",len(a))
    print("\nb",b)
    print("\nc",c)
    print(d.lower())
    print(e.upper())
    print(len(f))
    print(f.strip()) # Remove gap
    print(len(f))
    print(g.split(' ')) # We can add any condition to it for cutting
    print(g.split('i')) 
    print(' '.join(g))
    print(h.replace('boy','girl'))
    print(h.replace('gamer boy','playing girl'))
    print(h.startswith('A'))
    print(h.endswith('boy'))
    print(i.count('is'))
    print(i.find('is'))
    print(i.rfind('is'))
    print(j.isalpha())  
    print(k.capitalize())
    print(k.title())
    print(k.swapcase())
    print(k.isupper())
    print(k.islower())
    print(l.isupper())
    print(m.center(20,"+"))
    n=59
    o="IIBM"
    p="BCA"
    txt="Asif is Rollno {0} He is a {2} From {1}"
    print(txt.format(n,o,p))

# List
Importent List can contain multiple data type
<br>
l=["Asif",19,22.3,"484",True]
# Method of list

    data=[40,50,70,10,20,30,80]
    print(max(data))
    data.append(45)
    print(data)
    data.reverse()
    data.remove(50)
    print(data.index(20))
    data.insert(0,69)
    data.clear()
    data.pop(5)
    data.sort()
    print(data[0])
    print(len(data))

# Python Classes/Objects
Python is an object oriented programming language.
<br>
Almost everything in Python is an object, with its properties and methods.
<br>
A Class is like an object constructor, or a "blueprint" for creating objects.
<br>
# Create a Class
To create a class, use the keyword class:

    class MyClass:
      x = 5

    print(MyClass)

    class Person:
     def __init__(self, name, age):
      self.name = name
      self.age = age

    p1 = Person("John", 36)

    print(p1.name)
    print(p1.age)

# Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
<br>
Parent class is the class being inherited from, also called base class.
<br>
Child class is the class that inherits from another class, also called derived class.
<br>

    # Inheritance class of having subclass with comman code of function
    # Like class Animal and subclass cat , dog , lion and tiger
    class c:
      def squ(s):
        s.y=int(input("Enter a number for square root"))

      def cube(s):
        s.x=int(input("Enter a number for cube root"))

    class d(c):
      def show(s):
        print("square",s.y*s.y,"\nCube",s.x*s.x*s.x)

    obj=d()
    obj.squ()
    obj.cube()
    obj.show()

# Python Polymorphism
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

    # Diffent function into one class
    # Method overriding when to or more method define as same name and same parameter in two or more class not possible to declare in a single class is called overriding
    class a:
      def info(s):
        print("Airtal")

    class b:
      def info(s):
        print("BSNL")

    class c:
      def info(s):
        print("JIO")

    obj=c()
    obj.info()

    asif=a()
    asif.info()

    obj=b()
    obj.info()



# Exception Handling

There are three type of error:
1. SyntaxError
2. LogicalError
3. Exception

There are three types of exceptions:
1. ZeroDivisionError: It is raised when a number is divided by zero
2. ValueError:
3. IndexError:

The <b><i>try</i></b> block lets you test a block of code for errors.
<br>
The <b><i>except</i></b> block lets you handle the error.
<br>
The <b><i>else</i></b> block lets you execute code when there is no error.
<br>
The <b><i>finally</i></b> block lets you execute code, regardless of the result of the try- and except blocks.
<br>
       
    try:
      # code that may raise an exception
      #pass
    except Exception as e:
      #code to handle the exception
      #pass
    finally:
      #code that will always be executed
      #pass
# How to install Matplotlib
    py -m pip install matplotlib
