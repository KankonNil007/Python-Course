# Exercise 08 - Merge the PDF

from pypdf import PdfWriter

x = PdfWriter()

files = ["076-Exercise-08/PDFs/file-example_PDF_1MB.pdf", "076-Exercise-08/PDFs/file-example_PDF_1MB.pdf", "076-Exercise-08/PDFs/file-sample_150kB.pdf"]

for pdf in files:
    x.append(pdf)

x.write("076-Exercise-08/MergedPDF.pdf")
x.close()