import PySimpleGUI as psg
import os
import subprocess


def convert_to_mp4(file, ffmpeg_path):
    name, ext = os.path.splitext(file)
    out_name = name + "_convert.wmv"
    command = [ffmpeg_path, '-i', file, '-c:v', 'wmv1', out_name]
    subprocess.call(command)
    print(f"Finished converting {file}")


psg.theme("DarkTeal2")
layout = [
    [psg.T("")],
    [psg.Text("Choose a file: "), psg.Input(), psg.FileBrowse(key="-IN-")],
    [psg.Button("Submit")]
]

# Building Window
window = psg.Window('My File Browser', layout, size=(600, 150))

ffmpeg_path = 'executables/ffmpeg'  # ffmpeg path

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Submit":
        convert_to_mp4(values["-IN-"], ffmpeg_path)

window.close()
