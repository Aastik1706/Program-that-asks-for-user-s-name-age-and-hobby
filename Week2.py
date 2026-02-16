name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))
if 90 <= marks <= 100:
    grade = "A"
    message = "Outstanding performance! 🌟"
elif 80 <= marks < 90:
    grade = "B"
    message = "Very Good! Keep it up! 👍"
elif 70 <= marks < 80:
    grade = "C"
    message = "Good job! Keep improving 🙂"
elif 60 <= marks < 70:
    grade = "D"
    message = "You passed! Keep working hard 💪"
elif 50 <= marks < 60:
    grade = "E"
    message = "Don't give up! You can do better 📚"
elif 0 <= marks < 50:
    grade = "F"
    message = "Keep trying! Practice more 🚀"
else:
    grade = "Invalid"
    message = "Invalid marks entered."
print("\n📊 RESULT FOR", name.upper() + ":")
print("Marks:", int(marks), "/100")
print("Grade:", grade)
print("Message:", message)
