import tkinter as tk
from tkinter import filedialog, messagebox
from converter import convert_image_to_ascii

class ASCIIConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to ASCII Converter")

        self.file_path = tk.StringVar()
        self.save_path = tk.StringVar()
        self.color_var = tk.BooleanVar()
        self.bg_color_var = tk.BooleanVar()
        self.same_dir_var = tk.BooleanVar()
        self.width_var = tk.IntVar(value=100)
        self.height_var = tk.IntVar(value=100)

        self.create_widgets()

    def create_widgets(self):
        # File selection
        tk.Label(self.root, text="Select Image File:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.file_path, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_file).grid(row=0, column=2, padx=10, pady=10)

        # Save directory selection
        tk.Label(self.root, text="Select Save Directory:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.save_dir_entry = tk.Entry(self.root, textvariable=self.save_path, width=50)
        self.save_dir_entry.grid(row=1, column=1, padx=10, pady=10)
        self.save_dir_button = tk.Button(self.root, text="Browse", command=self.browse_save_dir)
        self.save_dir_button.grid(row=1, column=2, padx=10, pady=10)

        # Checkbox for saving in the same directory as the source image
        tk.Checkbutton(self.root, text="Save in Source Directory", variable=self.same_dir_var, command=self.toggle_save_dir).grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Color toggle
        tk.Checkbutton(self.root, text="Enable Color", variable=self.color_var, command=self.toggle_color_mode).grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Background color toggle (visible only when color mode is enabled)
        self.bg_color_check = tk.Checkbutton(self.root, text="Black Background", variable=self.bg_color_var)

        # Width and Height (hidden by default)
        self.width_label = tk.Label(self.root, text="Width:")
        self.width_entry = tk.Entry(self.root, textvariable=self.width_var, width=10)
        self.height_label = tk.Label(self.root, text="Height:")
        self.height_entry = tk.Entry(self.root, textvariable=self.height_var, width=10)

        # Convert button
        tk.Button(self.root, text="Convert", command=self.convert_to_ascii).grid(row=6, column=1, padx=10, pady=10)

    def toggle_save_dir(self):
        """Enable or disable save directory selection based on 'Save in Source Directory' checkbox."""
        if self.same_dir_var.get():
            self.save_dir_entry.config(state=tk.DISABLED)
            self.save_dir_button.config(state=tk.DISABLED)
        else:
            self.save_dir_entry.config(state=tk.NORMAL)
            self.save_dir_button.config(state=tk.NORMAL)

    def toggle_color_mode(self):
        """Show or hide width, height, and background color fields based on color mode toggle."""
        if self.color_var.get():
            self.width_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
            self.width_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")
            self.height_label.grid(row=4, column=2, padx=10, pady=10, sticky="e")
            self.height_entry.grid(row=4, column=3, padx=10, pady=10, sticky="w")
            self.bg_color_check.grid(row=5, column=1, padx=10, pady=10, sticky="w")
        else:
            self.width_label.grid_remove()
            self.width_entry.grid_remove()
            self.height_label.grid_remove()
            self.height_entry.grid_remove()
            self.bg_color_check.grid_remove()

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif"), ("All files", "*.*")]
        )
        if file_path:
            self.file_path.set(file_path)

    def browse_save_dir(self):
        save_directory = filedialog.askdirectory()
        if save_directory:
            self.save_path.set(save_directory)

    def convert_to_ascii(self):
        image_path = self.file_path.get()
        save_directory = self.save_path.get()
        color = self.color_var.get()
        black_bg = self.bg_color_var.get()
        save_in_source_dir = self.same_dir_var.get()

        # Determine the output path
        if save_in_source_dir:
            output_path = image_path.rsplit('.', 1)[0] + "_output.png" if color else image_path.rsplit('.', 1)[0] + "_output.txt"
        else:
            output_path = f"{save_directory}/output_image.png" if color else f"{save_directory}/output.txt"

        try:
            if color:
                width = self.width_var.get()
                height = self.height_var.get()
                convert_image_to_ascii(image_path, output_path, width=width, color=color, black_bg=black_bg)
            else:
                convert_image_to_ascii(image_path, output_path, color=color)
            
            messagebox.showinfo("Success", f"ASCII art saved to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ASCIIConverterApp(root)
    root.mainloop()
