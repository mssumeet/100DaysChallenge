age = input("Enter your current age : ")
age_as_int = int(age)

years_remaining = 90-age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining *52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} Day s + you have {weeks_remaining} Weeks + you have {years_remaining} Years remaining")