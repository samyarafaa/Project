import tkinter as tk

from tkinter import messagebox

from gtts import gTTS


import os

import threading


def play_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            threading.Thread(target=generate_and_play_tts, args=(text,)).start()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to play.")

def generate_and_play_tts(text):
    tts = gTTS(text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3" if os.name == "nt" else "open output.mp3")


def clear_text():
    text_entry.delete("1.0", tk.END)


def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

#
root = tk.Tk()
root.title("Text-to-Speech App")
root.geometry("500x400")
root.config(bg="#f0f8ff")


text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=50, font=("Arial", 12))
text_entry.pack(pady=20)


button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)


play_button = tk.Button(
    button_frame, 
    text="🔊 Play", 
    command=play_text, 
    bg="#4caf50", 
    fg="white", 
    font=("Arial", 12), 
    padx=20, 
    pady=5
)
play_button.grid(row=0, column=0, padx=10)

set_button = tk.Button(
    button_frame, 
    text="🔧 set", 
    command=clear_text, 
    bg="#ff9800", 
    fg="white", 
    font=("Arial", 12), 
    padx=20, 
    pady=5
)
set_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(
    button_frame, 
    text="❌ Exit", 
    command=exit_app, 
    bg="#f44336", 
    fg="white", 
    font=("Arial", 12), 
    padx=20, 
    pady=5
)
exit_button.grid(row=0, column=2, padx=10)


root.mainloop()