import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta

class TaskReminder:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, due_date, due_time):
        due_datetime_str = f"{due_date} {due_time}:00"  # Add seconds to the time part
        due_datetime = datetime.strptime(due_datetime_str, "%Y-%m-%d %H:%M:%S")
        self.tasks[task] = due_datetime

    def check_tasks(self):
        current_datetime = datetime.now()
        tasks_to_remove = []

        for task, due_datetime in self.tasks.items():
            if current_datetime >= due_datetime:
                messagebox.showinfo("Pengingat Tugas", f"Waktunya untuk mengerjakan: {task}")
                tasks_to_remove.append(task)

        for task in tasks_to_remove:
            del self.tasks[task]

class TaskReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Reminder App")

        self.task_reminder = TaskReminder()

        self.label_task = tk.Label(root, text="Nama Tugas:")
        self.entry_task = tk.Entry(root)

        self.label_date = tk.Label(root, text="Tanggal:")
        self.calendar = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2)

        self.label_time = tk.Label(root, text="Waktu:")
        self.time_combobox = ttk.Combobox(root, values=self.generate_time_options(), state="readonly")

        self.button_add_task = tk.Button(root, text="Tambah Tugas", command=self.add_task)

        self.button_show_tasks = tk.Button(root, text="Lihat Tugas", command=self.show_tasks)

        self.label_task.grid(row=0, column=0, pady=(10, 0))
        self.entry_task.grid(row=0, column=1, pady=(10, 0))

        self.label_date.grid(row=1, column=0)
        self.calendar.grid(row=1, column=1)

        self.label_time.grid(row=2, column=0)
        self.time_combobox.grid(row=2, column=1)

        self.button_add_task.grid(row=3, column=0, columnspan=2, pady=(10, 0))
        self.button_show_tasks.grid(row=4, column=0, columnspan=2, pady=(10, 0))

    def generate_time_options(self):
        start_time = datetime.strptime("00:00", "%H:%M")
        time_options = []

        while start_time < datetime.strptime("23:55", "%H:%M"):
            time_options.append(start_time.strftime("%H:%M"))
            start_time += timedelta(minutes=5)

        return time_options

    def add_task(self):
        task = self.entry_task.get()
        due_date = self.calendar.get_date()
        due_time = self.time_combobox.get()

        if task and due_date and due_time:
            self.task_reminder.add_task(task, due_date, due_time)
            messagebox.showinfo("Tambah Tugas", f"Tugas '{task}' ditambahkan untuk diingatkan pada {due_date} pukul {due_time}.")
        else:
            messagebox.showerror("Error", "Mohon isi semua kolom.")

    def show_tasks(self):
        self.task_reminder.check_tasks()
        self.show_tasks_dialog()

    def show_tasks_dialog(self):
        tasks_str = "\n".join([f"{task}: {due_datetime.strftime('%Y-%m-%d %H:%M:%S')}" for task, due_datetime in self.task_reminder.tasks.items()])
        if tasks_str:
            messagebox.showinfo("Daftar Tugas", tasks_str)
        else:
            messagebox.showinfo("Daftar Tugas", "Tidak ada tugas yang ditambahkan.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskReminderApp(root)
    root.mainloop()
