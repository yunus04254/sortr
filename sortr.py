"""
Sortr: macOS File Organiser
by Yunus Sufian
2023

Description:
Sortr is a macOS file organisation tool. It organises based on file type and placing them into subfolders of their extension.

Key Features:
- Organise audio, video, image, and miscellaneous files.
- Automatically sort files based on their types and extensions.
- Set interval time for automatic sort.
- Customise your sorting preferences with directory.txt
"""
import rumps, subprocess, os, shutil, time
from threading import Thread

customDirectory = "directory.txt"

# Read the content of the customDirectory.txt file
with open(customDirectory, "r") as file:
    directoryPath = file.read().strip()

if directoryPath:
    if os.path.isdir(directoryPath):
        userDownloads = directoryPath
    else:
        pass
else:
    userDownloads = os.path.join(os.path.expanduser("~"), "Downloads")


# Define a class that represents the application.
class Sortr(rumps.App):
    def __init__(self):
        super(Sortr, self).__init__("sortr")

        # Default terminal command
        self.command = "echo 'Sorted!'"

        # Create a menu item to display a timer label
        self.timer_label = rumps.MenuItem("", callback=None)

        # Set the application icon
        self.icon = "sortr.png"

        # Define the menu items
        self.menu = [
            rumps.MenuItem("Sort", callback=self.runComm),  # Run the sorting process
            self.timer_label,  # Display the timer label
            rumps.MenuItem(
                "Set Interval (minutes)", callback=self.set_interval
            ),  # Set the sorting interval
        ]

        # Default sorting interval (in minutes)
        self.interval = 30

        # Create a thread to update the timer label
        self.timer_thread = Thread(target=self.update_timer_label)
        self.timer_thread.daemon = True

    # Callback function to set the sorting interval
    def set_interval(self, _):
        user_input = rumps.Window("Set Interval (minutes)").run()
        try:
            new_interval = int(user_input.text)
            if new_interval > 0:
                self.interval = new_interval
                self.time_remaining = 0
            else:
                rumps.alert("Please enter a valid positive integer for the interval.")
        except ValueError:
            rumps.alert("Please enter a valid positive integer for the interval.")

    # Function to update the timer label
    def update_timer_label(self):
        while True:
            current_time = time.localtime()
            target_time = (current_time.tm_hour, current_time.tm_min + self.interval)
            time_left = self.interval * 60

            if (
                current_time.tm_hour == target_time[0]
                and current_time.tm_min == target_time[1]
            ):
                # Execute the command at the specified time
                self.runComm()
            elif time_left <= 0:
                self.runComm()

            while time_left > 0:
                self.timer_label.title = f"Next run in: {time_left // 60} minutes"
                time_left -= 1
                time.sleep(1)
            time.sleep(self.interval * 60)

    # Quit the application
    def quit(self, _):
        self.timer_thread.join()
        rumps.quit_application()

    # Callback function to start sorting
    def runComm(self, _):
        if not self.timer_thread.is_alive():
            self.timer_thread = Thread(target=self.update_timer_label)
            self.timer_thread.daemon = True
            self.timer_thread.start()
        organiseDirectory(userDownloads)


# Functions for organising files
# These functions move files to specific folders based on their types (audio, video, images, and others)


# Main function to organise a customDirectory
def organiseDirectory(customDirectory):
    organiseFolders(customDirectory)
    organiseAudio(customDirectory)
    organiseVideo(customDirectory)
    organiseImage(customDirectory)
    organiseOther(customDirectory)


# Function to organise audio files
def organiseAudio(customDirectory):
    # Define audio file extensions
    audio_exts = (".mp3", ".m4a", ".wav")
    audio_folder = os.path.join(customDirectory, "Audio")
    os.makedirs(audio_folder, exist_ok=True)

    for root, _, files in os.walk(customDirectory):
        for file in files:
            if file.lower().endswith(audio_exts):
                file_path = os.path.join(root, file)
                shutil.move(file_path, os.path.join(audio_folder, file))


# Function to organise video files
def organiseVideo(customDirectory):
    # Define video file extensions
    video_exts = (".mp4", ".mov", ".mkv")
    video_folder = os.path.join(customDirectory, "Video")
    os.makedirs(video_folder, exist_ok=True)

    for root, _, files in os.walk(customDirectory):
        for file in files:
            if file.lower().endswith(video_exts):
                file_path = os.path.join(root, file)
                shutil.move(file_path, os.path.join(video_folder, file))


# Function to organise image files
def organiseImage(customDirectory):
    # Define image file extensions
    image_exts = (".jpg", ".jpeg", ".png", ".webp")
    image_folder = os.path.join(customDirectory, "Images")
    os.makedirs(image_folder, exist_ok=True)

    for root, _, files in os.walk(customDirectory):
        for file in files:
            if file.lower().endswith(image_exts):
                file_path = os.path.join(root, file)
                shutil.move(file_path, os.path.join(image_folder, file))


# Function to organise files with other extensions
def organiseOther(customDirectory):
    other_folder = os.path.join(customDirectory, "Other")
    os.makedirs(other_folder, exist_ok=True)

    # Define extensions to ignore when sorting
    ignore_extensions = (
        ".mp3",
        ".m4a",
        ".wav",
        ".mp4",
        ".mov",
        ".mkv",
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
    )

    for root, _, files in os.walk(customDirectory):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            if file_extension not in ignore_extensions:
                file_path = os.path.join(root, file)
                shutil.move(file_path, os.path.join(other_folder, file))


# Function to organise folders within the main customDirectory
def organiseFolders(customDirectory):
    other_folders_folder = os.path.join(customDirectory, "Other Folders")
    os.makedirs(other_folders_folder, exist_ok=True)

    # Define folder names to ignore when sorting
    ignore_folders = {"Audio", "Other", "Images", "Video"}

    for folder in os.listdir(customDirectory):
        folder_path = os.path.join(customDirectory, folder)
        if os.path.isdir(folder_path) and folder_path != other_folders_folder:
            if folder not in ignore_folders:
                shutil.move(folder_path, os.path.join(other_folders_folder, folder))


# Entry point for the application
if __name__ == "__main__":
    app = Sortr()
    app.run()
