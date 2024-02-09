"""Author: [Syed Inam Ali]
Roll/MOb Number: [03463319859]
Email: [inamali19891989@gmail.com]
roject: BODY MASS INDEX Calculator """
# Project Title 
print("Welcome to Body Mass Index(BMI) Calculator")
# Taking inputs from user
try:
    weight = float(input("Enter Your weight in Kilograms: "))
except:
    print("Some Expectations has occured, Yoy may have entered some non-numeric value")
try:
    height =  float(input("Enter Your Height in inches: "))
except:
    print("Some Expectations has occured, Yoy may have entered some non-numeric value")
# conversion of height from inches to meter
height_m = 0.0254*height
# BMI formula
BMI = int(weight/height_m**2)
# Ideal weight with respect to height
id_weight = int(22*height_m**2)
# finding difference in user's weight and ideal weight 
diff_weight = abs(id_weight - weight)
# Showing results i.e BMI value
print(f"Your Body mass index = {BMI}")
# Categarizing users BMI as Under weight, normal,Overweight, Obese, Extremly Obese and some suggestions about weight
if BMI < 18.5:
    print(f"You are in UNDERWEIGHT category,\nYour ideal weight should be about {id_weight}kg\nYou should gain weight about {diff_weight}kg ")
elif 18.5<BMI<24.9:
    print("Great, Your BMI is NORMAL.\nContinue Healthy Lifestyle. Good luck ")
elif 24.9<BMI<29.9:
    print(f"You are in OVERWIGHT category,\nYour ideal weight should be about {id_weight}kg\nYou should lose weight about {diff_weight}kg ")
elif 29.9<BMI<34.9:
    print(f"You are in OBESE category,\nYour ideal weight should be about {id_weight}kg\nYou should lose weight about {diff_weight}kg")
else:
    print(f"You are in EXTREMLY OBESE category,\nYour ideal weight should be about {id_weight}kg\nYou should lose weight about {diff_weight}kg")