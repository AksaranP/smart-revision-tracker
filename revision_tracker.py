import json

data = []

# Load data from file if it exists
try:
    with open("data.json", "r") as file:
        data = json.load(file)
except:
    data = []

def add_entry():
    subject = input("Enter subject: ")
    topic = input("Enter topic: ")
    score = int(input("Enter score (0-100): "))

    entry = [subject, topic, score]
    data.append(entry)

def view_data():
    if not data:
        print("No data available.")
    else:
        for entry in data:
            print(entry)

def weakest_topic():
    if not data:
        print("No data available.")
        return

    lowest = data[0]
    for entry in data:
        if entry[2] < lowest[2]:
            lowest = entry

    print("Weakest subject:", lowest[0])
    print("Weakest topic:", lowest[1])
    print("Score:", lowest[2])

def average_scores():
    if not data:
        print("No data available.")
        return

    totals = {}
    counts = {}

    for entry in data:
        subject = entry[0]
        score = entry[2]

        if subject in totals:
            totals[subject] += score
            counts[subject] += 1
        else:
            totals[subject] = score
            counts[subject] = 1

    for subject in totals:
        avg = totals[subject] / counts[subject]
        print(subject, "average:", round(avg, 2))

def save_data():
    with open("data.json", "w") as file:
        json.dump(data, file)

# Menu system
while True:
    print("\n--- Revision Tracker ---")
    print("1. Add data")
    print("2. View data")
    print("3. Weakest topic")
    print("4. Average scores")
    print("5. Save and exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_data()
    elif choice == "3":
        weakest_topic()
    elif choice == "4":
        average_scores()
    elif choice == "5":
        save_data()
        print("Data saved. Exiting...")
        break
    else:
        print("Invalid choice.")