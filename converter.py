import os
import subprocess
import threading
from tkinterdnd2 import *
from tkinter import PhotoImage, Label, Listbox, Button, filedialog, ttk, StringVar, DoubleVar, messagebox
import src.config as data
from src.info_window import showinfo
from src.settings_window import showsettings
from src.helpers import center_window, load_codecs_from_json, extract_duration, track_progress


def converter_window():
    """Main window where the conversion takes place"""

    def use_ffmpeg(input_file, output_file, video_codec, progress_callback):
        """Use ffmpeg for conversion"""
        ffmpeg_command = ['./executables/ffmpeg', '-i', input_file, '-c:v', video_codec, '-y', output_file]
        process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   universal_newlines=True)

        duration = extract_duration(process.stderr)
        track_progress(process.stderr, duration, progress_callback)

        output, error = process.communicate()
        if process.returncode == 0:
            message_label.configure(text="Conversion completed successfully")
        else:
            error_message = f"""Error occurred during conversion:\n\n
            Output:\n{output}\n\n
            Error:\n{error}\n\n
            Return Code: {process.returncode}"""
            messagebox.showerror("Conversion Error", error_message)

    def browse():
        """Get a path for chosen file to be converted"""
        filename = filedialog.askopenfilename()
        if filename.endswith(tuple(data.media_file_formats)):
            paths_listbox.insert('end', filename)
        else:
            message_label.configure(text="This format is not allowed")

    def clear():
        """Clear the path window"""
        paths_listbox.delete(0, 'end')

    def convert():
        """Call for conversion"""

        def update_progress(progress):
            progress_var.set(progress)
            root.update_idletasks()

        def convert_in_thread():
            input_file = paths_listbox.get('active')
            name, ext = os.path.splitext(input_file)
            selected_format = format_box.get()
            output_file = name + "_convert" + selected_format
            codecs = load_codecs_from_json()
            codec_to_be_used = codecs[selected_format]

            try:
                use_ffmpeg(input_file, output_file, codec_to_be_used, update_progress)
            except FileNotFoundError:
                print("No ffmpeg found")

        # Start the conversion in a separate thread
        thread = threading.Thread(target=convert_in_thread)
        thread.start()

    # Window elements
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
        fg=data.colors[3],
        width=65,
        height=12,
        borderwidth=0,
        highlightthickness=0)
    paths_listbox.place(x=44, y=60)

    extensions = StringVar()
    format_box = ttk.Combobox(
        root,
        textvariable=extensions,
        state='readonly',
        font=(data.font, 9), width=6)
    format_box['values'] = sorted(data.media_file_formats)
    format_box.current(10)
    format_box.place(x=209, y=290)

    progress_var = DoubleVar()
    progress_bar = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='determinate',
        variable=progress_var)
    progress_bar.place(x=0, y=395, width=480, height=5)

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
        font=(data.font, 10),
        fg=data.colors[3],
        bg=data.colors[2])
    message_label.place(x=5, y=400)

    root.mainloop()


if __name__ == '__main__':
    converter_window()
