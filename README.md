REQUIRES PYTHON TO LAUNCH
Retro Game Auto-Launcher

This tool is designed to automatically launch games like old-school cartridges or discs. It works with USB drives, SD cards, and even discs by detecting when they are inserted and checking for a autorun.json file.

---

How It Works
- autoplay.py (or autoplay.exe) runs in the background and watches for new removable media (USB, SD card, or disc).
- If it finds autorun.json on the media, it launches the specified game, shortcut, or URL.
- autorun_creator.py (or autorun_creator.exe) is a GUI tool for creating the autorun.json file.

Example autorun.json:
{
  "game": "C:\\Users\\YourName\\Desktop\\RetroGame.lnk"
}

This makes your PC feel like a retro console, where inserting media instantly starts the game.

---

Running the Scripts

Option 1: Run from Python
Install requirement:
pip install psutil

Run the autoplay script:
python autoplay.py

Run the GUI creator:
python autorun_creator.py

---

Option 2: Use the EXEs
If you have the .exe files:
- autoplay.exe → Runs in the background and auto-launches games when media is inserted.
- autorun_creator.exe → Creates the autorun.json file for the media.

---

Add Autoplay to Startup (Windows)

Method 1: Startup Folder
1. Press Win + R, type:
shell:startup
2. Copy autoplay.exe into this folder.
3. It will run automatically on login.

Method 2: Registry (Hidden Startup)
Run in Command Prompt (Admin):
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v RetroGameLauncher /t REG_SZ /d "C:\Path\to\autoplay.exe"

---

Notes
- Works with USB drives, SD cards, and optical discs.
- Perfect for retro-style game launching—like inserting a cartridge or disc.
- You can point to .exe, .lnk (shortcuts), or .url files.
- If you unplug and reinsert the media, the game will launch again.
