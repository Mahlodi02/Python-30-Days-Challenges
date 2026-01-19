# Student Grade Mana
students= {}
def number_students():
    num_students = int(input("Enter number of students: "))

    

    for i in range(num_students):
        name = input(f"Enter name of students {i + 1}: ")
        marks = []

        for j in range(3):
            mark = float(input(f"Enter mark {j + 1}: "))
            marks.append(mark)

        students[name] = marks

        print(students)


        students_average = []


    for name in students:
        student_marks_ave = sum(students[name]) / len(students[name])
        students_average.append(student_marks_ave)
        print(f"{name}: {student_marks_ave:.2f}")


    
    class_ave = sum(students_average) / len(students_average)
    print(f"{class_ave:.2f}")

    top_student = max(students, key=students.get)
    print(top_student)

number_students()

