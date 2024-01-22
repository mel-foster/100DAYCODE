#Data Types Notes
#String
#print("Hello"[4])

#Integer
#print (123 + 345)
#replace commas for large #'s with underscores
#123_456_789

#Float when # has decimals
#3.14159

#Boolean two values True or False  

#num_char = len(input("What is your name?"))
#new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters.")

#a = str(123)
#print (type(a))
#End of Section

#Exercise 5 
#two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
#Type Checking
#print (type(two_digit_number))
#Result string

#first_digit = int(two_digit_number[0])
#second_digit = int(two_digit_number[1])

#print(two_digit_number)

#Adding together
#two_digit_number = first_digit + second_digit

#print(two_digit_number)
#End of Section

#Other mathematics
#3 + 5  
#7 - 4
#3 * 2
#6 / 3 Division prints floated number 
#** Expontent 

#PEMDASLR 
#()
#** Exponents
#* Multiplication
#/ Division
#+ Addition
#- Subtraction
#left to right

#print(3 * (3 + 3) / 3 - 3)

#Exercise 6 BMI Calculator
# 1st input: enter height in meters e.g: 1.65
#height = input()
# 2nd input: enter weight in kilograms e.g: 72
#weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
#Solution: 
#height = input()
#weight = input()
#weight_as_int = int(weight)
#height_as_float = float(height)
#bmi = weight_as_int / (height_as_float * height_as_float)
#bmi_as_int =int(bmi)
#print(bmi_as_int)

#My solution: 
#Introduce BMI Calculator
#print ('Welcome to BMI Calculator!')
#Ask for height in Imperial/Inches

#height = input("What is your height in inches?\n")
#weight = input ("What is your weight?\n")

#weight_as_int = int(weight)
#height_as_float = float(height)

#BMI = round((weight_as_int / (height_as_float * height_as_float) * 703), 2)

#BMI_as_int = int(BMI)

#print(BMI_as_int)

#if BMI >= 18 and BMI <= 24:
    #print ('Your BMI is', BMI, 'According to the CDC, You are within a Healthy range.')
#elif BMI >= 25 and BMI <= 29:
    #print ('Your BMI is', BMI, 'According to the CDC, You are within an Unhealthy range, please work with a #medical professional.')
#elif BMI >= 30 and BMI <= 39:
    #print ('Your BMI is', BMI, 'According to the CDC, you are in an Obese range, please work with a medical professional.')
#elif BMI < 19:
    #print ('Your BMI is', BMI, 'You are NOT within a Healthy range, please work with a medical professional.')
#else:
    #print ('There was an error with your input. Please restart the program!')

#End of Section

#Number Manipulation and F Strings
#You can manipulate values based off previous values
#print(8/3)
#print(int(8/3))
#print(round(8/3))
#print(round(8/3, 2))
#print(8//3)
#print(type(8//3))
#print(type(8/3))
#result =
#result /= 2
#print(result)
#score = 0
#User scores a point
#score += 1
#print(score)

#F Strings
score =0
height = 1.8
isWinning = True
#f-String
#f"your score is {score}"
#print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


#Exercise 7 
#age = input("What is your current age?")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
#Solution
#age =input()
#ageint=int(age)
#yearremain=90-ageint
#days=yearremain*365
#week=yearremain*52
#print(f'You have {week} weeks left.')

#My solution
#print ('Welcome to how long do you have left to live if you live till 90!')
#age = input("What is your current age? ")
#ageint=int(age)
#yearremain=90-ageint
#days=yearremain*365
#week=yearremain*52
#month=yearremain*12
#print(f"you have {days} days, {week} weeks, and {month} months left.")

