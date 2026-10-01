first_name = input("What is your first name? ")
current_age = int(input("What is your current age? "))
dream_salary = float(input("What is your dream salary? "))

college_input = input("Are you currently enrolled in college? (True/False) ")
is_enrolled = college_input.strip().lower() == "true"

print()
print(f"Hello {first_name}! You are {current_age} years old and hope to make {dream_salary} dollars.")
print(f"Currently enrolled in college: {is_enrolled}")
