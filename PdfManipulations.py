from PyPDF2 import PdfWriter
from tkinter.filedialog import asksaveasfile
class PDFOperations():
	def __init__(self):
		pass
	def unir_pdf(self,lista,topventana):
		merge=PdfWriter()
		for valor in lista:
			merge.append(valor)
		files=[('Archivo pdf','*.pdf')]
		direccion=asksaveasfile(filetypes=files,defaultextension=files)		
		merge.write(direccion.name)
		merge.close()
		topventana.destroy()



