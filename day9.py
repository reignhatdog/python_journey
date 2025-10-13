# Simple Student Record System

students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter course: ")
    
    student = {
        'name': name,
        'age': age,
        'course': course
    }
    
    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students yet!")
        return
    
    print("\nSTUDENT LIST:")
    print("-" * 30)
    for i, student in enumerate(students, 1):
        print(f"{i}. Name: {student['name']}")
        print(f"   Age: {student['age']}")
        print(f"   Course: {student['course']}")
        print()

def search_student():
    name = input("Enter name to search: ")
    
    found = False
    for student in students:
        if name.lower() in student['name'].lower():
            print(f"Found: {student['name']}, Age: {student['age']}, Course: {student['course']}")
            found = True
    
    if not found:
        print("Student not found!")

def main_menu():
    while True:
        print("\n" + "="*40)
        print("STUDENT RECORD SYSTEM")
        print("="*40)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")
        print("="*40)
        
        choice = input("Choose option (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":

    main_menu()



