import tkinter as tk
import qrcode

# Create Tkinter GUI
root = tk.Tk()
root.title("QR Code Generator")

# Create input fields for student information
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

uid_label = tk.Label(root, text="UID:")
uid_label.grid(row=1, column=0)
uid_entry = tk.Entry(root)
uid_entry.grid(row=1, column=1)

branch_label = tk.Label(root, text="Branch:")
branch_label.grid(row=2, column=0)
branch_entry = tk.Entry(root)
branch_entry.grid(row=2, column=1)

group_label = tk.Label(root, text="Group:")
group_label.grid(row=3, column=0)
group_entry = tk.Entry(root)
group_entry.grid(row=3, column=1)

year_label = tk.Label(root, text="Year:")
year_label.grid(row=4, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=4, column=1)

# Function to generate QR code and save as PNG file
def generate_qr_code():
    # Get student information from input fields
    name = name_entry.get()
    uid = uid_entry.get()
    branch = branch_entry.get()
    group = group_entry.get()
    year = year_entry.get()

    # Construct a string containing the student information
    info_string = f"Name: {name}\nUID: {uid}\nBranch: {branch}\nGroup: {group}\nYear: {year}"

    # Generate a QR code containing the student information
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(info_string)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code as a PNG file
    img.save("student_qr.png")

# Create button to generate QR code and save as PNG file
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.grid(row=5, column=0, columnspan=2)

root.mainloop()