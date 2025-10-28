# app_key_logger.py
import tkinter as tk
from datetime import datetime

LOGFILE = "key_log.txt"

def log_key(event):
    # event.char is the printable character (if any)
    # event.keysym is the symbolic key name (Return, BackSpace, Shift_L, etc.)
    key = event.char if event.char not in ("", None) else f"<{event.keysym}>"
    ts = datetime.now().isoformat(sep=' ', timespec='seconds')
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(f"{ts}\t{key}\n")
    status_var.set(f"Last: {repr(key)}")

def clear_log():
    open(LOGFILE, "w", encoding="utf-8").close()
    status_var.set("Log cleared")

root = tk.Tk()
root.title("App-local Key Logger (for testing/debugging)")

status_var = tk.StringVar(value="Ready")
info = tk.Label(root, text="Type inside the box below. Keys will be logged to 'key_log.txt'.\nThis app logs only when it has focus.")
info.pack(padx=10, pady=(10, 0))

text = tk.Text(root, width=70, height=15)
text.pack(padx=10, pady=10)
text.focus_set()

text.bind("<Key>", log_key)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=(0,10))
clear_btn = tk.Button(btn_frame, text="Clear log file", command=clear_log)
clear_btn.pack(side="left", padx=5)
quit_btn = tk.Button(btn_frame, text="Quit", command=root.destroy)
quit_btn.pack(side="left", padx=5)

status = tk.Label(root, textvariable=status_var, anchor="w")
status.pack(fill="x", padx=10, pady=(0,10))

root.mainloop()
