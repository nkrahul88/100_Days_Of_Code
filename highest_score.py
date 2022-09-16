#Script to accept input from user of all the scores and print the highest score 

high_score = 0

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

for score in student_scores:
    if score > high_score:
        high_score = score

print(f'The highest score in the class is: {high_score}')