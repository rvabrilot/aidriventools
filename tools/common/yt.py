import yt_dlp
import whisper
import os
from tools.common.os import change_filename, generate_md5_hash

# Function to download a YouTube video
def download_video(url, output_folder, use_md5=False, use_yt_id=False):
    
    if not use_yt_id:
        outtmpl = f'{output_folder}/%(title)s.%(ext)s'
    else:
        outtmpl = f'{output_folder}/%(id)s.%(ext)s'

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]/mp4',
        'outtmpl': outtmpl
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            fnames = ydl.extract_info(url, download=False)
            
            if os.name == 'nt':  # Check if the OS is Windows
                directory_char = '\\'
            else:
                directory_char = '/'

            output_file = ydl.prepare_filename(fnames)
            ydl.download([url])

            if use_md5:
                md5_name = generate_md5_hash(output_file)
                returned_filename = md5_name
            else:
                returned_filename = output_file
            
            return returned_filename
    except:
        return "error, no se descargo el video"

def download_audio(url, output_folder, use_md5=False, use_yt_id=False):
    
    if not use_yt_id:
        outtmpl = f'{output_folder}/%(title)s.%(ext)s'
    else:
        outtmpl = f'{output_folder}/%(id)s.%(ext)s'

    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/mp4',
        'outtmpl': outtmpl,
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            fnames = ydl.extract_info(url, download=False)
            
            if os.name == 'nt':  # Check if the OS is Windows
                directory_char = '\\'
            else:
                directory_char = '/'

            output_file = ydl.prepare_filename(fnames)
            ydl.download([url])

            if use_md5:
                md5_name = generate_md5_hash(output_file)
                returned_filename = md5_name
            else:
                returned_filename = output_file.replace('.m4a', '.mp3')
            
            return returned_filename
    except:
        return "error, no se descargo el audio"

def download_mp4s_from_yt(input, output_folder):

    out_text = ""
    lines = input.split('\n')
    for line in lines:
        output_file = download_video(line, output_folder)
        if "error" not in output_file:
            out_text += f"#{line}\n"
        else:
            out_text += f"E{line}\n"
    
    return out_text

def download_mp3s_from_yt(input, output_folder):

    out_text = ""
    lines = input.split('\n')
    for line in lines:
        output_file = download_audio(line, output_folder)
        if "error" not in output_file:
            out_text += f"#{line}\n"
        else:
            out_text += f"E{line}\n"
    
    return out_text
    
def transcribe_mp3(input, output_folder):
    mp3_file = download_audio(input, output_folder, use_md5=False, use_yt_id=True)
    if "error" not in mp3_file:
        print("transcribing...")
        model = whisper.load_model("medium")
        result = model.transcribe(mp3_file)
    else:
        result = mp3_file

    return result["text"]
