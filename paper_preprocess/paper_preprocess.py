# created by Tianyi Tang @ 2018.11.3
# email : tty8128@bu.edu

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import HTMLConverter


pdf_directory = 'eg_paper.pdf'
html_directory = 'eg_paper.html'
pagenos = set()
debug = 0
maxpages = 0
# output option
imagewriter = None
rotation = 0
stripcontrol = False
layoutmode = 'normal'
codec = 'utf-8'
pageno = 1
scale = 1
caching = True
showpageno = True
laparams = LAParams()


def pdf_parse(pdf_directory, password=None):
    # Open a PDF file.
    fp = open(pdf_directory, 'rb')
    # Create a PDF parser object associated with the file object.
    parser = PDFParser(fp)
    # Create a PDF document object that stores the document structure.
    # Supply the password for initialization.
    document = PDFDocument(parser, password)
    # Check if the document allows text extraction. If not, abort.
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    # Create a PDF resource manager object that stores shared resources.
    rsrcmgr = PDFResourceManager()
    # Create a PDF device object.
    device = PDFDevice(rsrcmgr)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)


def pdf2html(pdf_directory, html_directory, password=None):
    rsrcmgr = PDFResourceManager(caching=caching)
    outfp = open(html_directory, 'wb')
    # device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams,
    #                        imagewriter=imagewriter)
    device = HTMLConverter(rsrcmgr, outfp, codec=codec, scale=scale,
                           layoutmode=layoutmode, laparams=laparams,
                           imagewriter=imagewriter, debug=debug)
    # Open a PDF file.
    fp = open(pdf_directory, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp, pagenos,
                                  maxpages=maxpages, password=password,
                                  caching=caching, check_extractable=True):
        page.rotate = (page.rotate+rotation) % 360
        interpreter.process_page(page)
    fp.close()
    device.close()
    outfp.close()


def main():
    # pdf_parse(pdf_directory)
    pdf2html(pdf_directory, html_directory)


if __name__ == "__main__":
    main()