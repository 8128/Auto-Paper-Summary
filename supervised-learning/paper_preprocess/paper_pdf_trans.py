# created by Tianyi Tang @ 2018.11.3
# email : tty8128@bu.edu

import sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import HTMLConverter, TextConverter

# options for pdfparser
pdf_directory = 'eg_paper.pdf'
html_directory = 'eg_paper.html'
txt_directory = 'eg_paper.txt'
pagenos = set()
debug = 0
maxpages = 0
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


def pdf2txt(pdf_directory, txt_directory, password=None):
    rsrcmgr = PDFResourceManager(caching=caching)
    outfp = open(txt_directory, 'wb')
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams,
                           imagewriter=imagewriter)
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


def pdf2html(pdf_directory, html_directory, password=None):
    rsrcmgr = PDFResourceManager(caching=caching)
    outfp = open(html_directory, 'wb')
    device = HTMLConverter(rsrcmgr, outfp, codec=codec, scale=scale,
                           layoutmode=layoutmode, laparams=laparams,
                           imagewriter=imagewriter, debug=debug)
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
    if sys.argv[1]:
      pdf_directory = sys.argv[1]
    if sys.argv[2]:
      html_directory = sys.argv[2]
    if len(sys.argv) >= 4:
      sys.exit(1)
    pdf2html(pdf_directory, html_directory)
    pdf2txt(pdf_directory, txt_directory)


if __name__ == "__main__":
    main()
