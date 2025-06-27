# 🎓 Career Counselling System (Python GUI)

This GUI-based Python project helps students explore career paths by stream — **Science 🔬**, **Commerce 💼**, or **Arts 🎨**. Users can select a stream and degree to view suitable colleges dynamically from a CSV file. Built using **Tkinter**, it combines functionality and ease of use with a visually engaging design.

---

## 🚀 Features

- ✅ Stream & degree selection via dynamic dropdowns
- 📊 College list displayed in tabular form
- 🖼️ Background image integration for GUI aesthetics
- 🔍 Easy navigation and 🔄 refresh functionality
- 📄 Reads college/course info from CSV data source

---

## 📁 Folder Structure

```
CareerCounsellingSystem/
├── assets/
│   └── background.png         # GUI background image
├── data/
│   └── colleges.csv           # CSV file with college/course info
├── main.py                    # Main Tkinter GUI application
└── README.md                  # This documentation
```

---

## 🧰 Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `pandas` (for handling CSV)

Install pandas if not available:
```bash
pip install pandas
```

---

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CareerCounsellingSystem.git
   cd CareerCounsellingSystem
   ```

2. Run the application:
   ```bash
   python main.py
   ```

---

## 📄 CSV Format (colleges.csv)

Ensure your CSV file contains the following headers:

```csv
Stream,Degree,College Name,Location
Science,BSc,XYZ College,Mumbai
Commerce,BCom,ABC University,Pune
Arts,BA,DEF Institute,Delhi
```

---

## 📸 Screenshots (Optional)

> Add GUI screenshots here if uploading to GitHub

---

## 👨‍💻 Author

**Nikhil Navale**  
For feedback or suggestions, feel free to connect.

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

> 🎯 Ideal for educational and academic mini-projects using Python and Tkinter.
