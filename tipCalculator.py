# print statement introducing "Tip Calculator".
# Inputs necessary to make code work. 
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
# Tip represented as percentage of 100.
total_tip_amount = bill * tip_as_percent
# Total bill is equal to bill plus tip amount as percentage amount from tip input 
total_bill = bill + total_tip_amount
# Total bill is equal to those two amounts.
bill_per_person = total_bill / people
# Bill per person is determined by dividing bill by number of people.
final_amount = round(bill_per_person, 2) 
print(f"Each person should pay: ${final_amount}")
# Final amount per person is determined and rounded to nearest whole dollar amount.