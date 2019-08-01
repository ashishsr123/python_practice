from operator import itemgetter
if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    grades=[]
    #sorted(L, key=itemgetter(2))
    students = sorted(students,key=itemgetter(0))
    print(students)
    for student in students:
        grades.append(student[1])
    min_grades = min(grades)
    remove_lowest = []
    for student in students:
        if student[1] == min_grades:
            remove_lowest.append(student)
    #students.remove(remove_lowest) 
    for item in remove_lowest:
        students.remove(item)
    grades_2 = []
    for student in students:
        grades_2.append(student[1])
    min_grades1 = min(grades_2)

    for student in students:
        if student[1] == min_grades1:
            print(" second lowest grades : ",student[0])
           

 
    


