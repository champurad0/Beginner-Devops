#create a program to tell us our cost for a pizza
# s = 15  pepperoni = 2
# m = 20  pepperoni = 3
# L = 25  pepperoni = 3
# extra cheese is 1

print("Welcome to python pizza.")
size = input("What size pizza would you like, s, m or l? \n")
pepperoni = input("Would you like to add pepperoni? Y or N \n")
cheese = input("Would you like to adde extra cheese? Y or N \n")
bill = 0 

if size == "s":
    bill = 15
    if pepperoni == "y":
        bill += 2
    if cheese == "y":
        bill += 1 

if size == "m":
    bill = 20
    if pepperoni == "y":
        bill += 3
    if cheese == "y":
        bill += 1 

if size == "l":
    bill = 25
    if pepperoni == "y":
        bill += 3
    if cheese == "y":
        bill += 1 

print(f"Your final bill is: ${bill}")