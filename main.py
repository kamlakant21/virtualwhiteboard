import tkinter as tk
from tkinter import ttk
import subprocess

root = tk.Tk()  # create the root window
root.title("Virtual Whiteboard - A Gesture control pen free tool")

# Create a style object for the button
style = ttk.Style()


def run_ppt():
    subprocess.run("python ppt.py", shell=False)


def run_vb():
    subprocess.run("python vb.py", shell=False)


# Create a canvas widget that occupies the full screen
canvas = tk.Canvas(root, width=root.winfo_screenwidth(),
                   height=root.winfo_screenheight())
canvas.pack(fill=tk.BOTH, expand=True)

# Define the start and end colors for the gradient
start_color = "#FFD1DC"  # Baby pink
end_color = "#FFE5B4"  # Peach

# Create a rectangle on the canvas with a gradient fill
for i in range(root.winfo_screenheight()):
    # Calculate the color at this point in the gradient
    r = int((i * int(end_color[1:3], 16) + (root.winfo_screenheight() - i)
            * int(start_color[1:3], 16)) / root.winfo_screenheight())
    g = int((i * int(end_color[3:5], 16) + (root.winfo_screenheight() - i)
            * int(start_color[3:5], 16)) / root.winfo_screenheight())
    b = int((i * int(end_color[5:], 16) + (root.winfo_screenheight() - i)
            * int(start_color[5:], 16)) / root.winfo_screenheight())
    color = "#" + hex(r)[2:].zfill(2) + \
        hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)

    # Draw a horizontal line of the gradient color
    canvas.create_line(0, i, root.winfo_screenwidth(), i, fill=color)

# create a label widget on the canvas
title_label = tk.Label(
    canvas, text="Welcome to Virtual Whiteboard- A Gesture Control Pen Free Tool", bg="#FFD1DC", fg='#171002')
title_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Set the background of the label to the same gradient as the canvas
title_label.config(font=('Helvetica', 40), highlightthickness=0)
title_label.configure(bg="#FFD1DC")
canvas.create_window(root.winfo_screenwidth(
)/2, root.winfo_screenheight()*0.2, anchor=tk.CENTER, window=title_label)


# create a label widget on the canvas
vb_label = tk.Label(
    canvas, text="Tired of traditional drawing tools? \nOur cutting-edge program lets you create stunning artwork using just your hands.\nUnleash your creativity and draw like never before with our state-of-the-art Python app. \nClick the button below to get started!", fg='#171002', bg="#FBD6D2")
vb_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
vb_label.config(font=('Helvetica', 20), highlightthickness=0)

# Configure the style for the button
style.configure('RoundedButton.TButton', foreground='#171002', background='#FFACAC',
                font=('Helvetica', 40), relief='groove', borderwidth=1, width=20)

# Configure the style for the button when the mouse is hovering over it
style.map('RoundedButton.TButton', foreground=[
          ('active', '#171002')], background=[('active', '#F190B7')])

# Create the button on the canvas using the style
vb_button = ttk.Button(canvas, text="Let's Draw",
                       style='RoundedButton.TButton', command=run_vb)
vb_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# create a label widget on the canvas
p_label = tk.Label(
    canvas, text="Revolutionize your presentations with our innovative gesture control feature, allowing you to navigate your slides, \ntake control and draw on your presentation without touching a single button. With intuitive and natural hand gestures, \nyou can deliver a seamless and engaging experience that takes your presentations to the next level.", fg='#171002', bg="#f9dcc5")
p_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
p_label.config(font=('Helvetica', 20), highlightthickness=0)

# Configure the style for the button
style.configure('RoundedButton.TButton', foreground='#171002', background='#FFACAC',
                font=('Helvetica', 40), relief='groove', borderwidth=1, width=20)

# Configure the style for the button when the mouse is hovering over it
style.map('RoundedButton.TButton', foreground=[
          ('active', '#171002')], background=[('active', '#F190B7')])

# Create the button on the canvas using the style
p_button = ttk.Button(canvas, text="Let's Present",
                      style='RoundedButton.TButton', command=run_ppt)
p_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
root.mainloop()  # start the main event loop
