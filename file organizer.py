import os
import shutil

folder_path = input("Enter the folder path: ")

# Check path first
if not os.path.exists(folder_path):
    print("❌ Invalid folder path!")
else:
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv"],
        "Others": []
    }

    # Create folders
    for folder in file_types:
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    # Move files
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            moved = False

            for folder, extensions in file_types.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(folder_path, folder, file))
                    print(f"{file} moved to {folder}")
                    moved = True
                    break

            if not moved:
                shutil.move(file_path, os.path.join(folder_path, "Others", file))
                print(f"{file} moved to Others")

    print("\n✅ Files organized successfully!")
