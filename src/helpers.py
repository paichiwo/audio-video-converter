import os
import re
import json
import webbrowser


def center_window(window, width, height):
    """Create a window in the center of the screen, using desired dimensions"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def open_url(url):
    """Open given link in the web browser"""
    webbrowser.open(url)


def get_downloads_folder_path():
    """Get the path to the Downloads folder on Windows"""
    user_profile = os.environ['USERPROFILE']
    downloads_folder = os.path.join(user_profile, 'Downloads')
    return downloads_folder


def load_codecs_from_json():
    """Get dictionary of file formats with corresponding codecs"""
    with open('../data/codecs.json', 'r') as file:
        codecs = json.load(file)
    return codecs


def extract_duration(ffmpeg_output):
    """Extract duration information from ffmpeg output"""
    for line in ffmpeg_output:
        if 'Duration: ' in line:
            match = re.search(r'Duration:\s+(\d{2}):(\d{2}):(\d{2}).\d+', line)
            if match:
                hours, minutes, seconds = map(int, match.groups())
                return hours * 3600 + minutes * 60 + seconds


def track_progress(ffmpeg_output, duration, progress_callback):
    """Extract time progress information from ffmpeg output and call the progress_callback"""
    for line in ffmpeg_output:
        if 'time=' in line and duration:
            match = re.search(r'time=\s*(\d{2}):(\d{2}):(\d{2}).\d+', line)
            if match:
                hours, minutes, seconds = map(int, match.groups())
                current_time = hours * 3600 + minutes * 60 + seconds
                progress = (current_time / duration) * 100
                progress_callback(progress)
