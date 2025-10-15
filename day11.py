# Student anlyzer

name = input("Enter your name: ")
grade1 = float(input("Enter your grade 1: "))
grade2 = float(input("Enter your grade 2: "))
grade3 = float(input("Enter your grade 3: "))

grades = [grade1, grade2, grade3]
average = sum(grades) / len(grades)


if average >=75:
        remarks = "pasado"
else:
        remarks = "bagsak"

print(f"Student: {name}")
print(f"Grades: {grades}")
print(f"Average: {average}")
print(f"Remarks: {remarks}")

print("\nDatatype:")
print("- name:", type(name))
print("- grades:", type(grades))
print("- average:", type(average))

