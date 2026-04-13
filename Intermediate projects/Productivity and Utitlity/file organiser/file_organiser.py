import os
import shutil

# Define categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".tar"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Get extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        moved = False
        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)

                # Handle duplicates
                dest_path = os.path.join(category_folder, filename)
                if os.path.exists(dest_path):
                    base, extension = os.path.splitext(filename)
                    i = 1
                    while os.path.exists(dest_path):
                        dest_path = os.path.join(category_folder, f"{base}_{i}{extension}")
                        i += 1

                shutil.move(file_path, dest_path)
                print(f"Moved: {filename} -> {category}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} -> Others")

if __name__ == "__main__":
    folder = input("Enter folder path to organize: ")
    organize_folder(folder)
    print("Organization complete!")