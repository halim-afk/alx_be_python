task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
remider_high_preority = "is a high priority task that requires immediate attention today!"
Reminder = "Reminder:"
match priority : 
    case "high":
       if time_bound == "yes":
         print(Reminder , task , remider_high_preority)
       else : 
         print(f"'{task}' is a medium priority task")
    case "medium":
       if time_bound == "yes":
         print(Reminder , task , remider_high_preority)
       else :
         print(f"{task}' is a medium priority task")
    case "low":
       if time_bound == "yes":
         print(f"'{task}' is a medium priority task that requires immediate attention today!")
       else :
         print(f"Note: {task}' is a low priority task. Consider completing it when you have free time.")     
    case _:
       print("thats unspacted")