from PyPDF2 import PdfFileReader, PdfFileWriter
import csv
pdf_file = PdfFileReader(file("syb56.pdf", "rb"))
with open('tables.csv', 'rb') as f:
    reader = csv.reader(f)
    tables = list(reader)
for table in tables[1:]:
    print table
    table_number=table[0];begin=int(table[1]);end=int(table[2])
    output = PdfFileWriter()
    for page in range(begin-1,end):
        output.addPage(pdf_file.getPage(page))
    outputStream = file(table_number+".pdf", "wb")
    output.write(outputStream)
    outputStream.close()
