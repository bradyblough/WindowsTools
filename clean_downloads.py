# Python script to delete the contents of the Downloads folder
# This script is intended to be run on a Windows system

import os
import shutil

def clear_downloads_folder():
    
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    
    for item_name in os.listdir(downloads_path):
        item_path = os.path.join(downloads_path, item_name)
        
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

if __name__ == "__main__":
    clear_downloads_folder()
    print("Downloads folder cleared.")