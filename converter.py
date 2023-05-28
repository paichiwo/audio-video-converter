import PySimpleGUI as psg
import moviepy.editor as moviepy


file_name = "tests/joystick"
psg.theme("DarkTeal2")
layout = [[psg.T("")], [psg.Text("Choose a file: "), psg.Input(), psg.FileBrowse(key="-IN-")], [psg.Button("Submit")]]

# Building Window
window = psg.Window('My File Browser', layout, size=(1000, 150))

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Submit":

        clip = moviepy.VideoFileClip(values["-IN-"])
        clip.write_videofile(file_name + "_convert" + ".mp4")

window.close()
