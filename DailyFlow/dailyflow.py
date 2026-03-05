import json
from datetime import date, timedelta

FILENAME = "data.json"

# Load data from file
def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except:
        return {}

# Save data to file
def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

# Get today's date
today = str(date.today())
yesterday = str(date.today() - timedelta(days=1))

data = load_data()

# Create today's entry if not exists
if today not in data:
    data[today] = {"tasks": []}

while True:
    print("\n🌞 DAILYFLOW MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Show Progress")
    print("5. Show Streak")
    print("6. Exit")

    choice = input("Enter choice: ")

    # ADD TASK
    if choice == "1":
        task = input("Enter task: ")
        data[today]["tasks"].append({"task": task, "done": False})
        save_data(data)
        print("✅ Task Added!")

    # VIEW TASKS
    elif choice == "2":
        tasks = data[today]["tasks"]
        if not tasks:
            print("No tasks for today.")
        else:
            for i, t in enumerate(tasks):
                status = "✔" if t["done"] else "✘"
                print(f"{i+1}. {t['task']} [{status}]")

    # MARK COMPLETE
    elif choice == "3":
        tasks = data[today]["tasks"]
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t['task']}")
        num = int(input("Enter task number: "))
        data[today]["tasks"][num-1]["done"] = True
        save_data(data)
        print("🎉 Task Completed!")

    # SHOW PROGRESS
    elif choice == "4":
        tasks = data[today]["tasks"]
        total = len(tasks)
        completed = sum(1 for t in tasks if t["done"])

        if total == 0:
            print("No tasks today.")
        else:
            percent = (completed / total) * 100
            print(f"📊 Progress: {percent:.2f}%")

    # SHOW STREAK
    elif choice == "5":
        streak = 0
        current_day = date.today()

        while True:
            day_str = str(current_day)
            if day_str in data:
                tasks = data[day_str]["tasks"]
                if tasks and all(t["done"] for t in tasks):
                    streak += 1
                    current_day -= timedelta(days=1)
                else:
                    break
            else:
                break

        print(f"🔥 Current Streak: {streak} day(s)")

    # EXIT
    elif choice == "6":
        print("Goodbye! Stay productive 🚀")
        break

    else:
        print("Invalid choice.")