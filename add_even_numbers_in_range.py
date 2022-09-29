#Script to add all the even numbers from a range using Python

total = 0
for even in range(2, 101, 2):
    total += even
print(total)