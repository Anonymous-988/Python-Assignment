tuple = ()
for i in range(3):
    ele = input(f"Enter Student{i+1} Name: ")
    tuple = tuple + (ele,)

stud1, stud2, stud3 = tuple
print(f"Student 1 is {stud1}")
print(f"Student 2 is {stud2}")
print(f"Student 3 is {stud3}")