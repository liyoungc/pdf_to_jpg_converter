import os
import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path
from PIL import Image

def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_path_var.set(file_path)
        output_dir_var.set(os.path.dirname(file_path))

def convert_pdf_to_jpeg():
    pdf_file = pdf_path_var.get()
    output_dir = output_dir_var.get()
    num_pages = int(num_pages_var.get())
    dpi = int(dpi_var.get())

    images = convert_from_path(pdf_file, dpi=dpi, fmt='jpeg', last_page=num_pages)

    base_filename = os.path.splitext(os.path.basename(pdf_file))[0]

    for i, img in enumerate(images):
        img.save(f"{output_dir}/{base_filename}_{i + 1}.jpg", "JPEG")

root = tk.Tk()
root.title("PDF to JPEG Converter")

pdf_path_var = tk.StringVar()
output_dir_var = tk.StringVar()
num_pages_var = tk.StringVar()
dpi_var = tk.StringVar()

tk.Label(root, text="PDF file:").grid(row=0, column=0, sticky="w")
pdf_path_entry = tk.Entry(root, textvariable=pdf_path_var, width=50).grid(row=0, column=1)
browse_button = tk.Button(root, text="Browse", command=browse_pdf).grid(row=0, column=2)

tk.Label(root, text="Output directory:").grid(row=1, column=0, sticky="w")
output_dir_entry = tk.Entry(root, textvariable=output_dir_var, width=50).grid(row=1, column=1)

tk.Label(root, text="Number of pages to convert:").grid(row=2, column=0, sticky="w")
num_pages_entry = tk.Entry(root, textvariable=num_pages_var, width=10).grid(row=2, column=1, sticky="w")
num_pages_var.set("4")

tk.Label(root, text="DPI:").grid(row=3, column=0, sticky="w")
dpi_entry = tk.Entry(root, textvariable=dpi_var, width=10).grid(row=3, column=1, sticky="w")
dpi_var.set("300")

convert_button = tk.Button(root, text="Convert PDF to JPEG", command=convert_pdf_to_jpeg).grid(row=4, column=1)

root.mainloop()
