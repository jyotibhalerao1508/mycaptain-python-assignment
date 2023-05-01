class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def remove_student(self, name):
        for i, student in enumerate(self.students):
            if student.name == name:
                del self.students[i]

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.grade
        return total / len(self.students)

school = School("ABC School")

while True:
    print("\nSelect an option:")
    print("1. Add a student")
    print("2. Get a student")
    print("3. Remove a student")
    print("4. Get average grade")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = float(input("Enter grade: "))
        student = Student(name, age, grade)
        school.add_student(student)
        print(f"{name} added to {school.name}.")

    elif choice == "2":
        name = input("Enter name: ")
        student = school.get_student(name)
        if student:
            print(f"{student.name}, {student.age} years old, grade: {student.grade}")
        else:
            print(f"{name} not found in {school.name}.")

    elif choice == "3":
        name = input("Enter name: ")
        school.remove_student(name)
        print(f"{name} removed from {school.name}.")

    elif choice == "4":
        avg_grade = school.get_average_grade()
        print(f"Average grade for {school.name}: {avg_grade:.2f}")

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
