# OD1N-4-LI4NUX #
# --- GUI-VERSION --- #
# https://github.com/Ragekill3377

import os
import subprocess
import customtkinter as ctk
from tkinter import filedialog, messagebox
import hashlib

def select_file(entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, ctk.END)
        entry.insert(0, file_path)


def isCorruptedn(file_path):
    if not os.path.isfile(file_path):
        return False
    try:
        with open(file_path, 'rb') as f:
            file_hash = hashlib.md5()
            while chunk := f.read(8192):
                file_hash.update(chunk)
        return file_hash.hexdigest()
    except Exception as e:
        messagebox.showerror("Error", f"File check failed: {e}")
        return False

# main stuff
def flash_device():
    bl_file = bl_entry.get()
    ap_file = ap_entry.get()
    cp_file = cp_entry.get()
    csc_file = csc_entry.get()
    erase_nand = nand_var.get()
    reboot_flag = reboot_var.get()
    redownload_flag = redownload_var.get()

    
    for file in [bl_file, ap_file, cp_file, csc_file]:
        if file and not isCorruptedn(file):
            messagebox.showerror("Error", f"FILE: {file} seems to be corrupted. Please verify it.")
            return

    # cmd exec
    command = ['odin4']
    if bl_file: command.extend(['-b', bl_file])
    if ap_file: command.extend(['-a', ap_file])
    if cp_file: command.extend(['-c', cp_file])
    if csc_file: command.extend(['-s', csc_file])
    if erase_nand: command.append('-e')
    if reboot_flag: command.append('--reboot')
    if redownload_flag: command.append('--redownload')

    
    def update_progress(process):
        for line in process.stdout:
            progress_text.insert(ctk.END, line.decode('utf-8'))
            progress_text.see(ctk.END)

    try:
        progress_text.delete(1.0, ctk.END)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        root.after(100, update_progress, process)
        process.wait()
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Flashing failed: {e}")

# ---- GUI ----


ctk.set_appearance_mode("dark")  # "dark", "light", or "system"
ctk.set_default_color_theme("dark-blue")


root = ctk.CTk()
root.title("Odin-4-Linux")
root.geometry("900x700")


nand_var = ctk.BooleanVar()
reboot_var = ctk.BooleanVar()
redownload_var = ctk.BooleanVar()


bg_color = "#2E2E2E"
text_color = "#FFFFFF"
root.configure(bg=bg_color) 

# Tabs view
tabview = ctk.CTkTabview(root)
tabview.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# BL
tab_bl = tabview.add("Bootloader")
bl_label = ctk.CTkLabel(tab_bl, text="Bootloader (BL):", fg_color=bg_color)
bl_label.grid(row=0, column=0, padx=10, pady=10)
bl_entry = ctk.CTkEntry(tab_bl, width=350)
bl_entry.grid(row=0, column=1, padx=10, pady=10)
bl_button = ctk.CTkButton(tab_bl, text="Browse", command=lambda: select_file(bl_entry), fg_color="black")
bl_button.grid(row=0, column=2, padx=10, pady=10)

# AP
tab_ap = tabview.add("AP")
ap_label = ctk.CTkLabel(tab_ap, text="AP file:", fg_color=bg_color)
ap_label.grid(row=0, column=0, padx=10, pady=10)
ap_entry = ctk.CTkEntry(tab_ap, width=350)
ap_entry.grid(row=0, column=1, padx=10, pady=10)
ap_button = ctk.CTkButton(tab_ap, text="Browse", command=lambda: select_file(ap_entry), fg_color="black")
ap_button.grid(row=0, column=2, padx=10, pady=10)

# CP
tab_cp = tabview.add("CP")
cp_label = ctk.CTkLabel(tab_cp, text="CP file:", fg_color=bg_color)
cp_label.grid(row=0, column=0, padx=10, pady=10)
cp_entry = ctk.CTkEntry(tab_cp, width=350)
cp_entry.grid(row=0, column=1, padx=10, pady=10)
cp_button = ctk.CTkButton(tab_cp, text="Browse", command=lambda: select_file(cp_entry), fg_color="black")
cp_button.grid(row=0, column=2, padx=10, pady=10)

# CSC
tab_csc = tabview.add("CSC")
csc_label = ctk.CTkLabel(tab_csc, text="CSC file:", fg_color=bg_color)
csc_label.grid(row=0, column=0, padx=10, pady=10)
csc_entry = ctk.CTkEntry(tab_csc, width=350)
csc_entry.grid(row=0, column=1, padx=10, pady=10)
csc_button = ctk.CTkButton(tab_csc, text="Browse", command=lambda: select_file(csc_entry), fg_color="black")
csc_button.grid(row=0, column=2, padx=10, pady=10)

# Checkboxes
tab_options = tabview.add("Options")
nand_check = ctk.CTkCheckBox(tab_options, text="Erase NAND", variable=nand_var, fg_color=bg_color)
nand_check.grid(row=1, column=0, padx=10, pady=10)

reboot_check = ctk.CTkCheckBox(tab_options, text="Reboot after flash", variable=reboot_var, fg_color=bg_color)
reboot_check.grid(row=1, column=1, padx=10, pady=10)

redownload_check = ctk.CTkCheckBox(tab_options, text="Redownload mode", variable=redownload_var, fg_color=bg_color)
redownload_check.grid(row=1, column=2, padx=10, pady=10)

# Flash
flash_button = ctk.CTkButton(root, text="Flash", command=flash_device, width=120, corner_radius=15, fg_color="black")
flash_button.grid(row=1, column=0, padx=20, pady=20)

# Just outputs command's output, which you would normally see in terminal.
progress_text = ctk.CTkTextbox(root, height=20, width=80, corner_radius=15, fg_color=bg_color)
progress_text.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

# run
root.mainloop()
