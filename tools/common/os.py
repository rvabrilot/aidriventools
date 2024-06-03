import re
import hashlib
import os

def escape_filename(original_file_name):
    invalid_chars = r'[<>:"/\\|?*]'

    # Escape all invalid characters
    escaped_file_name = re.sub(invalid_chars, lambda match: '%%%02X' % ord(match.group()), original_file_name)

    return escaped_file_name

def change_filename(file_path, new_filename):
    directory = os.path.dirname(file_path)
    new_path = os.path.join(directory, new_filename)
    os.rename(file_path, new_path)

def generate_md5_hash(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        md5_hash = hashlib.md5(data).hexdigest()
        return md5_hash