import tkinter as tk
from PIL import Image, ImageTk
import os

class DesktopPet:
    def __init__(self, root, image_path):
        self.root = root
        self.root.overrideredirect(True)  # Remove window decorations (title bar, etc.)
        self.root.geometry('200x200+400+400')  # Set initial position and size
        self.root.wm_attributes("-topmost", True)  # Keep window on top

        # Load the image
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        # Create a label to hold the image
        self.label = tk.Label(root, image=self.photo, bd=0)
        self.label.pack()

        # Bind mouse events for dragging the window
        self.label.bind("<Button-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.do_move)

        # Initialize position variables
        self.offset_x = 0
        self.offset_y = 0

    def start_move(self, event):
        self.offset_x = event.x
        self.offset_y = event.y

    def do_move(self, event):
        x = self.root.winfo_pointerx() - self.offset_x
        y = self.root.winfo_pointery() - self.offset_y
        self.root.geometry(f'+{x}+{y}')

if __name__ == "__main__":
    # Define the path to the image
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, 'Image', 'Egg.png')

    # Create the main window
    root = tk.Tk()

    # Initialize the desktop pet
    pet = DesktopPet(root, image_path)

    # Run the application
    root.mainloop()
