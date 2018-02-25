from PyPDF2 import PdfFileReader, PdfFileWriter
import csv
yearbook="1_yearbooks/syb56.pdf"
table_pages="2_table_page_numbers/tables.csv"
output_folder="3_table_pdfs/"
pdf_file = PdfFileReader(file(yearbook, "rb"))
with open(table_pages, 'rb') as f:
    reader = csv.reader(f)
    tables = list(reader)
for table in tables[1:]:
    print table
    table_number=table[0];begin=int(table[1]);end=int(table[2])
    output = PdfFileWriter()
    for page in range(begin-1,end):
        output.addPage(pdf_file.getPage(page))
    outputStream = file(output_folder+table_number+".pdf", "wb")
    output.write(outputStream)
    outputStream.close()
