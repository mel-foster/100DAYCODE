#OBJECTIVE
#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line:

#Solution
#print("Welcome to the Band Name Generator.")
#street = input("What's the name of the city you grew up in?\n")
#pet = input("What's your pet's name?\n")
#print("Your band name could be " + street + " " + pet)

#My Solution:
print("Welcome! Let's Create Your Custom Band's Name")
city = input("What city did you grow up in?\n")
pet = input("What is the name of your pet?\n")
band_name = city + " " + pet
print("Wow! What do you think about calling your band, " + band_name + "?")
