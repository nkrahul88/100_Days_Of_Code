#Script to get inputs from User of height of person and calculate the height of the 
total = 0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total += student_heights[n]
#print(total)
avg = float(total / len(student_heights))
print(round(avg))

