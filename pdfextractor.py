from PyPDF2 import PdfFileWriter, PdfFileReader
import easygui as gui

input_path = gui.fileopenbox(title="Choose the file",default="*.pdf")
readerobj = PdfFileReader(input_path)
writerobj = PdfFileWriter()
total_pages = readerobj.getNumPages()
while True:
    start_page = gui.enterbox("Enter the beginning of the page to extract","Enter box")
    start_page = int(start_page)
                
    if start_page <= total_pages:
        while True:
            end_page = gui.enterbox("Enter the ending of the page to extract","Enter box")
            end_page = int(end_page)
            if end_page >= start_page and end_page <= total_pages:
                break
            else:
                gui.msgbox("Enter the valid page number.","Warning")
        break
    else:
        gui.msgbox("Enter the valid page number","Warning")

output_path = gui.filesavebox(title="Save as", default="*.pdf")

if start_page == end_page:
    page = readerobj.getPage(start_page-1)
    writerobj.addPage(page)
else:
    for i in range(start_page-1,end_page):
        page = readerobj.getPage(i)
        writerobj.addPage(page)

with open(output_path,"wb") as target:
    writerobj.write(target)








