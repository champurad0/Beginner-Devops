#create a tip calculator 

total_bill = float(input("What was the total of the bill? \n"))

percent_tip = float(input("What percentage of tip would you like to leave? \n"))
tip = percent_tip / 100
tip_total = tip * total_bill
meal_total = total_bill + tip_total

total_people = int(input("How many people will split the bill? \n"))

total_per_person = meal_total / total_people
 
print(f"Each person will have to pay {round(total_per_person, 2)}")
