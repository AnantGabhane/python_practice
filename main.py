student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

#----------method 1 ------------
#total_height = sum((student_heights))
#average = int((len(student_heights)))
#output = round(total_height/average)
#print(output)

#----------method 2 ------------
total_height = 0
for height in student_heights:
    total_height += height
#print(total_height)

no_of_students = 0
for student in student_heights:
    no_of_students += 1
#print(no_of_students)

output = round(total_height/no_of_students)
print(output)