#student_scores = input("Input a list of student scores ").split()
#for n in range(0, len(student_scores)):
#  student_scores[n] = int(student_scores[n])
#print(student_scores)
student_scores = [78,65,91,89,55,64,89]
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest_score is : {highest_score}")