from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


class Main_Windows():
	def __init__(self):
		self.Ventana_Principal=Tk()
		self.Ventana_Principal.geometry('600x400')
		self.Ventana_Principal.title('PDFJNC')
		self.width,self.height=self.Ventana_Principal.winfo_width(),self.Ventana_Principal.winfo_height()
		self.Ventana_Principal.resizable(0,0)
		self.CombinarPdf=Button(self.Ventana_Principal,text='Combinar')
		self.CombinarPdf.config(width=15,height=4)
		self.CombinarPdf['command']=self.Top_CombinarPdf
		self.CombinarPdf.pack(anchor='center',pady=10)

		self.DividirPdf=Button(self.Ventana_Principal,text='Dividir')
		self.DividirPdf.config(width=15,height=4)
		self.DividirPdf.pack(anchor='center',pady=10)

		self.ConvertirPdf=Button(self.Ventana_Principal,text='Convertir a Word')
		self.ConvertirPdf.config(width=15,height=4)
		self.ConvertirPdf.pack(anchor='center',pady=10)
		self.Ventana_Principal.mainloop()
	def Top_CombinarPdf(self):
		lista=askopenfilename(initialdir='/',title="seleccione archivos",filetypes=(('Archivos pdf','*.pdf'),),multiple=True)
		#separando nombres
		nombres=[valor[valor.rfind('/')+1:] for valor in lista]
		if len(lista)>0:
			self.Top_Combinar=Toplevel()
			self.Top_Combinar.title('Lista de Archivos')
			#self.Top_Combinar.resizable(0,0)
			self.vista=ttk.Treeview(self.Top_Combinar)

			self.vista.pack(fill="x")			
			for nombre in nombres:
				self.vista.insert("","end", text=nombre)				
			
			frame=Frame(self.Top_Combinar)
			frame.pack(fill="x")
			moverUp=Button(frame,text='Subir')
			moverUp['command']=self.up_move
			moverUp.grid(row=1,column=0)
			moverDown=Button(frame,text='Bajar')
			moverDown['command']=self.down_move
			moverDown.grid(row=1,column=1)
			#self.Top_Combinar.grab_set()
			self.Top_Combinar.geometry('500x400')
	def up_move(self):
		rows=self.vista.selection()
		for row in rows:
			self.vista.move(row,self.vista.parent(row),self.vista.index(row)-1)
	def down_move(self):
		rows=self.vista.selection()
		for row in rows:
			self.vista.move(row,self.vista.parent(row),self.vista.index(row)+1)


if __name__=="__main__":
	Main_Windows()