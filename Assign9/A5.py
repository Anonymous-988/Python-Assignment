class Student:
    def __init__(self, rollno, name, subMark = []) -> None:
        self.rollno = rollno
        self.name = name
        self.subMark = subMark
        self.percentage = 0

    def calculatePercentage(self):
        totalMarks = self.


students = {}

# Menu for the program
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Display Student Details")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        rollNo = input("Enter Roll No: ")
        name = input("Enter Name: ")
        subMark = []
        for i in range(3):
            subject = input("Enter Subject Name: ")
            mark = int(input(f"Enter marks for {subject}: "))
            subMark.append((subject, mark))
        studentObj = Student(rollNo, name, subMark)
        students[rollNo] = studentObj
        print("Student {rollNo} added successfully.")

    elif choice == "2":
        rollNo = input("Enter roll no to delete: ")
        if rollNo in students:
            obj = students.pop(rollNo)
            del obj

    elif choice == "3":



## Have to implement proper methods to the Student Class as well need to reconstruct the switch cases
