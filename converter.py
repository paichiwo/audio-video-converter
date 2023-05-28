import PySimpleGUI as psg
import os
import ffmpeg

import os
import ffmpeg


def convert_to_wmv(file):
    name, ext = os.path.splitext(file)
    count = 1
    out_name = name + "_convert_{}{}".format(count, ext)

    while os.path.exists(out_name):
        count += 1
        out_name = name + "_convert_{}{}".format(count, ext)

    def progress_callback(progress):
        print("Converting {}: {:.2f}%".format(file, progress))

    ffmpeg.input(file).output(out_name, vcodec='wmv1', progress=progress_callback).run()
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
        try:
            convert_to_wmv(values["-IN-"])
            break
        except ffmpeg._run.Error:
            print("codec error")

window.close()

