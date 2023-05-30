import tkinter as tk
from tkinter import Label, Button, Listbox, END, filedialog
from tkinterdnd2 import *
import glob
import os

root = TkinterDnD.Tk()
root.title("Video Converter")
root.geometry("380x500")

file_list = []


def get_all_paths(event):

    files = []
    if isinstance(event.data, str):
        if os.path.isdir(event.data):  # Handle a folder drop
            folder_path = event.data
            for file in glob.glob(f"{folder_path}/*.*"):
                attributes = os.stat(file).st_file_attributes
                if not os.path.basename(file).startswith('.') and attributes != 6:
                    files.append(file)
        else:  # Handle a single or multiple file drop
            for file in event.data.split():
                print(file)
                files.append(file)
    for file in files:
        ListboxWidget.insert(END, file)
    return files


def update_listbox(event):
    file_list.extend(get_all_paths(event))

    print(len(file_list))

    if len(file_list) > 0:
        frame_1.pack_forget()
        frame_2.pack()


def clear_listbox():
    ListboxWidget.delete(0, END)
    file_list.clear()


def folder_selection():
    folder_selected = filedialog.askdirectory()
    return folder_selected


# Create widgets
frame_1 = tk.Frame(root)
frame_1.pack()

image = tk.PhotoImage(file='drop.png')  # Drag & Drop image
image_label = Label(frame_1, image=image, padx=5, pady=5)

frame_2 = tk.Frame()

ClearButton = Button(frame_2, text="Clear", command=clear_listbox)
FolderButton = Button(frame_2, text="Destination", command=folder_selection)
ListboxWidget = Listbox(frame_2, width=100)

# Place widgets
image_label.grid(row=0, column=0, columnspan=3, sticky="news", padx=5, pady=5)
ClearButton.grid(row=2, column=0, padx=5, pady=5)
FolderButton.grid(row=2, column=1, padx=5, pady=5)
ListboxWidget.grid(row=1, column=0, columnspan=5, sticky="news", padx=5, pady=5)


# Drag & Drop binding
image_label.drop_target_register(DND_ALL)
image_label.dnd_bind("<<Drop>>", update_listbox)
ListboxWidget.drop_target_register(DND_ALL)
ListboxWidget.dnd_bind("<<Drop>>", update_listbox)

root.mainloop()
