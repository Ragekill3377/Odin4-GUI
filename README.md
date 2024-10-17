# Odin4 GUI for Linux

- This project is a Python-based GUI for **Odin4**, a command-line flashing tool for Samsung devices on Linux.
- Samsung's Odin on Linux is no longer a dream! This is an **official version leaked from Samsung.**

## Features

- **File Flashing**: Supports BL, AP, CP, CSC, and UMS files.
- **Device Detection**: Auto-detect connected Samsung devices. You *WILL* need adb and usbmuxd.
- **Progress Monitoring**: Displays the terminal output of Odin4 during flashing, for Debugging.
- **File Integrity Check**: Prevents flashing corrupted files to avoid bricking the device.
- **Reboot Options**: Provides options for rebooting or downloading mode after flashing.
- **Odin-Like**: Feels just like the normal odin on Windows.

## Screenshot

![Screenshot Preview](Odin4-GUI/preview/odin-4-linux.png)

## Installation

### Requirements

1. **Python 3.x**
2. **Odin4**: (Actual binary is in project.)
3. **ADB(Android-Debug-Brdige)**
4. **usbmuxd**

### Steps:

**1**.Run the script:

```bash
./install_odin4.sh
```

**2**.Install dependencies:
- Depending on distro/flavour of linux you're running, install usbmuxd,adb,python,customtkinter(from python-pip).

**3**.Run:
```bash
python3 main.py
```

Open an issue if there are any difficulties.
Disclaimer: Odin4Linux itself is **NOT** open-source, but it is an official samsung leak.
- You can hash check the file or even decompile it to check for any 'unwated' things, even though there are none.
- You are free to use this and modify it however you want.
- Samsung firmware sites (Trusted 100%):-
1. [samfw](https://samfw.com)
2. [sammobile](https://sammobile.com)
- Personally, I use samfw.

# ** I, Ragekill3377, am NOT responsible for any damage caused to your devices by this tool. Flashing incorrectly can lead to bricked devices. Be careful. You are not to blame me. If you try, I'll laugh at you.**
