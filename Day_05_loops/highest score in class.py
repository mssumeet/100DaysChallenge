student_score = input("enter the student score : ").split( )
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

highest_score = 0
# print(type(highest_score))

for score in student_score:
    if score > highest_score:
        highest_score = score

print(f"Highest Score is : {highest_score} ")