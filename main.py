'''
Speeding Ticket Program
Teukin Barauti
Version 1
This program gives out a ticket depending on how fast you are going.
'''


# Here are my Variables
INT_LIMIT = 100
STR_SPEEDINPUT = "How fast do you think you were going?"

# If else statement
if int_userSpeed > 100:
  print(STR_UNSAFE)
# Integers and stuff
int_userSpeed = 0
INT_MONEYOWED = 500
# Strings and stuff! :D
STR_SAFE = "Okay, sorry for the confusion."
STR_GIMME_MONEY = "You give me ${} for speeding. Not good. Bad.".format(INT_MONEYOWED)
STR_UNSAFE = "You could've died, slow down!"
