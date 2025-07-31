import os
import PyPDF2

merger = PyPDF2.PdfMerger()

file_list = os.listdir("arquivos")
file_list.sort()
print(file_list)

for arquivo in file_list:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

merger.write("PDF Final.pdf")