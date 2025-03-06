import os
import pathlib

def list_video_files(root_dir):
    """Lists all video files in the given directory and its subdirectories."""

    video_extensions = {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".3gp"} # Add more if needed.
    found_files = []

    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = pathlib.Path(root) / file
            if file_path.suffix.lower() in video_extensions:
                found_files.append(str(file_path))

    return found_files

if __name__ == "__main__":
    try:
        root_directory = pathlib.Path(os.environ.get("SystemDrive", "C:")) # Default to C: drive

        print(f"Searching for video files in: {root_directory}")

        video_files = list_video_files(root_directory)

        if video_files:
            print("\nVideo files found:")
            for file in video_files:
                print(file)
        else:
            print("No video files found.")

    except PermissionError:
        print("Permission denied. Run this script as administrator.")

    except Exception as e:
        print(f"An error occurred: {e}")