import webbrowser
from tkinter import Tk, PhotoImage, Label
import data


def open_url(url):
    """Open given link in the web browser"""
    webbrowser.open(url)


def showinfo():
    """Create a new tkinter window with information about the application."""
    info = Tk()
    info.title("About")
    info.geometry("480x500")
    info.configure(bg=data.colors[2])

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
    pass
