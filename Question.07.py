"""Write a program that takes user input for their age
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