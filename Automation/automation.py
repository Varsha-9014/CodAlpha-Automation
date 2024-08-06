import os
import shutil

# Define the directory path and file extensions with their corresponding folder names
directory_path = r"D:\html1"
file_types = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.ogg'],
    'programs' : ['.py'],
    'games':[],
    'ppt':['.pdf'],
    'movies':[],
    'songs':[],
}

# Create the folders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(directory_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files into their corresponding folders
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(directory_path, folder))
                print(f'Moved {filename} to {folder}')
                break

