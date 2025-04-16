import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from typing import List
import pandas as pd
from models import validate_dataframe
from file_processor import read_file, merge_files


class DataProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Processor")
        self.root.geometry("600x400")
        self.file_paths: List[str] = []

        self.setup_ui()

    def setup_ui(self):
        # File selection frame
        file_frame = ttk.LabelFrame(self.root, text="File Selection", padding="10")
        file_frame.pack(fill="x", padx=10, pady=5)

        ttk.Button(file_frame, text="Add Files", command=self.add_files).pack(
            side="left", padx=5
        )
        ttk.Button(file_frame, text="Clear Files", command=self.clear_files).pack(
            side="left", padx=5
        )

        self.file_listbox = tk.Listbox(file_frame, height=5)
        self.file_listbox.pack(fill="x", pady=5)

        # Output frame
        output_frame = ttk.LabelFrame(self.root, text="Output Settings", padding="10")
        output_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(output_frame, text="Output Directory:").pack(anchor="w")
        self.output_dir = tk.StringVar()
        ttk.Entry(output_frame, textvariable=self.output_dir).pack(fill="x", pady=2)
        ttk.Button(output_frame, text="Browse", command=self.select_output_dir).pack(
            pady=2
        )

        ttk.Label(output_frame, text="Output Filename:").pack(anchor="w")
        self.output_filename = tk.StringVar()
        ttk.Entry(output_frame, textvariable=self.output_filename).pack(
            fill="x", pady=2
        )

        # Process button
        ttk.Button(self.root, text="Process Files", command=self.process_files).pack(
            pady=10
        )

    def add_files(self):
        files = filedialog.askopenfilenames(
            filetypes=[("CSV/Excel files", "*.csv *.xlsx *.xls")]
        )
        if files:
            self.file_paths.extend(files)
            self.update_file_list()

    def clear_files(self):
        self.file_paths.clear()
        self.update_file_list()

    def update_file_list(self):
        self.file_listbox.delete(0, tk.END)
        for file in self.file_paths:
            self.file_listbox.insert(tk.END, Path(file).name)

    def select_output_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_dir.set(directory)

    def process_files(self):
        if not self.file_paths:
            messagebox.showerror("Error", "Please select at least one file")
            return

        if not self.output_dir.get():
            messagebox.showerror("Error", "Please select an output directory")
            return

        if not self.output_filename.get():
            messagebox.showerror("Error", "Please enter an output filename")
            return

        try:
            # Validate all files
            for file_path in self.file_paths:
                df = read_file(file_path)
                validate_dataframe(df)

            # Merge files
            output_path = Path(self.output_dir.get()) / self.output_filename.get()
            merge_files(self.file_paths, str(output_path))

            messagebox.showinfo(
                "Success",
                f"Files processed successfully!\nOutput saved to: {output_path}",
            )

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


def main():
    root = tk.Tk()
    app = DataProcessorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
