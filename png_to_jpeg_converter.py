import tkinter as tk
from tkinter import filedialog, ttk, simpledialog
from PIL import Image

# Create the main window
window = tk.Tk()
window.title("PNG to JPEG Converter")


# Function to convert the image
def convert():
    # Open the input image
    with Image.open(input_label["text"]) as im:
        # Convert the image to RGB mode (removes the alpha channel)
        im = im.convert("RGB")
        # Prompt the user for the output file name
        file_name = simpledialog.askstring("Output file name", "Enter the output file name:")
        # Save the image as JPEG in the output location
        im.save(output_label["text"] + "/" + file_name + ".jpg", "JPEG")


# Function to browse for the input file
def browse_input():
    # Open a file selection dialog
    filepath = filedialog.askopenfilename()
    # Update the input file label with the selected file
    input_label.config(text=filepath)


# Function to browse for the output location
def browse_output():
    # Open a directory selection dialog
    directory = filedialog.askdirectory()
    # Update the output location label with the selected directory
    output_label.config(text=directory)


# Create a style with a font size of 18 points
style = ttk.Style()
style.configure("TLabel", font=("Arial", 18))

# Create a label for the input file
input_label = ttk.Label(text="No file selected")
input_label.grid(row=0, column=0, columnspan=2, sticky="W")

# Create a button to browse for the input file
browse_button = ttk.Button(text="Browse", command=browse_input)
browse_button.grid(row=1, column=0, padx=10, pady=5)

# Create a label for the output location
output_label = ttk.Label(text="No output location selected")
output_label.grid(row=2, column=0, columnspan=2, sticky="W")

# Create a button to browse for the output location
browse_button = ttk.Button(text="Browse", command=browse_output)
browse_button.grid(row=3, column=0, padx=10, pady=5)

# Create a button to start the conversion
convert_button = ttk.Button(text="Convert", command=convert)
convert_button.grid(row=4, column=0, padx=10, pady=5)

# Run the main loop
window.mainloop()
