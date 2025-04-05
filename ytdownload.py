import yt_dlp



import tkinter as tk
from tkinter import messagebox

def download_video():
    url = url_entry.get()
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("800x600")

# Create and pack widgets
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=40)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=45)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=50)

root.mainloop()