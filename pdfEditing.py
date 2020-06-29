import PyPDF2


# Rotating a PDF file
"""
with open('pdfs/original.pdf','rb') as file:
    # print(file)
    reader=PyPDF2.PdfFileReader(file)
    page=(reader.getPage(0)) # page Object
    new_page=(page.rotateCounterClockwise(90))
    writer=PyPDF2.PdfFileWriter()
    writer.addPage(new_page)
    with open('new_orignal.pdf','wb') as new_file:
        writer.write(new_file)
"""

#Merging a pdf file

"""def pdfCombiner(x,y):
    merger=PyPDF2.PdfFileMerger()
    merger.append(x)
    merger.append(y)
    merger.write('Super1.pdf')

pdfCombiner('pdfs/original.pdf','pdfs/original (1).pdf')

"""

#Changing background of PDF or have some mark

template=PyPDF2.PdfFileReader(open('Super1.pdf','rb'))
waterMark=PyPDF2.PdfFileReader(open('pdfs/original (2).pdf','rb'))
output=PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page=template.getPage(i)
    page.mergePage(waterMark.getPage(0))
    output.addPage(page)
    
    with open('waterMarked.pdf','wb') as file:
        output.write(file)
    