from src.config import images, colors, font, info_header, info_text, github_link
from src.helpers import center_window, open_url
from tkinter import Tk, Label, PhotoImage


def showinfo():
    """Create a tkinter window with information about the application"""
    info = Tk()
    center_window(info, 480, 500)
    info.title("About")
    info.iconbitmap(images['icon'])
    info.configure(bg=colors[2])
    info.resizable(False, False)

    about_app_header = Label(
        info,
        text=info_header,
        font=(font, 11, 'bold'),
        fg=colors[3],
        bg=colors[2],
        justify='center')
    about_app_header.pack()

    app_icon_image = PhotoImage(
        master=info,
        file=images['icon_png'])
    app_icon_label = Label(
        info,
        image=app_icon_image,
        bg=colors[2])
    app_icon_label.pack()

    about_app_label = Label(
        info,
        text=info_text,
        font=(font, 10),
        fg=colors[3],
        bg=colors[2],
        justify='center')
    about_app_label.pack()

    github_image = PhotoImage(
        master=info,
        file=images['github'])
    github_image_label = Label(
        info,
        image=github_image,
        bg=colors[2],
        cursor='hand2')
    github_image_label.pack()
    github_image_label.bind("<Button-1>", lambda _: open_url(github_link))

    github_label = Label(
        info,
        text="My GitHub",
        font=(font, 10),
        fg=colors[3],
        bg=colors[2],
        justify='center',
        cursor='hand2')
    github_label.pack()
    github_label.bind("<Button-1>", lambda _: open_url(github_link))

    info.mainloop()
