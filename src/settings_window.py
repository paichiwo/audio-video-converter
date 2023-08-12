from src.config import images, colors, font
from tkinter import Tk, filedialog, Label, PhotoImage, Button
from src.helpers import load_settings_from_json, save_settings_to_json


def showsettings():
    """Create a new tkinter window with settings for the application"""

    def get_output_path():
        """Get a file path for the chosen output folder"""
        folder_selected = filedialog.askdirectory()
        output_path_label.configure(text=folder_selected)
        return

    def save_settings():
        """Save settings callback"""
        output_folder = output_path_label.cget('text')
        save_settings_to_json(output_folder)
        settings_info_label.configure(text="Settings saved")

    sett = Tk()
    sett.geometry("480x250")
    sett.title("Settings")
    sett.iconbitmap(images['icon'])
    sett.configure(bg=colors[2])
    sett.resizable(False, False)

    settings_header = Label(
        sett,
        text="SETTINGS\n\n",
        font=(font, 13, 'bold'),
        fg=colors[3],
        bg=colors[2],
        justify='center')
    settings_header.pack()

    output_path_info = Label(
        sett,
        text="Choose output folder:",
        font=(font, 11),
        fg=colors[3],
        bg=colors[2],
        justify='center')
    output_path_info.pack()

    output_path_image = PhotoImage(
        master=sett,
        file=images['filepath'])
    output_path_image_label = Label(
        sett,
        image=output_path_image,
        bg=colors[2],
        borderwidth=0)
    output_path_image_label.pack()

    folder_icon_image = PhotoImage(
        master=sett,
        file=images['folder'])
    folder_icon_label = Label(
        sett,
        image=folder_icon_image,
        bg=colors[0])
    folder_icon_label.place(x=44, y=123)

    output_path_label = Label(
        sett,
        text=load_settings_from_json(),
        font=(font, 10),
        fg=colors[3],
        bg=colors[0],
        justify='left')
    output_path_label.place(x=75, y=123)

    output_path_button_image = PhotoImage(
        master=sett,
        file=images['plus'])
    output_path_button = Button(
        sett,
        image=output_path_button_image,
        bg=colors[0],
        activebackground=colors[0],
        borderwidth=0,
        command=get_output_path)
    output_path_button.place(x=410, y=126)

    save_button_image = PhotoImage(
        master=sett,
        file=images['save'])
    save_button = Button(
        sett,
        image=save_button_image,
        bg=colors[2],
        activebackground=colors[2],
        borderwidth=0,
        command=save_settings)
    save_button.pack()

    settings_info_label = Label(
        sett,
        text="",
        font=(font, 10),
        fg=colors[3],
        bg=colors[2])
    settings_info_label.place(x=10, y=278)

    sett.mainloop()
