
print("===== STUDENT MARKS ANALYZER =====")

name = input("Enter student name: ")

subjects = ["Python", "Mathematics", "English", "Science", "Computer"]

marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (out of 100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

total = sum(marks)
average = total / len(subjects)
percentage = (total / (len(subjects) * 100)) * 100

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("\n===== STUDENT RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Average Marks:", round(average, 2))
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
