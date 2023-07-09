from tkinter import PhotoImage, Label, Listbox, Button, Radiobutton
from tkinterdnd2 import *
import data
from helpers import showinfo


def browse():
    pass


def clear():
    pass


def convert():
    pass


# def use_ffmpeg(input_file, output_file, video_codec):
#     """Convert a file with ffmpeg"""
#     # Check if the output file already exists
#     if os.path.exists(output_file):
#         # Ask the user if they want to overwrite the file
#         choice = psg.popup_yes_no("Overwrite?")
#         if choice != 'Yes':
#             # User does not want to overwrite, exit the function
#             print("Conversion canceled.")
#             return
#
#     ffmpeg_command = ["executables/ffmpeg", "-i", input_file, "-c:v", video_codec, "-y", output_file]
#     process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#     output, error = process.communicate()
#     if process.returncode == 0:
#         # Conversion successful
#         print("Conversion completed successfully!")
#     else:
#         print(output)
#         print(error)
#         print(process.returncode)


# def converter(video_codec, file_extension):
#     """Call for conversion."""
#     input_file = values["-IN-"]
#     name, ext = os.path.splitext(input_file)
#     output_file = name + "_convert" + file_extension
#     try:
#         use_ffmpeg(input_file, output_file, video_codec)
#     except FileNotFoundError:
#         print("No ffmpeg found")


root = TkinterDnD.Tk()
root.title("Audio-Video Converter")
root.geometry("480x420")
root.configure(bg=data.colors[2])


background_image = PhotoImage(
    master=root,
    file='./images/background.png')
background_label = Label(
    root,
    image=background_image)
background_label.pack()

version_label = Label(
    text=f"Audio-Video Converter v{data.version}",
    font=(data.font, 12),
    fg=data.colors[3],
    bg=data.colors[2])
version_label.place(x=45, y=10)

info_image = PhotoImage(
    master=root,
    file='./images/info_icon.png')
info_button = Button(
    root,
    image=info_image,
    bg=data.colors[2],
    activebackground=data.colors[2],
    borderwidth=0,
    command=showinfo)
info_button.place(x=392, y=15)

settings_image = PhotoImage(
    master=root,
    file='./images/settings_icon.png')
settings_button = Button(
    root,
    image=settings_image,
    bg=data.colors[2],
    activebackground=data.colors[2],
    borderwidth=0,
    command=show_settings)
settings_button.place(x=421, y=15)

browse_image = PhotoImage(
    master=root,
    file='./images/browse_button.png')
browse_button = Button(
    root,
    image=browse_image,
    bg=data.colors[2],
    activebackground=data.colors[2],
    borderwidth=0)
browse_button.place(x=32, y=335)

convert_image = PhotoImage(
    master=root,
    file='./images/convert_button.png')
convert_button = Button(
    root,
    image=convert_image,
    bg=data.colors[2],
    activebackground=data.colors[2],
    borderwidth=0)
convert_button.place(x=188, y=335)

clear_image = PhotoImage(
    master=root,
    file='./images/clear_button.png')
clear_button = Button(
    root,
    image=clear_image,
    bg=data.colors[2],
    activebackground=data.colors[2],
    borderwidth=0)
clear_button.place(x=345, y=335)

message_label = Label(
    root,
    text="test",
    font=(data.font, 11),
    fg=data.colors[3],
    bg=data.colors[2])
message_label.place(x=5, y=396)

root.mainloop()
