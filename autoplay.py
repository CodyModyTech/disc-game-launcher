import time
import os
import json
import string

PROCESSED_DRIVES = set()

def get_drives():
    return [f"{d}:\\"
            for d in string.ascii_uppercase
            if os.path.exists(f"{d}:\\")]

print("Watching for new drives...")

while True:
    current_drives = set(get_drives())

    # Detect removed drives
    removed_drives = PROCESSED_DRIVES - current_drives
    if removed_drives:
        for drive in removed_drives:
            print(f"Drive removed: {drive}")
        PROCESSED_DRIVES -= removed_drives  # Reset for removed drives

    # Detect new drives
    new_drives = current_drives - PROCESSED_DRIVES
    for drive in new_drives:
        print(f"New drive detected: {drive}")
        autorun_file = os.path.join(drive, "autorun.json")
        if os.path.exists(autorun_file):
            print(f"Found autorun.json on {drive}")
            try:
                with open(autorun_file, "r") as f:
                    config = json.load(f)
                game_path = config.get("game")
                if game_path and os.path.exists(game_path):
                    print(f"Launching {game_path}")
                    os.startfile(game_path)
                else:
                    print(f"Game path invalid or not found: {game_path}")
            except Exception as e:
                print(f"Error reading autorun.json: {e}")
        PROCESSED_DRIVES.add(drive)

    time.sleep(2)
