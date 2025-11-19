# Name: Gaurav Kumar 
# Roll No: 2501660010
# Course: BCA
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-1 Mini Project
# Title: Student Profile Console App
# Date: 19-11-2025

# ------------------------------------------------------------
# STUDENT PROFILE CONSOLE APP
# ------------------------------------------------------------
# This mini-project demonstrates basic Python programming concepts:
# - Variables, input/output
# - Data types & type conversion
# - Operators (arithmetic, assignment, comparison, logical, identity, membership)
# - String operations and formatting
# - File handling (bonus task)
# ------------------------------------------------------------

# -------------------- Task 1: Setup & Introduction --------------------
print("==========================================")
print(" Welcome to the Student Profile CLI Tool ")
print("==========================================\n")
print("This tool collects your personal details and displays your profile card.\n")

# -------------------- Task 2: Input & Variables --------------------
# Taking user input and storing in variables
full_name = input("Enter your Full Name: ")
roll_no = input("Enter your Roll Number: ")
program = input("Enter your Program (e.g., BCA): ")
university = input("Enter your University Name: ")
city = input("Enter your City: ")
age = int(input("Enter your Age: "))   # type conversion to integer
hobby = input("Enter your Hobby: ")

print("\nData captured successfully!\n")

# -------------------- Task 3: Operators Demonstration --------------------
print("------ Operators Demonstration ------")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Arithmetic Operators
print("\nArithmetic Operators:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} // {num2} = {num1 // num2}")

# Assignment Operators
print("\nAssignment Operators:")
x = num1
x += num2
print(f"x += num2 → {x}")
x -= num2
print(f"x -= num2 → {x}")
x *= num2
print(f"x *= num2 → {x}")
x //= num2
print(f"x //= num2 → {x}")

# Comparison Operators
print("\nComparison Operators:")
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")

# Logical Operators
print("\nLogical Operators:")
print(f"({num1} > 0) and ({num2} > 0): {(num1 > 0) and (num2 > 0)}")
print(f"({num1} > 0) or ({num2} < 0): {(num1 > 0) or (num2 < 0)}")
print(f"not({num1} > {num2}): {not(num1 > num2)}")

# Identity Operators
print("\nIdentity Operators:")
print(f"num1 is num2: {num1 is num2}")
print(f"num1 is not num2: {num1 is not num2}")

# Membership Operators
print("\nMembership Operators:")
sample_list = [1, 2, 3, 4, 5]
print(f"{num1} in {sample_list}: {num1 in sample_list}")
print(f"{num2} not in {sample_list}: {num2 not in sample_list}")

# -------------------- Task 4: Python Strings & Formatting --------------------
print("\n------ String Operations ------")

# String concatenation
greeting = "Hello, " + full_name + "! Welcome to Python programming."

# f-string formatting
f_string_msg = f"Hi {full_name}, you are enrolled in {program} at {university}."

# Escape characters
escape_example = "Here is your formatted profile:\n\tName:\t" + full_name + "\n\tCity:\t" + city

# String methods
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")
print(f"Title Case: {full_name.title()}")
print(f"Replaced City Name: {city.replace('a', '@')}")
print(f"Count of 'a' in name: {full_name.count('a')}")

print("\n" + greeting)
print(f_string_msg)
print(escape_example)

# -------------------- Task 5: Final Output — Student Profile Card --------------------
print("\n----------------------------------------")
print("           STUDENT PROFILE SYSTEM       ")
print("----------------------------------------")
print(f"Name: {full_name}")
print(f"Roll No: {roll_no}")
print(f"Course: {program}")
print(f"University: {university}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Hobby: {hobby}")
print("----------------------------------------")
print("Welcome to Python Programming!")
print("----------------------------------------\n")

# -------------------- Task 6: Bonus Task (Optional) --------------------
save_choice = input("Do you want to save your profile? (yes/no): ").strip().lower()
if save_choice == "yes":
    with open("student_profile.txt", "w") as file:
        file.write("----------------------------------------\n")
        file.write("           STUDENT PROFILE SYSTEM       \n")
        file.write("----------------------------------------\n")
        file.write(f"Name: {full_name}\n")
        file.write(f"Roll No: {roll_no}\n")
        file.write(f"Course: {program}\n")
        file.write(f"University: {university}\n")
        file.write(f"City: {city}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Hobby: {hobby}\n")
        file.write("----------------------------------------\n")
        file.write("Welcome to Python Programming!\n")
    print("Profile saved successfully as 'student_profile.txt'!")

print("\nThank you for using the Student Profile CLI Tool.")
