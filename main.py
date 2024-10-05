import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import threading
import time


# Function to get disk usage
def get_disk_usage(path):
    total, used, free = shutil.disk_usage(path)
    return total, used, free


# Function to monitor the disk usage
def monitor_disk(path, threshold):
    while True:
        total, used, free = get_disk_usage(path)
        usage_percent = (used / total) * 100

        # Update the label with the current disk usage
        lbl_usage.config(text=f"Disk Usage: {usage_percent:.2f}%")

        if usage_percent > threshold:
            messagebox.showwarning("Disk Usage Alert", f"Warning! Disk usage has exceeded {threshold}%")

        # Wait for 5 seconds before checking again
        time.sleep(5)


# Function to start monitoring
def start_monitoring():
    directory = filedialog.askdirectory(title="Select Directory to Monitor")
    if not directory:
        messagebox.showerror("Error", "No directory selected")
        return

    threshold = float(entry_threshold.get())

    # Start the monitoring process in a separate thread
    thread = threading.Thread(target=monitor_disk, args=(directory, threshold))
    thread.daemon = True
    thread.start()


# Create the main Tkinter window
root = tk.Tk()
root.title("Disk Usage Monitor")

# Label and Entry for Threshold
lbl_threshold = tk.Label(root, text="Set Disk Usage Threshold (%):")
lbl_threshold.pack(pady=10)

entry_threshold = tk.Entry(root)
entry_threshold.pack(pady=5)
entry_threshold.insert(0, "80")  # Default threshold is set to 80%

# Button to Start Monitoring
btn_start = tk.Button(root, text="Select Directory and Start Monitoring", command=start_monitoring)
btn_start.pack(pady=10)

# Label to display disk usage
lbl_usage = tk.Label(root, text="Disk Usage: N/A")
lbl_usage.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
