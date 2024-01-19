""" Question.01: 
Declare two variables, num1 and num2, with any integer values.
 Use these to calculate their sum and print the result.
Understand how variables store numerical values and perform
basic arithmetic in Python"""

num1 = 5
num2 = 6
sum = num1 +num2
print('Sum of two numbers are:', sum)

"""Question.02:
Create a variable called message and give it a string value.
 Append the string " World!" to it and print the updated message.
 Explore basic string operations in Python."""

message = ['this is a message','this is also a message']
print(message)
message.append("World")
print(message)

"""Question.03:
  Declare a variable, is_python_fun, and assign it a boolean value.
 Print a statement based on whether Python is considered fun.
 Learn to use boolean variables for decision-making in Python."""

is_python_fun = True
if is_python_fun == True :
    print("Python is fun",is_python_fun)
else :
    print("python is not fun")

"""Question.04:
Create a list called fruits with at least three different fruit names.
 Print the list, add a new fruit, and then print the updated list.
   Understand the basics of working with lists in Python."""

fruits = ['Apple','Banana','Orange']
print(fruits)
fruits.append('cheery')
print(fruits)   

"""Question.05:
Declare a variable called price with a floating-point value. 
Convert it to an integer and print both the original and converted values.
 Explore how to convert between different data types in Python"""
price = 5.26
print('price for one pencil:',price)
i = int(price)
print('its integer value will be',i)

"""Question.06:
 Create a dictionary named student_info with keys for 'name', 'age'
, and 'grade'. Assign corresponding values and print the dictionary.
 Learn how to work with dictionaries, a versatile data structure 
in Python"""
Student_info = {'name':'Ali','Age':'23','grade':'A'}
print(Student_info)

"""Question.07: 
Write a program that takes user input for their age
 and prints a message addressing their age group
   (e.g., "Teenager," "Adult"). 
Explore user interaction and conditional statements in Python."""
Person_Age = input ("Enter Your Age :")
Age = int(Person_Age)
if (Age < 20) :
    print("You are a teen ager")
elif (20<=Age<=60):
    print("You are an Adult")

else:
    print("You area a Senior citizen")

    """Question.08:
Create a complex number variable, comp_num, with real and 
imaginary parts.Print both parts separately.
 Understand the representation of complex numbers in Python."""

comp_num = 3 + 4j # Complex number declared
complex_no = complex(comp_num)
Re = complex_no.real
Im = complex_no.imag
print("Real part of your complex number is:",Re)
print("Imaginary part of your complex number is:",Im)

"""Question.09:
Combine two strings using concatenation. Use string interpolation 
to include the length of the resulting string in a print statement. 
Explore different ways to manipulate strings in Python."""

String1= "My name is Syed Inam Ali"
string2= " I am doing course on Python from Bano Qabil "
print(String1+ string2)
print("Total lenght of Combine String is:", len(String1+string2))

"""Question.10
Create a tuple named days_of_week with the names of the days.
 Access and print the third day of the week.
 Understand the basics of working with tuples in Python"""

days_of_week = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(days_of_week[2])
