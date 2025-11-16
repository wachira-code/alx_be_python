task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority case"
    case "low":
        reminder = f"'{task}' is a low priority case"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". cosider completing it when you have free time."

print(reminder)