print(" Welcome to zoo")

height = int(input(" Please enter your height"))
bill = 0
if height >= 120:

    print("u can play rollercoaster")
    age=int(input(" enter your age"))

    if age <= 12:
        bill = 5
        print(" Children ticket 5$")
    elif age <= 18:
        bill = 15
        print("youth ticket 15$")


    # logical operator
    elif age >=45 and age<=55:
        print("dont worry , have a free ride!")


    elif age >= 18:
        bill = 25
        print("For everyone 25$")
    want_photo = input(" dou you want photo? Y or N.")
    if want_photo =="Y":
        bill += 3
        print(f"your final bill is {bill} ")

else:
    print("please grow tall")
