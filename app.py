import tkinter as tk

# app window
window = tk.Tk()
window.title("My To-Do List")
window.geometry("400x400")

# Heading
heading = tk.Label(window, text="My To-Do List", font=("Arial", 20))
heading.pack(pady=15)

# Text input field
task_entry = tk.Entry(window, width=35)
task_entry.pack(pady=10)

# Add Task button
add_button = tk.Button(window, text="Add Task")
add_button.pack(pady=10)

# Keeps the application running
window.mainloop()