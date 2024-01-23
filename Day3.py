#Control Flow with if/else and Conditional Operators

#NOTES: you can use > to be greater than, < to be less than, >= to be greater than or equal to, <= to be less than or equal to
# == is equal to, != is not equal to

#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in inches? "))
#if height >= 48:
  #print("You can ride the rollercoaster!")
  
#else:
  #print("Sorry, you have to grow taller before you can ride.")

#Exercise 8 Odd or Even
#number = int(input("Which number do you want to check? "))

#if number % 2 == 0:
  #print("This is an even number.")
#else:
  #print("This is an odd number.")

#NOTES: 
#Nested if/else
#if/elif/else

#Writing multiple conditions in the same line of code
#if condition1:
  #do A
#elif condition2:
  #do B
#else:
  #do this

#bill += 3 is the same as bill = bill + 3

#EXERCISE 8.5 Rollercoaster
#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in inches? "))
#if height >= 48:
  #print("You can ride the rollercoaster!")
  #age = int(input("What is your age? "))

#if age < 12:
  #bill = 5
  #print("Child tickets are $5.")

  #if age <= 18:
    #bill = 7
    #print("Youth tickets are $7.")
    #print("Please pay $7.")

#for those in midlife crisis, they can ride for free
  #if age >= 45 and age <= 55:
    #print("Everything is going to be ok. Have a free ride on us!")
  #else:
    #bill = 12
    #print("Adult tickets are $12.")  

  #wants_photo = input("Do you want a photo taken? Y or N. ")
  #if wants_photo == "Y":
   #Add $3 to their bill for cost of photo
   #bill = bill + 3
  #print(f"Your final bill is ${bill}.")  

#else:
#print("Sorry, you have to grow taller before you can ride.")


#EXERCISE 9 BMI 2.0
#You can remove round to get a float

#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))
#bmi = round(weight / height ** 2)
#if bmi < 18.5:
  #print(f"Your BMI is {bmi}, you are underweight.")
#elif bmi < 25:
  #print(f"Your BMI is {bmi}, you have a normal weight.")
#elif bmi < 30:
  #print(f"Your BMI is {bmi}, you are slightly overweight.")
#elif bmi < 35:
  #print(f"Your BMI is {bmi}, you are obese.")
#else:
  #print(f"Your BMI is {bmi}, you are clinically obese.")

#EXERCISE 10 Leap Year
#Solution: 
#year = int(input("Which year do you want to check? "))
#if year % 4 == 0:
  #if year % 100 == 0:
    #if year % 400 == 0:
      #print("Leap year.")
    #else:
      #print("Not leap year.")  
  #else:
    #print("Leap year.")  
#else:    
  #print("Not leap year.")



#EXERCISE 11 Pizza Order Practice
#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M, or L ")
#add_pepperoni = input("Do you want pepperoni? Y or N ")
#extra_cheese = input("Do you want extra cheese? Y or N ")
#bill = 0
#if size == "S":
  #bill += 15
#elif size == "M":
  #bill += 20
#else:
  #bill += 25
#if add_pepperoni == "Y":
  #if size == "S":
    #bill += 2
  #else:
    #bill += 3
#if extra_cheese == "Y":
  #bill += 1
#print(f"Your final bill is: ${bill}.")


#NOTES: Logical Operators
#A and B
#C or D
#not E



#EXERCISE 12 Love Calculator
#print("Welcome to the Love Calculator!")
#name1 = input("What is your name? \n")
#name2 = input("What is their name? \n")
#combined_names = name1 + name2
#lower_names = combined_names.lower()
#t = lower_names.count("t")
#r = lower_names.count("r")
#u = lower_names.count("u")
#e = lower_names.count("e")
#first_digit = t + r + u + e
#l = lower_names.count("l")
#o = lower_names.count("o")
#v = lower_names.count("v")
#e = lower_names.count("e")
#second_digit = l + o + v + e
#score = int(str(first_digit) + str(second_digit))
#if (score < 10) or (score > 90):
  #print(f"Your score is {score}, you go together like coke and mentos.")
#elif (score >= 40) and (score <= 50):
  #print(f"Your score is {score}, you are alright together.")
#else:
  #print(f"Your score is {score}.")
