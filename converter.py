from tkinter import PhotoImage, Label, Listbox, Button, Radiobutton
from tkinterdnd2 import *
import data


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
root.title("Video Audio Converter")
root.geometry("480x420")
root.configure(bg=data.colors[2])


background_image = PhotoImage(file='./images/background.png')
background_label = Label(image=background_image)
background_label.pack()

version_label = Label(
    text=f"Video Audio Converter v{data.version}",
    font=(data.font, 12),
    fg=data.colors[3],
    bg=data.colors[2]
)
version_label.place(x=45, y=10)

info_image = PhotoImage(file='./images/info_icon.png')
info_button = Button(
    image=info_image,
    bg=data.colors[2],
    activebackground=data.colors[2],
    borderwidth=0
)
info_button.place(x=392, y=15)

settings_image = PhotoImage(file='./images/settings_icon.png')
settings_button = Button(
    image=settings_image,
    bg=data.colors[2],
    activebackground=data.colors[2],
    borderwidth=0
)
settings_button.place(x=421, y=15)

root.mainloop()
