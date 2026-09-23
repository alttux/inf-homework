f = open('1.txt')
students = {}
for l in f:
    student = l.strip().split()
    if student[0] in students:
        students[student[0]] = [students[student[0]][0]+int(student[1]), students[student[0]][1]+1]
    else:
        students[student[0]] = [int(student[1]), 1]

students_finish = {}
for s in students:
    students_finish[s] = students[s][0] / students[s][1]

print(max(students_finish, key=students_finish.get))

# students = {'Pasha': [10, 2]}
# print(students)