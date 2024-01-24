print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You are at a crossroads. Which way do you want to go?")
direction = input("Type 'left' or 'right'.\n")
if direction == "left":
    print("You come to a beautiful lake. ")
    print("You notice there is an island in the middle of the lake.")
    print("After looking around, you discover a small abandoned row boat at the edge of the shore.")
    print("It's hot day. Do you take a swim to the island? Or do you use the boat?")
    
    swim_or_boat = input("Type 'swim' or 'boat'.\n")

    if swim_or_boat == "swim":
        print("You have been attached by a snapping turtle. Game Over.")

    if swim_or_boat == "boat":
        print("After you row across the lake, you arrive at the island unharmed.")
        print(('Stepping out of the boat, you notice a trail leading into a dark forest.'
            ' Do you follow the trail or do you continue on the beach?'))

        trail_or_beach = input("Type 'trail' or 'beach'.\n")

    if trail_or_beach == "trail":
        print(('You follow the trail and discover a small cave.'
               'Your intuition tells you that the treasure is hidden inside.'
               'Do you enter the cave?'))

        yes_or_no = input("Type 'yes' or 'no'.\n")

        if yes_or_no == "yes":
            print("You found the treasure! You Win!")

        if yes_or_no == "no":
            print("You lose. You are now cursed to remain on the island forever.")

    if trail_or_beach == "beach":
        print("You wonder the beach for hours, become exhausted and dehydrated. Game Over.")

if direction == "right":
    print("You have fallen into a hole. Game Over.")
