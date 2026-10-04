import os
import shutil

def organize_files():
    directory_path = "./MyWorkspace"
    
    # Setup dummy directory if it does not exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        # Create some basic files for testing
        open(os.path.join(directory_path, "report.pdf"), "w").close()
        open(os.path.join(directory_path, "image.jpg"), "w").close()
        open(os.path.join(directory_path, "notes.txt"), "w").close()

    # Mapping of extensions to target folders
    folder_mapping = {
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Audio_Video": [".mp4", ".mp3", ".mkv"]
    }

    print("Starting file organization process...")
    
    for filename in os.listdir(directory_path):
        current_file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(current_file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            was_moved = False
            
            for target_folder, extensions in folder_mapping.items():
                if file_ext in extensions:
                    destination_dir = os.path.join(directory_path, target_folder)
                    
                    if not os.path.exists(destination_dir):
                        os.makedirs(destination_dir)
                        
                    shutil.move(current_file_path, os.path.join(destination_dir, filename))
                    print(f"Moved file: {filename} -> {target_folder}/")
                    was_moved = True
                    break
            
            if not was_moved:
                misc_dir = os.path.join(directory_path, "Miscellaneous")
                if not os.path.exists(misc_dir):
                    os.makedirs(misc_dir)
                shutil.move(current_file_path, os.path.join(misc_dir, filename))
                print(f"Moved file: {filename} -> Miscellaneous/")

    print("Process completed successfully.")

if __name__ == "__main__":
    organize_files()