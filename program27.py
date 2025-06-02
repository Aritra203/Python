# Program to print name, roll, and age of 5 students using format() method with user input

students = []

for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    roll = int(input(f"Enter roll number of student {i+1}: "))
    age = int(input(f"Enter age of student {i+1}: "))
    students.append({"name": name, "roll": roll, "age": age})

print("{:<10} {:<10} {:<10}".format("Name", "Roll", "Age"))
for student in students:
    print("{:<10} {:<10} {:<10}".format(student["name"], student["roll"], student["age"]))