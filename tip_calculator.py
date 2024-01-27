#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill amount?"))
tip = int(input("What percentage tip would you like to give? 10, 12 0r 15?"))
people = int(input("How many people to split the bill?"))

tip_as_a_percent = tip/100
tip_in_amount = tip_as_a_percent * bill
total_bill = bill + tip_in_amount
bill_per_person = total_bill/people

print(f"Each person should pay: ${bill_per_person:.2f}")
