# file_organiser.py
# Automation script — organises files in a folder by extension

import os
import shutil

def organise_folder(folder_path):
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue
        
        # Get file extension
        ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else "misc"
        
        # Create subfolder if it doesn't exist
        subfolder = os.path.join(folder_path, ext)
        os.makedirs(subfolder, exist_ok=True)
        
        # Move file
        shutil.move(filepath, os.path.join(subfolder, filename))
        print(f"Moved: {filename} → {ext}/")

# Run on current directory (for demo)
organise_folder(".")
