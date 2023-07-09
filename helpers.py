from tkinter import Tk, PhotoImage, Label
import data


def showinfo():
    """Create new tkinter window with information about the application."""

    info = Tk()
    info.title("About")
    info.geometry("480x420")
    info.configure(bg=data.colors[2])

    about_app_header = Label(
        info,
        text=data.info_header,
        font=(data.font, 10),
        fg=data.colors[3],
        bg=data.colors[2],
        justify='center')
    about_app_header.pack()

    app_icon_image = PhotoImage(
        master=info,
        file='images/audio-video_converter_icon_64x64.png')
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

    info.mainloop()


def showsettings():
    pass
