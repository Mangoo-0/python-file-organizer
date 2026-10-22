# File Organizer

A simple Python project that sorts files into folders based on their extensions.

I built this project to practise Python and learn how to work with files and folders. It can organize images, videos, documents, and other file types automatically.

### How it works

The program scans a folder, checks each file's extension, and assigns it to a category.

- Images: `.jpg`, `.jpeg`, `.png`, `.gif`
- Videos: `.mp4`, `.mkv`
- Documents: `.pdf`, `.txt`
- Other file types go into `others`

It creates the required folders automatically. Before organizing, you can choose to preview the changes or move the files. It also checks if a file with the same name already exists in the destination folder.

### Run it

You need Python 3 installed.

1. Download `file_organizer.py`.
2. Open the file and set the folder path you want to organize.
3. Run it from your terminal:

```bash
python file_organizer.py
```

Enter `no` to preview the changes or `yes` to move the files.

### What I learned

While making this, I practised using `pathlib`, `shutil`, loops, conditions, and input validation. I also learned how to preview file operations before executing them.

This is one of my beginner Python projects, and I'll improve it as I learn more.

