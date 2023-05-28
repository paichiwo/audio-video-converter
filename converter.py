import PySimpleGUI as psg
import os
import ffmpeg


def convert_to_mp4(file):
    name, ext = os.path.splitext(file)
    out_name = name + "_convert.mp4"
    ffmpeg.input(file).output(out_name).run()
    print("Finished converting {}".format(file))


psg.theme("DarkTeal2")
layout = [[psg.T("")], [psg.Text("Choose a file: "), psg.Input(), psg.FileBrowse(key="-IN-")], [psg.Button("Submit")]]

# Building Window
window = psg.Window('My File Browser', layout, size=(1000, 150))

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Submit":
        convert_to_mp4(values["-IN-"])

window.close()

