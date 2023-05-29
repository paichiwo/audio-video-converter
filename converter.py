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


def convert_with_ffmpeg(input_file, output_file, video_codec):
    """Using ffmpeg functions to convert the files."""
    # Check if the output file already exists
    if os.path.exists(output_file):
        # Ask the user if they want to overwrite the file
        choice = psg.popup_yes_no("Overwrite ?")
        if choice != 'Yes':
            # User does not want to overwrite, exit the function
            print("Conversion canceled.")
            return

    ffmpeg_command = ['ffmpeg', '-i', input_file, '-c:v', video_codec, '-y', output_file]
    process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, error = process.communicate()

    if process.returncode == 0:
        # Conversion successful
        print("Conversion completed successfully!")
    else:
        # Error occurred
        print("Conversion failed. Error message:")
        print(error)


def converter(video_codec, file_extension):
    input_file = values["-IN-"]
    name, ext = os.path.splitext(input_file)
    output_file = name + "_convert" + file_extension
    try:
        convert_with_ffmpeg(input_file, output_file, video_codec)
        calculate_progress(output_file, progress)
    except FileNotFoundError:
        print("Please choose a file")


psg.theme("DarkBlue")
layout = [
    [psg.T("")],
    [psg.Text("Choose a file: "), psg.Input(expand_x=True), psg.FileBrowse(key="-IN-")],
    [
        psg.Radio("MP4", key="-MP4-", default=True, group_id="format"),
        psg.Radio("WMV", key="-WMV-", group_id="format"),
        psg.Radio("MP3", key="-MP3-", group_id="format")
    ],
    [psg.Button("Submit")],
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

    elif event == "Submit":
        progress = window["-PBAR-"]  # Get the progress bar element
        if values["-WMV-"]:
            codec = 'wmv1'
            extension = '.wmv'
        if values["-MP4-"]:
            codec = 'h264'
            extension = '.mp4'
        if values["-MP3-"]:
            codec = 'mp3'
            extension = '.mp3'

        converter(codec, extension)

window.close()
