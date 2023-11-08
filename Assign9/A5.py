class Student:
    def __init__(self, rollno, name, subMark = []) -> None:
        self.rollno = rollno
        self.name = name
        self.subMark = subMark
        self.percentage = 0

    def calculatePercentage(self):
        totalMarks = self.subMark[0][1] + self.subMark[1][1] + self.subMark[2][1]
        self.percentage = (totalMarks / 3)
        self.percentage = round(self.percentage,2)

    def studentDetails(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Student Name: {self.rollno}")
        print(f"Subject Details are as: ")
        for subName, subMark in self.subMark:
            print(f"\t{subName} -> {subMark}")
        print(f"Overall Percentage: {self.percentage}")


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
        print(f"Student {rollNo} added successfully.")

    elif choice == "2":
        rollNo = input("Enter roll no to delete: ")
        if rollNo in students:
            obj = students.pop(rollNo)
            del obj
            print(f"Student {rollNo} deleted successfully.")
        else:
            print(f"Student {rollNo} not found.")

    elif choice == "3":
        if len(students.values()) == 0:
            print("No Student details available")
            continue

        print("Student Details are as below: ")
        for studentObj in students.values():
            studentObj.calculatePercentage()
            studentObj.studentDetails()
    
    elif choice == "4":
        break

    else:
        print("Wrong Input")
