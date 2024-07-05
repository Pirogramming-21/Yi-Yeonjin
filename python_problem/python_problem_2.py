students = {}

def Menu1(name, mid, final):
    students[name] = {'mid': mid, 'final': final, 'grade': None}

def Menu2():
    for student in students.values():
        if student['grade'] is None:
            average = (student['mid'] + student['final']) / 2
            if average >= 90:
                student['grade'] = 'A'
            elif average >= 80:
                student['grade'] = 'B'
            elif average >= 70:
                student['grade'] = 'C'
            else:
                student['grade'] = 'D'

def Menu3():
    print("-------------------------------")
    print("name\tmid\tfinal\tgrade")
    print("-------------------------------")
    for name, grades in students.items():
        print(f"{name}\t{grades['mid']}\t{grades['final']}\t{grades['grade']}")

def Menu4(name):
    if name in students:
        del students[name]
        print(f"{name} student information is deleted.")
    else:
        print("Not exist name!")

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            inputs = input("Enter name mid-score final-score: ").split()
            if len(inputs) != 3:
                print("Num of data is not 3!")
            else:
                name, mid, final = inputs
                if name in students:
                    print("Already exist name!")
                elif int(mid) <= 0 or int(final) <= 0:
                    raise ValueError
                else:
                    Menu1(name, int(mid), int(final))
        except ValueError:
            print("Score is not positive integer!")
    elif choice == "2":
        if students:
            Menu2()
            print("Grading to all students.")
        else:
            print("No student data!")
    elif choice == "3":
        if students:
            None_grade = False
            for student in students.values():
                if student['grade'] is None:
                    None_grade = True
            if None_grade:
                print("There is a student who didn't get a grade.")
            else:
                print()
                Menu3()
        else:
            print("No student data! ")
    elif choice == "4":
        if students:
            name = input("Enter name to delete: ")
            Menu4(name)
        else:
            print("No student data! ")
    elif choice == "5":
        print("Exit Program!")
        break
    else:
        print("Wrong number. Choose again.")
