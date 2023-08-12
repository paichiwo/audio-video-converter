import os
import subprocess
import threading
from tkinterdnd2 import *
from tkinter import PhotoImage, Label, Listbox, Button, filedialog, ttk, StringVar, DoubleVar, messagebox
from src.config import ffmpeg_path, media_file_formats, colors, font, version, images
from src.info_window import showinfo
from src.settings_window import showsettings
from src.helpers import center_window, load_codecs_from_json, extract_duration, track_progress, load_settings

# Show how many files were converted in some new label
# Make the process faster (maybe add more than one thread)
# Redesign UI for something nicer (custom tkinter)

files_to_convert = []


def converter_window():
    """Create the primary window for the conversion process"""

    def use_ffmpeg(input_file, output_file, video_codec, progress_callback):
        """Utilize FFmpeg for the conversion process"""
        message_label.configure(text="Converting...")
        ffmpeg_command = [ffmpeg_path, '-i', input_file, '-c:v', video_codec, '-y', output_file]
        process = subprocess.Popen(
            ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True
        )

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

    def drop(event):
        """Handle dropped file or files"""
        if event.data and (event.widget == paths_listbox or event.widget == plus_label):
            plus_label.destroy()
            files = paths_listbox.tk.splitlist(event.data)
            for file in files:
                if file.endswith(tuple(media_file_formats)):
                    files_to_convert.append(file)
                    paths_listbox.insert('end', file.split('/')[-1])
                    message_label.configure(text="")
                else:
                    message_label.configure(text="This format is not allowed")

    def browse():
        """select file or files for conversion"""
        # paths_listbox.delete(0, 'end')
        files = filedialog.askopenfilenames()
        if files:
            plus_label.destroy()
            for file in files:
                if file.endswith(tuple(media_file_formats)):
                    files_to_convert.append(file)
                    paths_listbox.insert('end', file.split("/")[-1])
                    message_label.configure(text="")
                else:
                    message_label.configure(text="This format is not allowed")

    def clear():
        """Clear the list of selected files and reset the interface"""
        paths_listbox.delete(0, 'end')
        files_to_convert.clear()

    def convert():
        """Initiate the conversion process"""

        def update_progress(progress):
            """Update the progress bar for each file being converted"""
            progress_var.set(progress)
            root.update_idletasks()

        def convert_in_thread():
            """Perform the conversion in a separate thread"""
            for input_file in files_to_convert:
                name, ext = os.path.splitext(input_file)
                selected_format = format_box.get()
                output_file = name.split('/')[-1] + "_convert" + selected_format
                output_folder = load_settings()
                output_path = os.path.join(output_folder, output_file)
                codecs = load_codecs_from_json()
                codec_to_be_used = codecs[selected_format]

                try:
                    use_ffmpeg(input_file, output_path, codec_to_be_used, update_progress)
                except FileNotFoundError:
                    print("No ffmpeg found")

            # Start the conversion in a separate thread
        thread = threading.Thread(target=convert_in_thread)
        thread.start()

    # Create the main window
    root = TkinterDnD.Tk()
    center_window(root, 480, 420)
    root.title(f"Audio-Video Converter v{version}")
    root.iconbitmap(images['icon'])
    root.configure(bg=colors[2])
    root.resizable(False, False)

    background_image = PhotoImage(master=root, file=images['bg'])
    background_label = Label(root, image=background_image)
    background_label.pack()

    info_image = PhotoImage(master=root, file=images['info'])
    info_button = Button(
        root,
        image=info_image,
        bg=colors[2],
        activebackground=colors[2],
        bd=0,
        command=showinfo)
    info_button.place(x=392, y=15)

    settings_image = PhotoImage(master=root, file=images['settings'])
    settings_button = Button(
        root,
        image=settings_image,
        bg=colors[2],
        activebackground=colors[2],
        bd=0,
        command=showsettings)
    settings_button.place(x=421, y=15)

    paths_listbox = Listbox(
        root,
        bg=colors[0],
        fg=colors[3],
        width=65,
        height=12,
        bd=0,
        highlightthickness=0)
    paths_listbox.place(x=44, y=60)
    paths_listbox.drop_target_register(DND_FILES)
    paths_listbox.dnd_bind('<<Drop>>', drop)

    plus_image = PhotoImage(master=root, file=images['plus_large'])
    plus_label = Label(root, image=plus_image, background=colors[0])
    plus_label.place(x=208, y=120)
    plus_label.drop_target_register(DND_FILES)
    plus_label.dnd_bind('<<Drop>>', drop)

    extensions = StringVar()
    format_box = ttk.Combobox(
        root,
        textvariable=extensions,
        state='readonly',
        font=(font, 9), width=6)
    format_box['values'] = sorted(media_file_formats)
    format_box.current(10)
    format_box.place(x=209, y=290)

    progress_var = DoubleVar()
    progress_bar = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='determinate',
        variable=progress_var)
    progress_bar.place(x=0, y=395, width=480, height=5)

    browse_image = PhotoImage(master=root, file=images['browse'])
    browse_button = Button(
        root,
        image=browse_image,
        bg=colors[2],
        activebackground=colors[2],
        bd=0,
        command=browse)
    browse_button.place(x=32, y=335)

    convert_image = PhotoImage(master=root, file=images['convert'])
    convert_button = Button(
        root,
        image=convert_image,
        bg=colors[2],
        activebackground=colors[2],
        bd=0,
        command=convert)
    convert_button.place(x=188, y=335)

    clear_image = PhotoImage(master=root, file=images['clear'])
    clear_button = Button(
        root,
        image=clear_image,
        bg=colors[2],
        activebackground=colors[2],
        bd=0,
        command=clear)
    clear_button.place(x=345, y=335)

    message_label = Label(
        root,
        text="",
        font=(font, 10),
        fg=colors[3],
        bg=colors[2])
    message_label.place(x=5, y=400)

    root.mainloop()


if __name__ == '__main__':
    converter_window()
