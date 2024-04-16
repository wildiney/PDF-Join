import os
from pypdf import PdfReader, PdfWriter


def join_pdf_files(filename):
    merger = PdfWriter()
    pages = 0
    for root, dir, files in os.walk('files'):
        for file in files:
            if file.endswith('.pdf'):
                pages += 1
                pdfFile = PdfReader(os.path.join(root, file))
                merger.append(pdfFile)
    if pages == 0:
        print("No pdf files found")
        return False

    merger.write(f"{filename}.pdf")
    return True


def reduce_pdf_size(filename, compression_level=3):
    reader = PdfReader(f"{filename}.pdf")
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    for page in writer.pages:
        page.compress_content_streams(level=compression_level)

    with open(f"{filename}-small.pdf", 'wb') as f:
        writer.write(f)


if __name__ == "__main__":
    filename = input("Save as: ")
    if filename:
        pdfFile = join_pdf_files(filename=filename)
        if (pdfFile):
            reduce_pdf_size(filename=filename, compression_level=9)
    else:
        print("Try again and insert a name for your file.")
