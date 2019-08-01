if __name__ == '__main__':
    students={}
    for _ in range(int(input())):
        name = input("name ")
        maths = int(input("maths marks "))
        physics = int(input(" physics marks "))
        chemistry = int(input( " chemistry marks "))
        students[name]= [maths,physics,chemistry]
    print(students)
    query_name = input(" Student name whose average is required ")
    marks_values = students[query_name]
    print(marks_values)

    for names , m1 in students.items():
        if names == query_name:
            avg_marks = (m1[0] + m1[1] + m1[2])/3.00
            print(format(avg_marks,'.2f'))


