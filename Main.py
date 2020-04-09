#Kimberly Guerrero
#Final Integration Project
#Quiz meant to gauge personality and give 4 alternatives to a perfect day

#Function for random song choice in bonus round
def songChoice(quizSongs):
  import random
  songs = open(quizSongs).read().splitlines()
  return random.choice(songs)

#Function for random video game choice in bonus round
def gameChoice(quizGames):
  import random
  games = open(quizGames).read().splitlines()
  return random.choice(games)

#Function to get quiz results from other file
def quizResult(num1):
  if(num1<=18):
    print(open("resultStories.txt").read()[0:814])
  elif(num1<=26):
    print(open("resultStories.txt").read()[816:1546])
  elif(num1<=35):
    print(open("resultStories.txt").read()[1548:2355])
  elif(num1<=44):
    print(open("resultStories.txt").read()[2357:3079])

print("*****Hello and Welcome to*****\n****The Perfect Day Maker!****")
name = input("\nWhat's your name?\n") #input of user name

totalPoints = 0

readyAnswer = input("\nAre you ready to know your perfect day? (Y or N)\n")
while readyAnswer != 'Y' and readyAnswer != 'y': #While loop asking to continue of Y or y not entered
  readyAnswer = input("Are you ready to know your perfect day now? (Y or N)\n")
  
sleepAnswer = input("\nHow much do you love sleep?\n a. Im basically Sleeping Beauty\n b. I'm the average joe \n c. Can't humans survive off 4 hours? \n d. I'll sleep when I die\n")#prompting for response and initializing variable

#Below is the structure every question will follow from prompt, answer, to point assignment.
#Sean Lamont helped with while not loop organization
while not (sleepAnswer == 'a' or sleepAnswer == 'b' or sleepAnswer == 'c' or sleepAnswer == 'd'):
  sleepAnswer = input("Please use a, b, c, or d\n")
  #while loop is entered if correct letter is not inputted by user and does not exit unless a,b,c,d are entered
#Points added according to answer from calmest (one point) to wildest(4 points)
if sleepAnswer == 'a':
  totalPoints+=1
elif sleepAnswer == 'b':
  totalPoints+=2
elif sleepAnswer == 'c':
  totalPoints+=3
elif sleepAnswer == 'd':
  totalPoints+=4

zodiacSign = input("\nWhat is your zodiac sign?\n a. Fire(Aries, Leo, Sagittarius) \n b. Water(Cancer, Scorpio, Pisces)  \n c. Air(Libra, Aquarius, Gemini)  \n d. Earth(Capricorn, Taurus, Virgo)\n")
while not (zodiacSign == 'a' or zodiacSign == 'b' or zodiacSign == 'c' or zodiacSign == 'd'):
  zodiacSign = input("Please use a, b, c, or d\n")
if zodiacSign == 'a':
  totalPoints+=4
elif zodiacSign == 'b':
  totalPoints+=1
elif zodiacSign == 'c':
  totalPoints+=3
elif zodiacSign == 'd':
  totalPoints+=2

lunchDate = input("\nWhat group would you have lunch with?\n a. Mario, Yoshi, Luigi, Toadette \n b. Ash, Pikachu, Bulbazar, Misty  \n c. Donkey Kong, Diddy, Dixie, Candy  \n d. Cloud Strife, Aerith, Bahamut, Barret Wallace\n")
while not (lunchDate == 'a' or lunchDate == 'b' or lunchDate == 'c' or lunchDate == 'd'):
  lunchDate = input("Please use a, b, c, or d\n")
if lunchDate == 'a':
  totalPoints+=1
elif lunchDate == 'b':
  totalPoints+=2
elif lunchDate == 'c':
  totalPoints+=3
elif lunchDate == 'd':
  totalPoints+=4

hogwartsHouse = input("\nWhat's your Hogwarts House?\n a. Gryfindor \n b. Hufflepuff  \n c. Slytherin  \n d. Ravenclaw\n")
while not (hogwartsHouse == 'a' or hogwartsHouse == 'b' or hogwartsHouse == 'c' or hogwartsHouse == 'd'):
  hogwartsHouse = input("Please use a, b, c, or d\n")
if hogwartsHouse == 'a':
  totalPoints+=2
elif hogwartsHouse == 'b':
  totalPoints+=1
elif hogwartsHouse == 'c':
  totalPoints+=4
elif hogwartsHouse == 'd':
  totalPoints+=3

workAnswer = input("\nAfter a long day at work what do you do?\n a. Bubble Bath and incense\n b. Unwinding with a good book\n c. Call the squad for a night out\n d. Tinder for the win!\n")
while not (workAnswer == 'a' or workAnswer == 'b' or workAnswer == 'c' or workAnswer == 'd'):
  workAnswer = input("Please use a, b, c, or d\n")
