import time
import random
score = 0
def sleep():
    time.sleep(2)
def startGame():
    print("You find yourself standing in an open field, filled with grass and",
      "yellow wildflowers.")
    sleep()
    print("Rumor has it that a wicked fairie is somewhere around here, and has",
      "been terrifying the nearby village.")
    sleep()
    print("In front of you is a house.")
    sleep()
    print("To your right is a dark cave.")
    sleep()
    print("In your hand you hold your trusty (but not very effective) rusty old magic wand.")
    sleep()     
# this function display what happend when getting to house    
def door1():
    print("you approch the door of the house")
    sleep()
    print("You are about to knock when the door opens and out steps a wicked fairy.")
    sleep()
    print("Eep! Thi s is the wicked fairy's house!")
    sleep()
    print("The wicked fairy finds you!,You feel a bit under-prepared for this ," 
            "what with only having a tiny, rusty old magic wand.")
# this function display what happend when getting to cave first once
def cave1():
    sleep()
    print("You peer cautiously into the cave.")
    sleep()
    print("It turns out to be only a very small cave") 
    sleep()
    print("Your eye catches a glint of metal behind a rock.")
    sleep()
    print("You have found the " + color + " magical Wand of Ogoroth!You discard your " 
             "rusty old magic wand and take the Wand of Ogoroth with you")
    sleep()
    print("You walk back out to the field.")
 # this function ask the player to get to the house or the cave. and checks the answer     
def ask1():
    print("would you like to (1) enter to house or (2) peer to cave")
    global choice1
    choice1 = input("please enter your choice (1) or (2)")
    while choice1 != "1" and choice1 != "2":
          print("this is a wrong value")
          ask1()
# this function ask the player what decision he will make. and checks the answer   
def ask2():
    print("would you like to (1) cast a spell (2) run away")
    global choice2
    choice2 = input("please enter your choice (1) or (2)")
    while choice2 != "1" and choice2 != "2":
          print("this is a wrong value")
          ask2() 
# this function ask the player for playing again or not. and checks the answer         
def ask3():
    global answer
    answer = input("Do you want to play again.(y/n)")
    while answer != 'y' and answer != 'n':
          print("this is a wrong value")
          ask3()  
    if answer == "y":
       Game()
    if answer == "n":            
       print("thank you for playing")
       exit()                        
# this function demonstrate if player choose to get to house with out getting to the cave.
# (lose condition) 
def lose_condition():
    while choice1 == "1":
            door1()
            ask2()
            while choice2 == "2":
                  sleep()
                  print("you back to the field succesfully withou any dameges")
                  ask1()
                  while choice1 == "1":
                        lose_condition()

                  if choice1 == "2":
                     win_conditions()                           
            if choice2 == "1":
               sleep()
               print("sorry,the fairy make you a frog because you have a rusty old magic wand")
               print("your score is " + str(score))
               time.sleep(4)
               ask3()
# this function demonstrate if player choose to get to cave.
# (win condition)              
def win_conditions():
    global n
    global score
    if choice1 == "2" and n == 0:
       cave1()
       n = n + 1
       ask1()
    while choice1 == "2" and n > 0:
          print("the cave has become empty")
          ask1()
    while choice1 == "1" and n >= 1:
          door1()
          ask2()
            
          while choice2 == "2":
                sleep()
                print("you back to the field succesfully withou any dameges")
                ask1()
                  
                while choice1 == "1" or choice1 == "2":
                      win_conditions()
   
          if choice2 == "1":
             print("you rid of the fairy")
             score = score + 100
             print("your score is " + str(score))
             ask3()                                                                    
def Game():
    global n
    n = 0
    global color
    choices = ["red", "blue", "green", "orange", "purple"]
    color = random.choice(choices)
    startGame()
    ask1()
    while choice1 == "1":
          lose_condition()

    if choice1 == "2":
       win_conditions()
Game()
