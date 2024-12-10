import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import mysql.connector
import pandas as pd

def install_dependencies():
    try:
        subprocess.check_call(['pip', 'install', 'mysql-connector-python', 'pandas'])
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Dependency installation failed: {e}")

def run_import_sql(username, password, db_name, folder_path):
    try:
        # Set environment variables
        os.environ['DB_USER'] = username
        os.environ['DB_PASSWORD'] = password
        os.environ['DB_NAME'] = db_name
        os.environ['FOLDER_PATH'] = folder_path
        # Run importsql.py
        result = subprocess.run(['python', 'importsql.py'], capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(result.stderr)
        print(result.stdout)
    except Exception as e:
        raise RuntimeError(f"Failed to run importsql.py: {e}")

def browse_folder():
    folder_selected.set(filedialog.askdirectory())

def submit():
    username = entry_username.get()
    password = entry_password.get()
    db_name = entry_db.get()
    folder = folder_selected.get()
    
    if not all([username, password, db_name, folder]):
        messagebox.showerror("Error", "All fields are required.")
        return
    
    try:
        install_dependencies()
    except RuntimeError as e:
        messagebox.showerror("Installation Error", str(e))
        return
    
    try:
        run_import_sql(username, password, db_name, folder)
        messagebox.showinfo("Success", "Data imported successfully.")
    except RuntimeError as e:
        messagebox.showerror("Import Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("ImportSQL GUI")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Database Name:").grid(row=2, column=0, padx=10, pady=5)
entry_db = tk.Entry(root)
entry_db.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Folder Path:").grid(row=3, column=0, padx=10, pady=5)
folder_selected = tk.StringVar()
entry_folder = tk.Entry(root, textvariable=folder_selected)
entry_folder.grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_folder).grid(row=3, column=2, padx=10, pady=5)

tk.Button(root, text="Submit", command=submit).grid(row=4, column=1, pady=20)

root.mainloop()