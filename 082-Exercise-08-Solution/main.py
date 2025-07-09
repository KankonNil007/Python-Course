# Exercise 08 - Solution

from pypdf import PdfWriter
import os

x = PdfWriter()

files = [file for file in os.listdir("082-Exercise-08-Solution/PDFs") if file.endswith(".pdf")]

directory = "082-Exercise-08-Solution/PDFs/"

filesUpdated = list(map(lambda x : directory + x, files))

for pdf in filesUpdated:
    x.append(pdf)

x.write("082-Exercise-08-Solution/MergedPDF.pdf")
x.close()