import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

"from tkinter.messagebox import showinfo" 
filename = fd.askopenfilename()

#Boton de grafos para crear la cabecera de la interfaz 
"""
root = tk.Tk()
root.config(width=300, height=200)
root.title("Boton grafos")
root.resizable(False, False)

text = tk.Text(root, height=12)
text.grid(column=0, row=0, sticky='nsew')
"""

#Funcion para leer el archivo.txt
def open_text_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
)    
#Muestra y abre el filedialog 
  
f = fd.askopenfile()
grafo = f.readlines()
print (grafo)

#Funcion para eliminar el archivo txt seleccionado en la interfaz 
#def delete_interfaz():
    #text.delete(1.0, tk.END)

"""
    filename = fd.askopenfilename(
        title = 'Open a file',
        initialdir= '/home/stiven/MEGA/Univalle/3_Semestre/proyectoGrafos/Grafos',
        filetypes = filetypes)


showinfo(
        title = 'Selected File',
        message = filename
    )
"""
#Boton para seleccionar los archivos
"""
open_button = ttk.Button(   
    root,
    text='Open Files',
    command=open_text_file 

)
#Boton para limpiar la interfaz 
boton = ttk.Button(
    root,
    text='Limpiar interfaz',
    command= delete_interfaz

)
  
#De esta manera ordeno los botones
boton.grid(column=0, row=1, sticky='w', padx=100, pady=10)

open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)

    
# run the application
root.mainloop()   



"""
