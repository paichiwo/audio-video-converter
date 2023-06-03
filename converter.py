import PySimpleGUI as psg
import os
import subprocess


def calculate_progress(file_path, progress_bar):
    """Calculate the progress of the output file."""
    total_size = os.path.getsize(file_path)
    bytes_processed = 0

    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(4096)  # Read a chunk of data from the file
            if not chunk:
                break  # Reached the end of the file

            bytes_processed += len(chunk)
            percentage = (bytes_processed / total_size) * 100

            # Update the progress bar value
            progress_bar.update(round(percentage))


def use_ffmpeg(input_file, output_file, video_codec, progress_bar):
    """Convert a file with ffmpeg"""
    # Check if the output file already exists
    if os.path.exists(output_file):
        # Ask the user if they want to overwrite the file
        choice = psg.popup_yes_no("Overwrite?")
        if choice != 'Yes':
            # User does not want to overwrite, exit the function
            print("Conversion canceled.")
            return

    ffmpeg_command = ['executables/ffmpeg', '-i', input_file, '-c:v', video_codec, '-y', output_file]
    process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, error = process.communicate()
    calculate_progress(output_file, progress_bar)
    if process.returncode == 0:
        # Conversion successful
        print("Conversion completed successfully!")
    else:
        print(output)
        print(error)
        print(process.returncode)


def converter(video_codec, file_extension):
    """Call for conversion."""
    input_file = values["-IN-"]
    name, ext = os.path.splitext(input_file)
    output_file = name + "_convert" + file_extension
    try:
        use_ffmpeg(input_file, output_file, video_codec, progress)
    except FileNotFoundError:
        print("No ffmpeg found")


psg.theme("DarkBlue")
layout = [
    [psg.Text("Choose a file: "),
     psg.Input(expand_x=True, border_width=0, key="-IN-"),
     psg.Button("Browse", key="-BROWSE-", border_width=0)],
    [
        psg.Push(),
        psg.Radio("MP4", key="-MP4-", default=True, group_id="format"),
        psg.Radio("WMV", key="-WMV-", group_id="format"),
        psg.Radio("AVI", key="-AVI-", group_id="format"),
        psg.Radio("MP3", key="-MP3-", group_id="format"),
        psg.Push()
    ],
    [psg.Push(), psg.Button("Submit", border_width=0), psg.Push()],
    [psg.Text("", key="-MESSAGE-")],
    [psg.VPush()],
    [psg.ProgressBar(100, orientation='h', expand_x=True, size=(20, 2), key='-PBAR-')]
]

# Building Window
window = psg.Window('Video Converter', layout, size=(600, 150))

codec = ""
extension = ""

while True:
    event, values = window.read(timeout=0)
    if event == psg.WIN_CLOSED or event == "Exit":
        break

    elif event == '-BROWSE-':
        file = psg.popup_get_file('', no_window=True)
        window['-IN-'].update(file)

    elif event == "Submit":
        if values["-IN-"]:
            progress = window["-PBAR-"]  # Get the progress bar element
            if values["-WMV-"]:
                codec = 'wmv1'
                extension = '.wmv'
            elif values["-MP4-"]:
                codec = 'h264'
                extension = '.mp4'
            elif values["-AVI-"]:
                codec = 'libx264'
                extension = '.avi'
            elif values["-MP3-"]:
                codec = 'libmp3lame'
                extension = '.mp3'

            converter(codec, extension)

        else:
            print("No file")


window.close()
