import json
import webbrowser
from tkinter import Tk, PhotoImage, Label, Button, filedialog
import data


def center_window(window, width, height):
    """Create a window in the center of the screen, using desired dimensions"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def open_url(url):
    """Open given link in the web browser"""
    webbrowser.open(url)


def load_codecs_from_json():
    """Get dictionary of file formats with corresponding codecs"""
    with open('codecs.json', 'r') as file:
        codecs = json.load(file)
    return codecs


def showinfo():
    """Create a new tkinter window with information about the application"""
    info = Tk()
    center_window(info, 480, 500)
    info.title("About")
    info.iconbitmap('./images/audio-video_converter_icon_512x512.ico')
    info.configure(bg=data.colors[2])
    info.resizable(False, False)

    about_app_header = Label(
        info,
        text=data.info_header,
        font=(data.font, 11, 'bold'),
        fg=data.colors[3],
        bg=data.colors[2],
        justify='center')
    about_app_header.pack()

    app_icon_image = PhotoImage(
        master=info,
        file='./images/audio-video_converter_icon_64x64.png')
    app_icon_label = Label(
        info,
        image=app_icon_image,
        bg=data.colors[2])
    app_icon_label.pack()

    about_app_label = Label(
        info,
        text=data.info_text,
        font=(data.font, 10),
        fg=data.colors[3],
        bg=data.colors[2],
        justify='center')
    about_app_label.pack()

    github_image = PhotoImage(
        master=info,
        file='./images/github_icon_32x32.png')
    github_image_label = Label(
        info,
        image=github_image,
        bg=data.colors[2],
        cursor='hand2')
    github_image_label.pack()
    github_image_label.bind("<Button-1>", lambda _: open_url(data.github_link))

    github_label = Label(
        info,
        text="My GitHub",
        font=(data.font, 10),
        fg=data.colors[3],
        bg=data.colors[2],
        justify='center',
        cursor='hand2')
    github_label.pack()
    github_label.bind("<Button-1>", lambda _: open_url(data.github_link))

    info.mainloop()


def showsettings():
    """Create a new tkinter window with settings for the application"""

    def get_output_path():
        """Get a file path for the chosen output folder"""
        folder_selected = filedialog.askdirectory()
        output_path_label.configure(text=folder_selected)
        return

    def save_settings():
        output_folder = output_path_label.cget('text')
        with open('settings.json', 'w') as file:
            json.dump({'output_folder': output_folder}, file)
        settings_info_label.configure(text="Settings saved")

    def load_settings():
        try:
            with open('settings.json', 'r') as file:
                settings = json.load(file)
                return settings['output_folder']
        except json.decoder.JSONDecodeError:
            return "C:/Users/"

    sett = Tk()
    center_window(sett, 480, 300)
    sett.title("Settings")
    sett.iconbitmap('./images/audio-video_converter_icon_512x512.ico')
    sett.configure(bg=data.colors[2])
    sett.resizable(False, False)

    settings_header = Label(
        sett,
        text="SETTINGS\n\n",
        font=(data.font, 13, 'bold'),
        fg=data.colors[3],
        bg=data.colors[2],
        justify='center')
    settings_header.pack()

    output_path_info = Label(
        sett,
        text="Choose output folder:",
        font=(data.font, 11),
        fg=data.colors[3],
        bg=data.colors[2],
        justify='center')
    output_path_info.pack()

    output_path_image = PhotoImage(
        master=sett,
        file='./images/filepath.png')
    output_path_image_label = Label(
        sett,
        image=output_path_image,
        bg=data.colors[2],
        borderwidth=0)
    output_path_image_label.pack()

    folder_icon_image = PhotoImage(
        master=sett,
        file='./images/folder_icon.png')
    folder_icon_label = Label(
        sett,
        image=folder_icon_image,
        bg=data.colors[0])
    folder_icon_label.place(x=44, y=123)

    output_path_label = Label(
        sett,
        text=load_settings(),
        font=(data.font, 11),
        fg=data.colors[3],
        bg=data.colors[0],
        justify='left')
    output_path_label.place(x=75, y=123)

    output_path_button_image = PhotoImage(
        master=sett,
        file='./images/plus_16x16.png')
    output_path_button = Button(
        sett,
        image=output_path_button_image,
        bg=data.colors[0],
        activebackground=data.colors[0],
        borderwidth=0,
        command=get_output_path)
    output_path_button.place(x=410, y=126)

    save_button_image = PhotoImage(
        master=sett,
        file="./images/save_button.png")
    save_button = Button(
        sett,
        image=save_button_image,
        bg=data.colors[2],
        activebackground=data.colors[2],
        borderwidth=0,
        command=save_settings)
    save_button.pack()

    settings_info_label = Label(
        sett,
        text="",
        font=(data.font, 10),
        fg=data.colors[3],
        bg=data.colors[2])
    settings_info_label.place(x=10, y=278)

    sett.mainloop()