if workAnswer == 'a':
  totalPoints+=1
elif workAnswer == 'b':
  totalPoints+=2
elif workAnswer == 'c':
  totalPoints+=3
elif workAnswer == 'd':
  totalPoints+=4

disneyAnswer = input("\nWhat Disney movie do you relate to?\n a.Peter Pan \n b.Beauty and the Beast\n c.Lion King\n d.Aladdin\n")
while not (disneyAnswer == 'a' or disneyAnswer == 'b' or disneyAnswer == 'c' or disneyAnswer == 'd'):
  disneyAnswer = input("Please use a, b, c, or d\n")
if disneyAnswer == 'a':
  totalPoints+=1
elif disneyAnswer == 'b':
  totalPoints+=2
elif disneyAnswer == 'c':
  totalPoints+=3
elif disneyAnswer == 'd':
  totalPoints+=4

weatherAnswer = input("\nWhats your ideal weather?\n a.Cloudy \n b.Rainy \n c.Sunny \n d.Windy\n")
while not (weatherAnswer == 'a' or weatherAnswer == 'b' or weatherAnswer == 'c' or weatherAnswer == 'd'):
  weatherAnswer = input("Please use a, b, c, or d\n")
if weatherAnswer == 'a':
  totalPoints+=1
elif weatherAnswer == 'b':
  totalPoints+=2
elif weatherAnswer == 'c':
  totalPoints+=4
elif weatherAnswer == 'd':
  totalPoints+=3

partyAnswer = input("\nWho are you at the party?\n a.The Host! duh! \n b.The Life of it. Hello! \n c.My friends made me come \n d.What party lol\n")
while not (partyAnswer == 'a' or partyAnswer == 'b' or partyAnswer == 'c' or partyAnswer == 'd'):
  partyAnswer = input("Please use a, b, c, or d\n")
if partyAnswer == 'a':
  totalPoints+=4
elif partyAnswer == 'b':
  totalPoints+=3
elif partyAnswer == 'c':
  totalPoints+=2
elif partyAnswer == 'd':
  totalPoints+=1

homeAnswer = input("\nWhere would you rather live?\n a.By the Beach. Aloha! \n b.Desert Vibes \n c.Big City Life \n d.Wherever feels right\n")
while not (homeAnswer == 'a' or homeAnswer == 'b' or homeAnswer == 'c' or homeAnswer == 'd'):
  homeAnswer = input("Please use a, b, c, or d\n")
if homeAnswer == 'a':
  totalPoints+=2
elif homeAnswer == 'b':
  totalPoints+=3
elif homeAnswer == 'c':
  totalPoints+=4
elif homeAnswer == 'd':
  totalPoints+=1

drinkAnswer = input("\nPick a drink?\n a.Tea/Coffee \n b.Juice/Smoothie \n c.Your finest cocktail \n d.Water\n")
while not (drinkAnswer == 'a' or drinkAnswer == 'b' or drinkAnswer == 'c' or drinkAnswer == 'd'):
  drinkAnswer = input("Please use a, b, c, or d\n")
if drinkAnswer == 'a':
  totalPoints+=2
elif drinkAnswer == 'b':
  totalPoints+=3
elif drinkAnswer == 'c':
  totalPoints+=4
elif drinkAnswer == 'd':
  totalPoints+=1

boardgameAnswer = input("\nFavorite Board Game?\n a.CLUE \n b.Trivial Pursuit \n c.Monopoly \n d.Jenga\n")
while not (boardgameAnswer == 'a' or boardgameAnswer == 'b' or boardgameAnswer == 'c' or boardgameAnswer == 'd'):
  weatherAnswer = input("Please use a, b, c, or d\n")
if boardgameAnswer == 'a':
  totalPoints+=1
elif boardgameAnswer == 'b':
  totalPoints+=2
elif boardgameAnswer == 'c':
  totalPoints+=3
elif boardgameAnswer == 'd':
  totalPoints+=4


quizResult(totalPoints)

print("\n\n*****QUARENTINE BONUS ROUND*****")
print(name + ", Its 2020 and we are all in locked down. You must be super bored and let me tell you that you came to the right place.")
quarentineAnswer = input("Do you want to know what song and video game you should try? (Y or N)\n")
while not (quarentineAnswer == 'Y' or quarentineAnswer == 'N'):
  quarentineAnswer = input("Please choose Y or N, So we can give you a suggestion.\n")
if quarentineAnswer == 'Y':
  print("Your song to listen to is", songChoice('newSongs.txt'))
  print("The game you should try is", gameChoice('popularGames.txt'))
  print("Stay Safe Now!")
elif quarentineAnswer == 'N':
  print("Okay then! Stay Safe!")
