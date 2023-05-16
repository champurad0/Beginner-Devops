#build a love calculator that counts the time the letters in TRUE LOVE are in the names

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

first = name1.lower()
second = name2.lower()

names = first + second

t1 = names.count("t")
r1 = names.count("r") 
u1 = names.count("u")
e1 = names.count("e")

true = t1 + r1 + u1 + e1

l2 = names.count("l")
o2 = names.count("o") 
v2 = names.count("v")
e2 = names.count("e")

love = l2 + o2 + v2 + e2

love_score = str(true) + str(love)
love_int = int(love_score)
if love_int < 10 or love_int > 90:
    print(f"Your score is {love_score}, good luck!")
elif love_int >= 40 and love_int <= 50:
    print(f"Your score is {love_score}, you'll be alright")
else:
    print(f"Your score is {love_score}")

