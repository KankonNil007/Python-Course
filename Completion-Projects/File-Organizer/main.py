# File Organizer Script

import shutil
import os

print("===== File Organizer =====")

inpPath = input("Enter Folder Path to Organize: ")

if (os.path.exists(inpPath)):
    print("\nOrganizing Files.....")
    os.mkdir(f"{inpPath}/Images")
    os.mkdir(f"{inpPath}/PDFs")
    os.mkdir(f"{inpPath}/Audios")

    files = os.listdir(f"{inpPath}")

    for file in files:
        if (file.endswith(".jpeg") or file.endswith(".png")):
            shutil.move(f"{inpPath}/{file}", f"{inpPath}/Images/{file}")

    print("Images moved to /Images")

    for file in files:
        if (file.endswith(".pdf")):
            shutil.move(f"{inpPath}/{file}", f"{inpPath}/PDFs/{file}")

    print("PDFs moved to /PDFs")

    for file in files:
        if (file.endswith(".mp3") or file.endswith(".wav")):
            shutil.move(f"{inpPath}/{file}", f"{inpPath}/Audios/{file}")

    print("Audioss moved to /Audios")

    print("\nAll Done!!!!!")

else:
    print("Invalid Path!!")