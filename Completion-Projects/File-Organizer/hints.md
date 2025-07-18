# File Organizer Script

### 🖥 UI (Command Line):
```
===== File Organizer =====
Enter folder path to organize: D:/Downloads

Organizing files...

Images moved to /Images
PDFs moved to /PDFs
Music, Songs moved to /Audios
Done!
```

### 🧠 Features:

- Detect file types in a folder
- Move them into folders like Images, PDFs, Audios, etc.

### 💡 Hints:

- Use os.listdir() and os.path.splitext() to get extensions
- Use os.makedirs() and shutil.move() to move files
- Organize by common extensions:
    - .jpg, .png → Images
    - .pdf → PDFs
    - .mp3, .wav → Audios