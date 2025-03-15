import click  # CLI (Command Line Interface) banane ke liye
import os  # File ki existence check karne ke liye
import json  # Tasks ko JSON file me save/load karne ke liye

# Summary:__
# is project me hum 5 function bna rhy hy no1 task exist krta hy tu return kry or agr nhi tu khali return kry no2 task ko json format me save kry no3 task ko complte mask kry ky user ny add kr diya hy no4 task ko list me show kry no5 task ko delete kry list me se number ky zariye  


# Yeh file me tasks store honge
todo_file = "todo.json"

# ------------------ Utility Functions ------------------

# Yeh function check karega agar todo.json file exist karti hai.
# Agar file exist karti hai to usko read karega, warna empty list return karega.
def get_todos():
    if not os.path.exists(todo_file):  # Agar file exist nahi karti
        return []  # Empty list return kar do
    
    # File ko safely open karne ke liye 'with' use kar rahe hain
    # 'r' (read mode) ka matlab hai ke hum sirf file read karenge
    with open(todo_file, 'r') as file:
        return json.load(file)  # JSON file ka data load kar ke return kar do

# Ek function jo user ke likhe gaye tasks ko save karega.  
# 'w' (write mode) se file open hogi, jo purani file overwrite kar dega.  
# json.dump(task, file, indent=4) se task ko JSON format me convert karke file me likha jayega.
def save_task(tasks):
    with open(todo_file, 'w') as file:
        json.dump(tasks, file, indent=4)  # File me task save karega

# ------------------ CLI Setup ------------------

# Yeh ek CLI ka base function hai jo sare commands ko group karega
# isme sirf ek docstring hai jo function ka description batayega
@click.group()
def cli():
    """Simple To-Do List Manager"""
    pass

# ------------------ Task Add Karne Ka Function ------------------

# Click ka decorator jo CLI me command ko register karega
# @click.argument('task') ka matlab hai ke user ek task likh sakta hai
@click.command()
@click.argument('task')
def add(task):
    """Add new task to the list"""
    tasks = get_todos()  # Pehle se saved tasks load karo
    tasks.append({'task': task, 'done': False})  # Naya task list me add karo
    save_task(tasks)  # List ko wapas save karo
    #echo ky keyword se hum cli me kuch print krwana ho tu hum ye click ka function use krty hy
    click.echo(f"Task added: {task}")  # CLI pe confirm message print karo

# ------------------ Sare Tasks Show Karne Ka Function ------------------

@click.command()
def list_tasks():
    """List all tasks"""
    tasks = get_todos()  # Pehle se saved tasks load karo

    if not tasks:  # Agar koi task nahi hai
        click.echo('No tasks found')  # Message print karo
        return

    # Yahan enumerate se har task ka index bhi mil jayega
    for index, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else '❌'  # Agar task done hai to ✅, warna ❌
        click.echo(f"{index}. {task['task']} {status}")

# ------------------ Task Complete Karne Ka Function ------------------

@click.command()
@click.argument('task_number', type=int)  # User ek number input karega
def complete(task_number):
    """Mark a task as Completed"""
    tasks = get_todos()

    # Yahan task number check karenge ke valid hai ya nahi
    if task_number > len(tasks) or task_number < 1:
        click.echo('Task not found')
        return

    task = tasks[task_number - 1]  # Task ko list me se dhoondo
    task['done'] = True  # Task ko complete mark karo
    save_task(tasks)  # Updated list save karo
    click.echo(f"Task '{task['task']}' marked as completed ✅")  # Confirmation message

# ------------------ Task Delete Karne Ka Function ------------------

@click.command()
@click.argument('task_number', type=int)
def delete(task_number):
    """Delete a task from the list"""
    tasks = get_todos()

    # Agar user galat task number de to error handle karenge
    if task_number > len(tasks) or task_number < 1:
        click.echo('Task not found')
        return

    task = tasks.pop(task_number - 1)  # List me se task hata do
    save_task(tasks)  # Updated list save karo
    click.echo(f"Task '{task['task']}' deleted 🗑️")  # Confirmation message

# ------------------ CLI Commands Add Karna ------------------

cli.add_command(add)  # Add command ko CLI me add karna
cli.add_command(list_tasks)  # List command ko CLI me add karna
cli.add_command(complete)  # Complete command ko CLI me add karna
cli.add_command(delete)  # Delete command ko CLI me add karna

# ------------------ CLI Start Karne Ka Code ------------------

# Agar ye file directly run ho to CLI start ho
if __name__ == "__main__":
    cli()
