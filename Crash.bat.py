import tkinter as tk
import random
import time
import winsound

root = tk.Tk()
root.title("Windows Update")
root.attributes("-toolwindow", True)

# =========================
# HORROR ICON
# =========================
import random

icon = tk.PhotoImage(width=32, height=32)

for x in range(32):
    for y in range(32):

        # Dark shadow background
        icon.put("#0a0a0a", (x, y))

        # Blood-red face area
        if 4 < x < 28 and 4 < y < 28:
            icon.put("#5a0000", (x, y))

        # Inner darker core
        if 8 < x < 24 and 8 < y < 24:
            icon.put("#8B0000", (x, y))

        # Glowing red eyes
        if (9 < x < 14 and 11 < y < 17):
            icon.put("#ff0000", (x, y))
        if (18 < x < 23 and 11 < y < 17):
            icon.put("#ff0000", (x, y))

        # Black pupils
        if (11 < x < 13 and 13 < y < 15):
            icon.put("black", (x, y))
        if (20 < x < 22 and 13 < y < 15):
            icon.put("black", (x, y))

        # Distorted mouth
        if 10 < x < 22 and 20 < y < 25:
            icon.put("black", (x, y))

        # Random glitch noise (corruption effect)
        if random.randint(0, 40) == 1:
            icon.put("#300000", (x, y))

root.iconphoto(True, icon)

# =========================
# Window Protection
# =========================
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.bind("<Alt-F4>", lambda e: "break")
root.bind("<Escape>", lambda e: "break")

root.attributes("-fullscreen", True)
root.attributes("-topmost", True)

# =========================
# Variables
# =========================
percent = 0
exit_hold_start = None
closing_started = False

messages = [
    "Unauthorized access detected.",
    "Encrypting system files...",
    "Firewall disabled.",
    "System registry corrupted.",
    "Critical files missing.",
    "Boot sector modified.",
    "Admin privileges escalated.",
    "Remote session established."
]

phases = [
    "Deleting Files",
    "Uninstalling drivers",
    "Configuring system settings",
    "Wiping BIOS",
    "Uninstalling Mcafee",
    "Corrupting Windows",
    "Draining Battery Cycle",
    "Deleting system components",
    "Hijacking Cellular Machinery",
    "Overclocking GPU"
]

current_phase = phases[0]

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

canvas = tk.Canvas(root, bg="#8B0000", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# =========================
# Keep Focus (Fake Lock Effect)
# =========================
def keep_focus():
    root.lift()
    root.focus_force()
    root.after(500, keep_focus)

keep_focus()

# =========================
# Beep
# =========================
def beep_alert():
    winsound.Beep(random.randint(800, 2000), 120)

# =========================
# Flicker Effect
# =========================
def flicker_effect():
    colors = ["#8B0000", "#550000", "#AA0000", "#330000"]
    canvas.config(bg=random.choice(colors))
    root.after(random.randint(80, 150), flicker_effect)

flicker_effect()

# =========================
# Random Warning Popups
# =========================
def random_warning():
    x = random.randint(0, width)
    y = random.randint(0, height)

    canvas.create_text(
        x,
        y,
        text=random.choice(messages),
        fill="yellow",
        font=("Consolas", 18, "bold")
    )

    beep_alert()
    root.after(random.randint(1000, 2500), random_warning)

random_warning()

# =========================
# Draw Screen
# =========================
def draw_screen():
    canvas.delete("center")

    # Glitch lines
    for _ in range(25):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = x1 + random.randint(-250, 250)
        canvas.create_line(x1, y1, x2, y1, fill="black", width=3)

    canvas.create_text(
        width // 2,
        height // 2 - 60,
        text=f"{percent}%",
        fill="white",
        font=("Segoe UI", 90),
        tags="center"
    )

    canvas.create_text(
        width // 2,
        height // 2 + 40,
        text=current_phase,
        fill="white",
        font=("Segoe UI", 28),
        tags="center"
    )

    canvas.create_text(
        width // 2,
        height // 2 + 100,
        text="Do not turn off your computer.",
        fill="white",
        font=("Segoe UI", 20),
        tags="center"
    )

# =========================
# Progress Logic
# =========================
def update_progress():
    global percent, current_phase, closing_started

    if percent < 100:
        percent += 1

        if percent % random.randint(4, 9) == 0:
            current_phase = random.choice(phases)

        if percent == 85:
            canvas.create_text(
                width // 2,
                height // 2 - 200,
                text="CRITICAL SYSTEM FAILURE",
                fill="red",
                font=("Segoe UI", 45, "bold")
            )
            beep_alert()

        draw_screen()
        root.after(random.randint(400, 800), update_progress)

    elif not closing_started:
        closing_started = True
        root.after(5000, root.destroy)

# =========================
# Hidden Exit (Hold Q 3 sec)
# =========================
def hold_to_exit(event):
    global exit_hold_start
    if exit_hold_start is None:
        exit_hold_start = time.time()
    elif time.time() - exit_hold_start > 3:
        root.destroy()

def release_exit(event):
    global exit_hold_start
    exit_hold_start = None

root.bind("q", hold_to_exit)
root.bind("<KeyRelease-q>", release_exit)

# =========================
# Start
# =========================
draw_screen()
update_progress()

root.mainloop()
