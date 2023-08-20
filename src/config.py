from src.helpers import resource_path


# data for converter.py

version = "1.0"
font = "Calibri"
colors = ['#087e8b', '#ff5a5f', '#3c3c3c', '#f5f5f5']

ffmpeg_path = resource_path('bin\\ffmpeg.exe')

images = {
    'icon': resource_path('images/audio-video_converter_icon_512x512.ico'),
    'icon_png': resource_path('images/audio-video_converter_icon_64x64.png'),
    'bg': resource_path('images/background.png'),
    'info': resource_path('images/info_icon.png'),
    'settings': resource_path('images/settings_icon.png'),
    'browse': resource_path('images/browse_button.png'),
    'convert': resource_path('images/convert_button.png'),
    'clear': resource_path('images/clear_button.png'),
    'filepath': resource_path('images/filepath.png'),
    'folder': resource_path('images/folder_icon.png'),
    'plus': resource_path('images/plus_16x16.png'),
    'plus_large': resource_path('images/plus.png'),
    'save': resource_path('images/save_button.png'),
    'github': resource_path('images/github_icon_32x32.png')
}

media_file_formats = [
    '.webm',
    '.mpg',
    '.mp2',
    '.mpeg',
    '.mpe',
    '.mpv',
    '.ogg',
    '.mp4',
    '.m4p',
    '.m4v',
    '.avi',
    '.wmv',
    '.mov',
    '.qt',
    '.flv',
    '.swf',
    '.mp3',
    '.flac',
    '.wav',
    '.aac',
    '.aiff',
    '.m4a']


github_link = "https://github.com/paichiwo/"

info_header = f"""
AUDIO-VIDEO CONVERTER v{version}
Paichiwo
2023
"""

info_text = """
Thank you for your interest in my Audio-Video Converter application. 
Application is coded in Python and it's utilizing 'FFmpeg' capabilities.

What is FFmpeg?
FFmpeg is a powerful open-source software library and command-line tool 
used for handling multimedia data. It can decode, encode, transcode, mux, 
demux, stream, and filter various audio and video formats. 
http://ffmpeg.org/

Features:
Convert audio files such as MP3, WAV, AAC, FLAC, etc. between audio formats.
Convert video files such as MP4, AVI, MKV, MOV, etc. to other video or audio.

Future plans:
Process multiple audio/video files simultaneously, saving time and effort.
"""
