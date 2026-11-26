"""
Case Study 10: Comprehensive Smart Campus Management Simulation
Menu-driven program using lists, nested lists, tuples and unpacking.
"""

EVENTS = (("TechFest", 200), ("Workshop", 150))
ATTENDANCE_LIMIT = 75.0


def add_student(students, roll, name, branch):
    if roll == "" or name == "":
        return False
    for record in students:
        if record[0] == roll:
            return False
    students.append([roll, name, branch])
    return True


def record_attendance(attendance, students, roll, present, total):
    if total <= 0 or present < 0 or present > total:
        return False
    found = False
    for record in students:
        if record[0] == roll:
            found = True
    if not found:
        return False
    attendance.append([roll, present, total])
    return True


def attendance_eligible(attendance, roll):
    for record in attendance:
        if record[0] == roll:
            percentage = record[1] * 100 / record[2]
            return percentage >= ATTENDANCE_LIMIT
    return False


def record_marks(marks_records, students, roll, marks):
    if len(marks) == 0:
        return False
    for mark in marks:
        if mark < 0 or mark > 100:
            return False
    found = False
    for record in students:
        if record[0] == roll:
            found = True
    if not found:
        return False
    marks_records.append([roll, marks])
    return True


def grade_for(marks):
    total = 0
    for mark in marks:
        total = total + mark
    average = total / len(marks)
    if average >= 75:
        return "FIRST"
    elif average >= 60:
        return "SECOND"
    elif average >= 40:
        return "THIRD"
    return "FAIL"


def register_event(events, students, roll, event_name):
    fee = -1
    for name, price in EVENTS:
        if name == event_name:
            fee = price
    if fee == -1:
        return False
    for record in students:
        if record[0] == roll:
            for old_roll, old_event, old_fee in events:
                if old_roll == roll and old_event == event_name:
                    return False
            events.append((roll, event_name, fee))
            return True
    return False


def allocate_transport(routes):
    result = []
    for route, demand, capacity in routes:
        buses = demand // capacity
        served = buses * capacity
        result.append((route, buses, served, demand - served))
    return result


def print_summary(students, attendance, marks_records, events, routes):
    print("\nSUMMARY REPORT")
    for roll, name, branch in students:
        status = "eligible" if attendance_eligible(attendance, roll) else "not eligible"
        print("%-5s %-9s %-5s attendance: %s" % (roll, name, branch, status))
    for roll, marks in marks_records:
        print("%-5s marks: %s grade: %s" %
              (roll, marks, grade_for(marks)))
    revenue = 0
    for roll, event_name, fee in events:
        revenue = revenue + fee
    print("Event registrations: %d, revenue Rs %d" % (len(events), revenue))
    for route, buses, served, unserved in allocate_transport(routes):
        print("Route %s: %d bus(es), %d served, %d unserved" %
              (route, buses, served, unserved))


def main():
    students = []
    attendance = []
    marks_records = []
    events = []
    routes = []
    while True:
        print("\nSMART CAMPUS MENU")
        print("1. Add student   2. Attendance   3. Marks   4. Event")
        print("5. Transport     6. Summary      0. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            roll = input("Roll: ")
            name = input("Name: ")
            branch = input("Branch: ")
            print("Added" if add_student(students, roll, name, branch) else "Rejected")
        elif choice == "2":
            roll = input("Roll: ")
            present = int(input("Present: "))
            total = int(input("Total: "))
            print("Recorded" if record_attendance(attendance, students, roll, present, total)
                  else "Rejected")
        elif choice == "3":
            roll = input("Roll: ")
            marks_text = input("Marks: ")
            parts = marks_text.split()
            marks = []
            for part in parts:
                marks.append(int(part))
            print("Recorded" if record_marks(marks_records, students, roll, marks)
                  else "Rejected")
        elif choice == "4":
            roll = input("Roll: ")
            event_name = input("Event: ")
            print("Registered" if register_event(events, students, roll, event_name)
                  else "Rejected")
        elif choice == "5":
            route = input("Route: ")
            demand = int(input("Demand: "))
            capacity = int(input("Capacity: "))
            routes.append((route, demand, capacity))
            print("Route added")
        elif choice == "6":
            print_summary(students, attendance, marks_records, events, routes)
        elif choice == "0":
            break
        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main()
