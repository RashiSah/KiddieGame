from sys import exit
from random import randint

print "The game you are going to play is - Maths locha."
def Entrance():
   print "Little 10 year old prince is waiting for a friend to play with him. He does not have have friends of his age in his palace. He had talked to his father regarding the problem. His father listened to him and told him that you will not only play with your friends, but you also have to study along with them. His father's favourite subject is Mathematics. As, the palace was on the another side of the river. If any friend wants to visit the palace, he has to cross the river"
   print "King decided to make the river the passing game for the other children. The boy/girl who will clear all the rounds of crossing the river will be the friend of the little prince and would be allowed to enter the palace. So, here we go. You are standing on a side of river and the palace is on the opposite side. Now your 1st level is"
   fst_ques()
def death():
   print "You died. You kinda suck at this.",
   exit(1)
def fst_ques():
   print "5 + 3 = ?"
   a = input()
   if a==8:
      print "Woh! You have completed the 1st level"
      print "Now, the question for the 2nd door"
      next_step()
   else:
      death()
def next_step():
   print "100-25 = ?"
   b = input()
   if b==75:
      print "Yuhu,the 3rd door is waiting for you now!"
      another_door()
   else:
      death()
def another_door():
   print "Now, tell me that what is the answer of 25*5 ?"
   c = input()
   if c==125:
      print "Great, you have completed the 3rd level. The 3rd door is now open for you"
      print "Going well! So, now forwarding towards our 4th door"
      lastphase()
   else:
      death()
def lastphase():
   print "The division time now"
   print "what is 60/3 ?"
   d = input()
   if d==20:
      print "Wow! You seem good at maths,King is impressed"
      next()
   else:
      death()
def next():
   print "Now I am going to ask you a general question after your maths work"
   print "Do you know that - on an average, how many people solve these questions??.. umm hmm.. so do you know.. C'mon, make a guess out of any number from 1 to 10"
   print "Here you will get 6 chances to make a guess. If your answer will not match to the correct number, the next door will permanently gets closed and you will not be able to meet the prince. Ah! Sad :( ... Good luck for the guess work!!"
   code = "%d" % (randint(1,10))
   guess = raw_input("[keypad]> ")
   g = 0
   while guess!=code and g<10:
       print "Oh No! Try again"
       g += 1
       guess = raw_input("[keypad]> ")
   if guess == code:
        print "Yipee! great in guessing haann!!!"
        end()
   else:
        print "It's sad to say that your guess didn't work. Alas! Door closes permanently"
        death()
def end():
   print "The last door is there! Be ready!"
   print "Hey there, let's see what is waiting for you"
   print "Choose any option, it will decide your future"
   print "dream or destiny"
   f = raw_input()
   if f=="dream":
       print "Oh yeah! you have reached to the final phase"
       print "Yipee!"
       finale()
   else:
       print "haww!! You need to reshow your kundly to the pandit. Your destiny isn't in your favour :'(.."
       death()
def finale():
    print "Congratulations! You have reached the palace and you are going to meet the little prince. You both will b friends forever"
    print "You won"
         
Entrance()

