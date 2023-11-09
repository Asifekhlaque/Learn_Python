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
# Python Lambda
  A lambda function is a small anonymous function.
  A lambda function can take any number of arguments, but can only have one expression.

    x = lambda a, b: a * b
    print(x(5, 6))
    
# How to install Matplotlib
    py -m pip install matplotlib

# Exception Handling

There are three type of error:
1. SyntaxError
2. LogicalError
3. Exception

There are three types of exceptions:
1. ZeroDivisionError: It is raised when a number is divided by zero
2. ValueError:
3. IndexError:

The <i>try</i> block lets you test a block of code for errors.

The <i>except</i> block lets you handle the error.

The <i>else</i> block lets you execute code when there is no error.

The <i>finally</i> block lets you execute code, regardless of the result of the try- and except blocks.
