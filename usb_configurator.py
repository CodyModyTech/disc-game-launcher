import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

ID_FILE = "autorun.json"

def select_app():
    file_path = filedialog.askopenfilename(
        title="Select Application, Shortcut, or URL",
        filetypes=(("Executable, Shortcut, URL", "*.exe *.lnk *.url"), ("All files", "*.*"))
    )
    if file_path:
        app_entry.delete(0, tk.END)
        app_entry.insert(0, file_path)

def save_json():
    app_path = app_entry.get()
    if not app_path:
        messagebox.showerror("Error", "Please select an application first.")
        return

    save_path = filedialog.asksaveasfilename(
        title="Save autorun.json",
        defaultextension=".json",
        initialfile=ID_FILE,
        filetypes=(("JSON Files", "*.json"), ("All Files", "*.*"))
    )
    if not save_path:
        return  # User canceled

    try:
        with open(save_path, 'w') as f:
            json.dump({"game": app_path}, f, indent=4)
        messagebox.showinfo("Success", f"Saved autorun.json to:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save JSON: {e}")

# GUI Setup
root = tk.Tk()
root.title("Autorun Configurator")
root.geometry("420x200")

tk.Label(root, text="Select Game, Shortcut, or URL:").pack(pady=5)
app_entry = tk.Entry(root, width=50)
app_entry.pack(pady=5)

tk.Button(root, text="Browse", command=select_app).pack(pady=5)
tk.Button(root, text="Save JSON", command=save_json).pack(pady=10)

root.mainloop()
