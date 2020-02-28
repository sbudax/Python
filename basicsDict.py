#creating a dictionary

student_grades = {"Sbusiso": 80, "John": 49, "Saun": 99}  #dictionary consisting of items("John": 49), Key and Value

mysum = sum(student_grades.values())
length = len(student_grades.values())
mean = mysum / length
print(mean)