import json
import time
from datetime import datetime

def load_data():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)

def start_timer():
    print("\n--- Start New Session ---")
    # پارامتر اجباری اول: نام تسک یا درس
    task_name = input("Enter task/course name (e.g., Theory, BSc_Project): ").strip()
    while not task_name:
        task_name = input("⚠️ Task name is required! Enter name: ").strip()
        
    # پارامتر اجباری دوم: نوع و سطح سختی باکس
    print("Choose Box Difficulty:")
    print("  [H] - Hard (e.g., Deep Konkoor Study, Complex Coding)")
    print("  [M] - Medium (e.g., HelpDesk, University Tasks)")
    print("  [S] - Simple (e.g., Organization, Light Coding)")
    box_type = input("Enter box type (H/M/S): ").strip().upper()
    while box_type not in ['H', 'M', 'S']:
        box_type = input("⚠️ Invalid input! Please enter H, M, or S: ").strip().upper()

    print(f"\n⏱️ Timer started for [{task_name}] | Difficulty: {box_type}")
    input("Press Enter when you actually start working...")
    start_time = time.time()
    
    input("\n🛑 Working... Press Enter again when you are DONE...")
    end_time = time.time()
    
    elapsed_time = round((end_time - start_time) / 60, 2) # تبدیل به دقیقه
    today = datetime.now().strftime("%Y-%m-%d")
    
    data = load_data()
    if today not in data:
        data[today] = []
        
    # ذخیره اطلاعات به همراه پارامتر نوع باکس
    data[today].append({
        "task": task_name, 
        "difficulty": box_type,
        "duration_minutes": elapsed_time
    })
    save_data(data)
    print(f"✅ Successfully logged {elapsed_time} minutes for '{task_name}' [{box_type}]!")

def view_report():
    today = datetime.now().strftime("%Y-%m-%d")
    data = load_data()
    print(f"\n📊 Performance Report for Today ({today}):")
    if today in data and data[today]:
        for item in data[today]:
            print(f"- {item['task']} [{item['difficulty']}]: {item['duration_minutes']} minutes")
    else:
        print("No tasks logged for today yet.")

if __name__ == "__main__":
    while True: # حلقه مداوم برای جلوگیری از بیرون پریدن برنامه
        print("\n================================")
        print("      MindDock MVP v0.1")
        print("================================")
        print("1. Start a new session (Timer)")
        print("2. View today's report")
        print("0. Exit Application")
        choice = input("Choose an option (1, 2, or 0): ").strip()
        
        if choice == "1":
            start_timer()
        elif choice == "2":
            view_report()
        elif choice == "0":
            print("\n👋 Saving environment... Goodbye, and keep consistent!")
            break # شکستن حلقه و خروج امن از برنامه
        else:
            print("⚠️ Invalid choice! Please select 1, 2, or 0.")