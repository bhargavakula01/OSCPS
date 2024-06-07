import tkinter as tk

class DraggableSprite:
    def __init__(self, canvas, image, x, y):
        self.canvas = canvas
        self.image = image
        self.id = canvas.create_image(x, y, image=self.image, anchor=tk.NW)
        self.canvas.tag_bind(self.id, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.id, "<ButtonRelease-1>", self.on_release)
        self.canvas.tag_bind(self.id, "<B1-Motion>", self.on_move)
        self.x = x
        self.y = y
        self.dragging = False

    def on_press(self, event):
        self.dragging = True
        self.start_x = event.x
        self.start_y = event.y

    def on_release(self, event):
        self.dragging = False

    def on_move(self, event):
        if self.dragging:
            dx = event.x - self.start_x
            dy = event.y - self.start_y
            self.canvas.move(self.id, dx, dy)
            self.start_x = event.x
            self.start_y = event.y

# Create the main window
root = tk.Tk()
root.title("Draggable Sprite")

# Create a Canvas widget that fills the entire window and expands with it
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Load an image (replace 'image.png' with your image file)
image = tk.PhotoImage(file="image.png")

# Create a draggable sprite
sprite = DraggableSprite(canvas, image, 100, 100)

# Run the main event loop
root.mainloop()

