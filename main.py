import csv

# Dictionary to store student data
student_grades = {}

# Function to calculate GPA from marks
def calculate_gpa(marks):
    return round(marks / 10, 2)

# Function to add a new student
def add_student(name, marks):
    gpa = calculate_gpa(marks)
    student_grades[name] = {"marks": marks, "gpa": gpa}
    print(f"Added {name} with {marks} marks (GPA: {gpa})")

# Function to update existing student
def update_student(name, marks):
    if name in student_grades:
        gpa = calculate_gpa(marks)
        student_grades[name] = {"marks": marks, "gpa": gpa}
        print(f"{name}'s record updated.")
    else:
        print(f"{name} not found!")

# Function to delete student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} deleted successfully.")
    else:
        print(f"{name} not found!")

# Function to display all students, sorted by GPA
def display_all_students():
    if not student_grades:
        print("No students available.")
        return
    sorted_students = sorted(student_grades.items(), key=lambda x: x[1]['gpa'], reverse=True)
    for name, data in sorted_students:
        print(f"{name} => Marks: {data['marks']}, GPA: {data['gpa']}")

# Function to find topper (highest GPA)
def find_topper():
    if not student_grades:
        print("No students available.")
        return
    max_gpa = max(student_grades.values(), key=lambda x: x['gpa'])['gpa']
    toppers = [name for name, data in student_grades.items() if data['gpa'] == max_gpa]
    print(f"Class Topper(s) with GPA {max_gpa}: " + ", ".join(toppers))

# Import data from CSV
def import_csv(filename="students.csv"):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["Name"]
                marks = int(row["Marks"])
                gpa = float(row["GPA"])
                student_grades[name] = {"marks": marks, "gpa": gpa}
        print(f"Data imported from {filename}")
    except FileNotFoundError:
        print(f"{filename} not found!")

# Export data to CSV
def export_csv(filename="students.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks", "GPA"])
        for name, data in student_grades.items():
            writer.writerow([name, data['marks'], data['gpa']])
    print(f"Data exported to {filename}")

# Main menu loop
def main():
    while True:
        print("\n--- Student GPA Management System ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Find Topper")
        print("6. Import from CSV")
        print("7. Export to CSV")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            name = input("Enter student name: ")
            marks = int(input("Enter marks (out of 100): "))
            add_student(name, marks)
        elif choice == 2:
            name = input("Enter student name: ")
            marks = int(input("Enter new marks: "))
            update_student(name, marks)
        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            find_topper()
        elif choice == 6:
            import_csv()
        elif choice == 7:
            export_csv()
        elif choice == 8:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select between 1–8.")

main()
