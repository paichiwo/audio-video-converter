import os
import data
import subprocess
from tkinter import PhotoImage, Label, Listbox, Button, Radiobutton, messagebox, filedialog
from tkinterdnd2 import *
from helpers import center_window, showinfo, showsettings


def use_ffmpeg(input_file, output_file, video_codec):
    """Use ffmpeg for conversion"""
    ffmpeg_command = ['./executables/ffmpeg', '-i', input_file, '-c:v', video_codec, '-y', output_file]
    process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, error = process.communicate()
    if process.returncode == 0:
        print('Conversion completed successfully')
    else:
        print(output)
        print(error)
        print(process.returncode)


def converter_window():
    """Main window where the conversion takes place"""
    def browse():
        """Get a path for chosen file to be converted"""
        filename = filedialog.askopenfilename()
        if filename[-4:] in data.media_file_formats:
            paths_listbox.insert('end', filename)
        else:
            message_label.configure(text="This format is not allowed")

    def clear():
        """Clear the path window"""
        paths_listbox.delete(0, 'end')

    def convert(video_codec='libmp3lame', file_extension='.mp3'):
        """Call for conversion."""
        input_file = paths_listbox.get('active')
        name, ext = os.path.splitext(input_file)
        output_file = name + "_convert" + file_extension
        try:
            use_ffmpeg(input_file, output_file, video_codec)
        except FileNotFoundError:
            print("No ffmpeg found")

    root = TkinterDnD.Tk()
    center_window(root, 480, 420)
    root.title(f"Audio-Video Converter v{data.version}")
    root.iconbitmap('./images/audio-video_converter_icon_512x512.ico')
    root.configure(bg=data.colors[2])
    root.resizable(False, False)

    background_image = PhotoImage(
        master=root,
        file='./images/background.png')
    background_label = Label(
        root,
        image=background_image)
    background_label.pack()

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
        command=showsettings)
    settings_button.place(x=421, y=15)

    paths_listbox = Listbox(
        root,
        bg=data.colors[0],
        width=65,
        height=12,
        borderwidth=0,
        highlightthickness=0)
    paths_listbox.place(x=44, y=60)

    browse_image = PhotoImage(
        master=root,
        file='./images/browse_button.png')
    browse_button = Button(
        root,
        image=browse_image,
        bg=data.colors[2],
        activebackground=data.colors[2],
        borderwidth=0,
        command=browse)
    browse_button.place(x=32, y=335)

    convert_image = PhotoImage(
        master=root,
        file='./images/convert_button.png')
    convert_button = Button(
        root,
        image=convert_image,
        bg=data.colors[2],
        activebackground=data.colors[2],
        borderwidth=0,
        command=convert)
    convert_button.place(x=188, y=335)

    clear_image = PhotoImage(
        master=root,
        file='./images/clear_button.png')
    clear_button = Button(
        root,
        image=clear_image,
        bg=data.colors[2],
        activebackground=data.colors[2],
        borderwidth=0,
        command=clear)
    clear_button.place(x=345, y=335)

    message_label = Label(
        root,
        text="test",
        font=(data.font, 11),
        fg=data.colors[3],
        bg=data.colors[2])
    message_label.place(x=5, y=396)

    root.mainloop()


if __name__ == '__main__':
    converter_window()
