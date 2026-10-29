from rich.console import Console

console = Console()
students = []

def show_menu():
    console.print("\nStudent Management System", style="bold blue")
    console.print("1. Add student")
    console.print("2. Show students")
    console.print("3. Calculate average")
    console.print("4. Exit")

def Calculate_average():
    if len(students) == 0:
        console.print("No grades available!", style="red")
    else:
        total = 0

    for student in students:
        total += student["grade"]

    average = total / len(students)

    console.print(
                f"Average grade: {average:.2f}",
                style="bold green"
            )


def Show_students():
    if len(students) == 0:
        console.print("No students found!", style="red")
    else:
        console.print("\nStudents List:", style="bold cyan")

    for student in students:
                console.print(
                    f"{student['name']} - {student['grade']}",
                    style="yellow"
                )
print("Amir")
def add_student():
    name = input("Student name: ")
    grade = float(input("Student grade: "))

    students.append({
    "name": name,
    "grade": grade
    })

console.print(
            "Student added successfully!",
            style="bold green"
        )



while True:
    show_menu()

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        Show_students()

    elif choice == "3":
        Calculate_average()

    elif choice == "4":
        console.print("Goodbye!", style="bold blue")
        break

    else:
        console.print("Invalid option!", style="bold red")
print(899381313661)