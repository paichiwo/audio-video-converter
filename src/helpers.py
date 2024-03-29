import os
import re
import json
import sys
import webbrowser


def resource_path(relative_path):
    """Get the absolute path to a resource, accommodating both development and PyInstaller builds"""
    if hasattr(sys, '_MEIPASS'):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)


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
    with open('./data/codecs.json', 'r') as file:
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


def load_settings():
    """Load settings from a JSON file"""
    path = os.path.join(os.environ['LOCALAPPDATA'], 'Tube-Getter', 'settings.json')
    try:
        with open(path, 'r') as file:
            settings = json.load(file)
            return settings.get('output_folder')
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        output_folder = get_downloads_folder_path()
        return output_folder


def save_settings(output_folder):
    """Save settings to a JSON file"""
    settings_file = 'settings.json'
    path = os.path.join(os.environ['LOCALAPPDATA'], 'Tube-Getter')
    settings_path = os.path.join(path, settings_file)
    data = {'output_folder': output_folder}

    if not os.path.exists(path):
        os.makedirs(path)

    with open(settings_path, 'w') as file:
        json.dump(data, file)
