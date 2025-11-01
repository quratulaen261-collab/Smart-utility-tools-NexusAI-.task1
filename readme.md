# 🧠 Nexus AI – File Management Utility  

This project is part of the **Nexus AI Task**, designed to **automate file organization, renaming, and reading operations** using simple, modular Python scripts.  

---

## 🚀 **Overview**

The project manages files inside a target folder (`test_files`) by:
1. **Renaming files** based on a given prefix.  
2. **Organizing files** into structured folders.  
3. **Reading file content** for processing or validation.  
4. **Logging results** and process status automatically.

---

## 🗂️ **Project Structure**

Nexus AI Task
├── file_manager.py # Handles renaming and organizing files
├── file_reader.py # Reads file content
├── utils.py # Logging and helper utilities
├── main.py # Main executable script
└── test_files/ # Folder containing test data

---

## ⚙️ **How It Works**

### **1️⃣ File Check**
Before any action, the script checks if `file.txt` exists inside the `test_files` folder.

### **2️⃣ File Operations**
If found:
- Renames files with a common prefix using `rename_files()`.  
- Organizes files into proper folders via `organize_files()`.  
- Reads file content using `read_file()`.  

### **3️⃣ Logging**
Progress and success messages are recorded using `log()` from `utils.py`.

---

## 💻 **Usage**

### **Run the Script**
```bash
python main.py
