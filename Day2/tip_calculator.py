print("Welcome To The Tip Caculator!")
bill =  float(input("What is the total bill to be paid? $"))
people = int(input("How many people wants to share the bill ? "))
tip = int(input("How much tip would you like to give ? %"))

tip_percent = tip / 100
total_tip_amount = bill * tip_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

print(f"This is the tip for each person {bill_per_person:.2f}")
