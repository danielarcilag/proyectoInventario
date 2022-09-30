import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)

imagen1 = tk.PhotoImage(file="imgs/crear.png")
btn1 = tk.Button(root,image=imagen1)
btn1.grid(column=0,row=0,sticky="SE",padx=30,pady=30)
lbCrear = tk.Label(root,text="CREAR")
lbCrear.grid(column=0,row=0,sticky="SE",padx=45)

imagen2 = tk.PhotoImage(file="imgs/editar.png")
btn2 = tk.Button(root,image=imagen2)
btn2.grid(column=1,row=0,sticky="SW",padx=30,pady=30)
lbEditar = tk.Label(root,text="EDITAR")
lbEditar.grid(column=1,row=0,sticky="SW",padx=45)

imagen3 = tk.PhotoImage(file="imgs/eliminar.png")
btn3 = tk.Button(root,image=imagen3)
btn3.grid(column=0,row=1,sticky="NE",padx=30,pady=30)
lbEliminar = tk.Label(root,text="ELIMINAR")
lbEliminar.grid(column=0,row=1,sticky="SE",padx=40,pady=100)

imagen4 = tk.PhotoImage(file="imgs/ver.png")
btn4 = tk.Button(root,image=imagen4)
btn4.grid(column=1,row=1,sticky="NW",padx=30,pady=30)
lbVer = tk.Label(root,text="VER")
lbVer.grid(column=1,row=1,sticky="SW",padx=55,pady=100)


root.mainloop()