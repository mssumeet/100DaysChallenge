import random

name_string= input(" give me everybody's name , seperated by comma.")

name= name_string.split(", ")
name_count = len(name)

random_name = random.randint(0, name_count -1)
person_to_pay = name[random_name]
print(person_to_pay + " is going to pay the bill today")

print(name)
