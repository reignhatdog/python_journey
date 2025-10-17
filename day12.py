#Python Program to Analyze Student Grades

students = []
count = int(input("How many students? "))

for i in range(count):
    name = input(f"Enter name of student {i + 1}: ")
    grade = float(input(f"Enter grade of {name}: "))
    students.append({"name": name, "grade": grade})


total = sum(student["grade"] for student in students)
average = total / count

highest = max(students, key=lambda x: x["grade"])
lowest = min(students, key=lambda x: x["grade"])

passed = [s["name"] for s in students if s["grade"] >= 75]
failed = [s["name"] for s in students if s["grade"] < 75]

print(f"\nAverage grade: {average:.2f}")
print(f"Highest grade: {highest['name']} - {highest['grade']}")
print(f"Lowest grade: {lowest['name']} - {lowest['grade']}")
print("Students who passed:")
for name in passed:
    print(f"- {name}")

print("\nStudents who failed:")
for name in failed:
    print(f"- {name}")
