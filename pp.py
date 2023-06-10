    
import tkinter as tk

tasks = []

def add():
    task_name = entry_task_name.get()
    task_description = entry_task_description.get()
            
    if task_name and task_description:
        new_task = {
            'name': task_name,
            'description': task_description,
            'status': 'pending'
        }
        tasks.append(new_task)
        
        entry_task_name.delete(0, 'end')
        entry_task_description.delete(0, 'end')
        
        print("Task added successfully")    
    else:
        print("Please provide both task name and description")

def view():
    task_display.delete('1.0', 'end')
    
    for task in tasks:
        task_name = task['name']
        task_description = task['description']
        task_status = task['status']
        
        task_display.insert('end', f"Name: {task_name}\n")
        task_display.insert('end', f"Description: {task_description}\n")
        task_display.insert('end', f"Status: {task_status}\n\n")

def mark_complete():
    selected_task = task_display.get('1.0', 'end-1c')
    for task in tasks:
        if task['name'] in selected_task:
            task['status'] = 'completed'
    view()

def delete():
    selected_task = task_display.get('1.0', 'end-1c')
    for task in tasks:
        if task['name'] in selected_task:
            tasks.remove(task)
    view()

def save():
    filename = entry_filename.get()
    if filename:
        with open(filename, 'w') as file:
            for task in tasks:
                file.write(f"Name: {task['name']}\n")
                file.write(f"Description: {task['description']}\n")
                file.write(f"Status: {task['status']}\n\n")
        print("Tasks saved successfully")
    else:
        print("Please provide a filename")

window = tk.Tk()
window.geometry('600x600')
window.configure(bg='black')

label1 = tk.Label(window,text='Name',fg='white',bg='black')
label1.place(x=170,y=3)
label2= tk.Label(window,text='description',fg='white',bg='black')
label2.place(x=170,y=20)
label3 = tk.Label(window,text='File name',fg='white',bg='black')
label3.place(x=170,y=40)




task_display = tk.Text(window, height=10, width=40)
task_display.place(x=100, y=300)

entry_task_name = tk.Entry(window)
entry_task_name.pack()

entry_task_description = tk.Entry(window)
entry_task_description.pack()

entry_filename = tk.Entry(window)
entry_filename.pack()

add_button = tk.Button(window, text='Add', bg='red', fg='white', command=add)
add_button.place(x=20, y=40)

view_button = tk.Button(window, text='View', bg='red', fg='white', command=view)
view_button.place(x=120, y=40)

mark_complete_button = tk.Button(window, text='Mark done', bg='red', fg='white', command=mark_complete)
mark_complete_button.place(x=260, y=60)

delete_button = tk.Button(window, text='Delete', bg='red', fg='white', command=delete)
delete_button.place(x=420, y=40)

save_button = tk.Button(window, text='Save', bg='red', fg='white', command=save)
save_button.place(x=520, y=40)

window.mainloop()
