import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(file_path, pages_per_file):
    pdf = PdfReader(file_path)
    for i in range(0, len(pdf.pages), pages_per_file):
        pdf_writer = PdfWriter()
        for j in range(i, min(i + pages_per_file, len(pdf.pages))):
            pdf_writer.add_page(pdf.pages[j])

        output_dir = os.path.join(os.path.dirname(file_path), os.path.splitext(os.path.basename(file_path))[0])
        os.makedirs(output_dir, exist_ok=True)

        output_filename = os.path.join(output_dir, f'{i // pages_per_file}.pdf')
        with open(output_filename, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

def select_folder():
    pages_per_file = entry.get()
    if not pages_per_file.isdigit():
        messagebox.showerror("Error", "Please enter a valid number of pages per split file")
        return

    pages_per_file = int(pages_per_file)
    folder_path = filedialog.askdirectory()
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            split_pdf(os.path.join(folder_path, filename), pages_per_file)

root = tk.Tk()
label = tk.Label(root, text='Enter the number of pages per split file:')
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text='Select Folder', command=select_folder)
button.pack()
root.mainloop()
