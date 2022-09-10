print("Welcome to tip calculator")

bill=int(input("What is the total bill ? In Rupees -> "))

people = int(input("how many people you like to split bill ->"))

tip= float(input("How much tip you like to give : 10,15,12,18...etc percentage -> "))

bill_with_tip = tip/100 * bill + bill

print(bill_with_tip)

