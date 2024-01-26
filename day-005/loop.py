fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)


# Ejercicio: Average Height 

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
num_students = 0
av_height = 0

for i in student_heights:
    total_height+=i
    num_students+=1
av_height = int(round(total_height/num_students,0))

print(f"total height = {total_height}")
print(f"number of students = {num_students}")
print(f"average height = {av_height}")

# Ejercicio: High Score

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

aux = 0
first = True
for i in student_scores:
    if first == True:
        aux=i
        first = False
    if aux < i:
        aux=i
print(f"The highest score in the class is: {aux}")



for i in range(1,10):
    print(i)
    