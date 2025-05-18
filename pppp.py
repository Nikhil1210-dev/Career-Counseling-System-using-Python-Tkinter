import tkinter
from tkinter import *
from tkinter import messagebox, ttk
import pandas as pd
from PIL import Image, ImageTk


def show_colleges_in_table(dataframe):
    """Displays the DataFrame in a new window with a table layout."""
    if dataframe.empty:
        messagebox.showinfo("Status", "No colleges found for this degree.")
        return

    table_window = Toplevel(root)
    table_window.title("Colleges")
    table_window.geometry("3000x700")

    frame = Frame(table_window)
    frame.pack(fill=BOTH, expand=True)

    # Create a Treeview to display the DataFrame
    tree = ttk.Treeview(frame, columns=list(dataframe.columns), show="headings")
    tree.pack(fill=BOTH, expand=True)

    # Configure the column headers
    for col in dataframe.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    # Insert rows into the Treeview
    for index, row in dataframe.iterrows():
        tree.insert("", "end", values=list(row))


root = tkinter.Tk()
root.geometry("1792x1024")

image = Image.open("wallpaper.jpg")
image = image.resize((1550, 1024))  # Resize if needed

# Convert the image to a Tkinter-compatible format
image_path = ImageTk.PhotoImage(image)

bg_image = tkinter.Label(root, image=image_path)
bg_image.place(relheight=1, relwidth=1)

root.title("Career Counseling")
head_label = tkinter.Label(root, text="Career Counseling", font=("algerian", 30))
head_label.pack(anchor=tkinter.W, padx=540, pady=25)

# Load CSV files
bbf_df = pd.read_csv("1.csv")
bbi_df = pd.read_csv("2.csv")
bcca_df = pd.read_csv("4.csv")
bba_df = pd.read_csv("3.csv")
engineering_df = pd.read_csv("Book1.csv")


def update_degree_dropdown(*args):
    selected_stream = stream_dropdown.get()
    if selected_stream == "Science":
        degree_dropdown['values'] = ["Medical", "Engineering", "Pharma"]
    elif selected_stream == "Commerce":
        degree_dropdown['values'] = ["BBA", "BCCA", "BBF", "BBI"]
    elif selected_stream == "Arts":
        degree_dropdown['values'] = ["Interior Design", "Graphics Design", "Animation"]
    else:
        degree_dropdown['values'] = []


def OnClick_Showcolleges():
    stream = stream_dropdown.get()
    degree = degree_dropdown.get()
    if stream and degree:
        if degree == "Engineering":
            show_colleges_in_table(engineering_df)
        elif degree == "BBF":
            show_colleges_in_table(bbf_df)
        elif degree == "BBI":
            show_colleges_in_table(bbi_df)
        elif degree == "BCCA":
            show_colleges_in_table(bcca_df)
        elif degree == "BBA":
            show_colleges_in_table(bba_df)
        else:
            messagebox.showinfo("Status", "No colleges found for this degree.")
    else:
        messagebox.showwarning("Warning", "Field left blank")


def refresh_fields():
    """Reset the stream and degree dropdowns."""
    stream_dropdown.set("")  # Clear stream selection
    degree_dropdown.set("")  # Clear degree selection
    degree_dropdown["values"] = []  # Clear degree options


stream_label = tkinter.Label(root, text="Select Stream", font=("calibri", 24))
stream_label.pack(anchor=tkinter.W, padx=640, pady=30)
stream_dropdown = ttk.Combobox(root, values=["Science", "Arts", "Commerce"])
stream_dropdown.pack(anchor=tkinter.W, padx=660, pady=15)
stream_dropdown.bind("<<ComboboxSelected>>", update_degree_dropdown)

degree_label = ttk.Label(root, text="Select Degree", font=("Calibri", 24))
degree_label.pack(anchor=tkinter.W, padx=640, pady=30)
degree_dropdown = ttk.Combobox(root)
degree_dropdown.pack(anchor=tkinter.W, padx=660, pady=15)

update_degree_dropdown()
Showcollege_button = tkinter.Button(
    root,
    text="Show Colleges",
    command=OnClick_Showcolleges,
    font=("arial black", 24),
    bg="#4CAF50",  # Green background
    fg="red",  # White text
    activebackground="#45a049",  # Darker green when pressed
    activeforeground="red",  # White text when pressed
)
Showcollege_button.pack(anchor=tkinter.W, padx=590, pady=60)

# Refresh Button
Refresh_button = tkinter.Button(
    root,
    text="Refresh",
    command=refresh_fields,
    font=("arial black", 24),
    bg="#4CAF50",  # green background
    fg="black",  # White text
    activebackground="#45a049",  # Darker green when pressed
    activeforeground="black",  # Black text when pressed
)
Refresh_button.pack(anchor=tkinter.W, padx=655, pady=10)

root.mainloop()
