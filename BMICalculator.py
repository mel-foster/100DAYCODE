#Exercise 6 BMI Calculator
# 1st input: enter height in meters e.g: 1.65
#height = input()
# 2nd input: enter weight in kilograms e.g: 72
#weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
#First Solution to get through testing in metrics: 
#height = input()
#weight = input()
#weight_as_int = int(weight)
#height_as_float = float(height)
#bmi = weight_as_int / (height_as_float * height_as_float)
#bmi_as_int =int(bmi)
#print(bmi_as_int)


#My solution for setting up as Imperial/Inches: 
#Introduce BMI Calculator
print ('Welcome to BMI Calculator!')
#Ask for height in Imperial/Inches

height = input("What is your height in inches?\n")
weight = input ("What is your weight?\n")

weight_as_int = int(weight)
height_as_float = float(height)

BMI = round((weight_as_int / (height_as_float * height_as_float) * 703), 2)

BMI_as_int = int(BMI)

print(BMI_as_int)

if BMI >= 18 and BMI <= 24:
    print ('Your BMI is', BMI, 'According to the CDC, You are within a healthy range.')
elif BMI >= 25 and BMI <= 29:
    print ('Your BMI is', BMI, 'According to the CDC, You are within an Unhealthy range, please work with a medical professional.')
elif BMI >= 30 and BMI <= 39:
    print ('Your BMI is', BMI, 'According to the CDC, you are in an Obese range, please work with a medical professional.')
elif BMI < 19:
    print ('Your BMI is', BMI, 'You are NOT within a Healthy range, please work with a medical professional.')
else:
    print ('There was an error with your input. Please restart the program!')

