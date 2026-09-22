import tkinter as tk
import threading
import time


running = False

def runScript():
    log("Running")

def loop():
    global running
    while running:
        runScript()
        time.sleep(2)

def start():
    global running
    if not running:
        running = True
        threading.Thread(target=loop, daemon=True).start()

def stop():
    global running
    running = False
    log("Stopped")

def log(message):
    output.insert(tk.END, message +"\n")
    output.see(tk.END) # unsafe. to be replaced with root.after() or queue.Queue()


root = tk.Tk()
root.geometry("400x200")

tk.Button(root, text="Start", command=start).pack()
tk.Button(root, text="Stop", command=stop).pack()

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

output = tk.Text(frame, height=10, yscrollcommand=scrollbar.set)
output.pack(side="left", fill="both", expand=True)

root.mainloop()