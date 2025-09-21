from PyPDF2 import PdfMerger

merger = PdfMerger()

pdfs = []
n = int(input("How many pdfs do you want to merge?\n"))

for i in range(n): 
    name = input(f"Enter the name of pdf {i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    with open(pdf, "rb") as f:
        merger.append(f)

merger.write("merged-pdf.pdf")
merger.close()

