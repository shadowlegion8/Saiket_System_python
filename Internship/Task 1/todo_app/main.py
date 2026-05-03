import json
import os


class Task:
    def __init__(self, task_id, description, completed=False):
        self.task_id = task_id
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "id": self.task_id,
            "description": self.description,
            "completed": self.completed
        }


class TodoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    # Load tasks from file
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                for item in data:
                    self.tasks.append(
                        Task(item["id"], item["description"], item["completed"])
                    )

    # Save tasks to file
    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    # Add task
    def add_task(self):
        desc = input("Enter task description: ").strip()
        if not desc:
            print("❌ Task cannot be empty!\n")
            return

        task_id = len(self.tasks) + 1
        self.tasks.append(Task(task_id, desc))
        self.save_tasks()
        print("✅ Task added successfully!\n")

    # View tasks
    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks available.\n")
            return

        print("\n📋 Your Tasks:")
        for task in self.tasks:
            status = "✔" if task.completed else "❌"
            print(f"{task.task_id}. {task.description} [{status}]")
        print()

    # Complete task
    def complete_task(self):
        self.view_tasks()
        try:
            num = int(input("Enter task ID to mark completed: "))
            for task in self.tasks:
                if task.task_id == num:
                    task.mark_completed()
                    self.save_tasks()
                    print("✅ Task marked as completed!\n")
                    return
            print("❌ Task not found!\n")
        except ValueError:
            print("❌ Invalid input!\n")

    # Delete task
    def delete_task(self):
        self.view_tasks()
        try:
            num = int(input("Enter task ID to delete: "))
            self.tasks = [task for task in self.tasks if task.task_id != num]

            # Reassign IDs
            for i, task in enumerate(self.tasks, start=1):
                task.task_id = i

            self.save_tasks()
            print("🗑 Task deleted successfully!\n")
        except ValueError:
            print("❌ Invalid input!\n")

    # Edit task
    def edit_task(self):
        self.view_tasks()
        try:
            num = int(input("Enter task ID to edit: "))
            for task in self.tasks:
                if task.task_id == num:
                    new_desc = input("Enter new description: ").strip()
                    if new_desc:
                        task.description = new_desc
                        self.save_tasks()
                        print("✏ Task updated!\n")
                    else:
                        print("❌ Description cannot be empty!\n")
                    return
            print("❌ Task not found!\n")
        except ValueError:
            print("❌ Invalid input!\n")

    # Main menu
    def run(self):
        while True:
            print("==== ADVANCED TO-DO LIST ====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Edit Task")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.edit_task()
            elif choice == "6":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice!\n")


if __name__ == "__main__":
    app = TodoApp()
    app.run()