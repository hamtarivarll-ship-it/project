from rich.console import Console
console=Console()
students = []
menu=[
    (1, "Add student"),
    (2, "Show students"),
    (3, "Calculate average"),
    (4, "Exit")
]


def add_student():
    name = input("Student name: ")
    grade = float(input("Student grade: "))
    
    students.append({
        "name": name,
        "grade": grade
    })
    
    console.print("Student added successfully!",
        style="bold green"
    )
def show_students():
    if len(students) == 0:
        console.print("No students found!", style="red")
    else:
        console.print("\nStudents List:", style="bold cyan")
        
        for student in students:
            console.print(
            f"{student['name']} - {student['grade']}",
            style="yellow"
            )
def calculate_average():
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

while True:
    console.print("\nStudent Management System", style="bold blue")
    for num, title in menu:
        console.print(f"{num}: {title}")

    choice = input("\nChoose an option: ")
    if choice=="1":
        add_student()
    elif choice=="2":
        show_students()
    elif choice=="3":  
        calculate_average()
    elif choice=="4":
        console.print("Goodbye!", style="bold blue")
        break
    else:
        console.print("Invalid option!", style="bold red")
