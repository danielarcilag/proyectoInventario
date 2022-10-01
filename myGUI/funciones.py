import tkinter as tk
from tkinter import ttk

def ventana():
    root = tk.Tk()
    #  Obtenemos el largo y  ancho de la pantalla
    wtotal = root.winfo_screenwidth()
    htotal = root.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = 600
    hventana = 400

    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)-100

    #  Se lo aplicamos a la geometría de la ventana
    root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
    root.resizable(0,0)

    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    return root
        

def CRUD(title):
    
    componentes = {}

    root = ventana()
    root.columnconfigure(2,weight=1)

    componentes['contenedores'] = [tk.Frame(root),tk.Frame(root),
                                   tk.Frame(root),tk.Frame(root),
                                   tk.Frame(root),tk.Frame(root)]

    contenedor = componentes['contenedores']

    contenedor[0].grid(column=0,row=0,sticky="SE",padx=10,pady=10)
    contenedor[1].grid(column=1,row=0,sticky="S",padx=10,pady=10)
    contenedor[2].grid(column=0,row=1,sticky="NE",pady=10)
    contenedor[3].grid(column=1,row=1,sticky="N",padx=10,pady=10)
    contenedor[4].grid(column=2,row=0,sticky="SW",padx=10,pady=10)
    contenedor[5].grid(column=2,row=1,sticky="NW",padx=10,pady=10)

    lb = tk.Label(root,text=title,font=('helvetica','18','bold'))
    lb.grid(column=1,row=0,sticky="N")

    componentes['imagenes']  = [tk.PhotoImage(file="imgs/crear.png"),
                                tk.PhotoImage(file="imgs/editar.png"),
                                tk.PhotoImage(file="imgs/eliminar.png"),
                                tk.PhotoImage(file="imgs/ver.png"),
                                tk.PhotoImage(file="imgs/volver.png"),
                                tk.PhotoImage(file="imgs/salir.png")]

    imagen = componentes['imagenes']

    componentes['botones']  =  [tk.Button(contenedor[0],image=imagen[0]),
                                tk.Button(contenedor[1],image=imagen[1]),
                                tk.Button(contenedor[2],image=imagen[2]),
                                tk.Button(contenedor[3],image=imagen[3]),
                                tk.Button(contenedor[4],image=imagen[4],command=lambda:[root.destroy(),menuPrincipal()]),
                                tk.Button(contenedor[5],image=imagen[5],command=root.destroy)]

    boton = componentes['botones']

    componentes['labels'] =[tk.Label(contenedor[0],text="CREAR "+ title),
                            tk.Label(contenedor[1],text="EDITAR "+ title),
                            tk.Label(contenedor[2],text="ELIMINAR "+ title),
                            tk.Label(contenedor[3],text="VER "+ title),
                            tk.Label(contenedor[4],text="VOLVER"),
                            tk.Label(contenedor[5],text="SALIR")]
    
    label = componentes['labels']

    for i in range(len(boton)):
        boton[i].pack()
        label[i].pack()

    root.mainloop()


def menuPrincipal():
    
    root = ventana()

    componentes = {}

    componentes['contenedores'] = [tk.Frame(root),tk.Frame(root),
                                   tk.Frame(root),tk.Frame(root)]

    contenedor = componentes['contenedores']

    contenedor[0].grid(column=0,row=0,sticky="SE",padx=10,pady=10)
    contenedor[1].grid(column=1,row=0,sticky="SW",padx=10,pady=10)
    contenedor[2].grid(column=0,row=1,sticky="NE",padx=10,pady=10)
    contenedor[3].grid(column=1,row=1,sticky="NW",padx=10,pady=10)


    componentes['imagenes'] = [tk.PhotoImage(file="imgs/cliente.png"),
                              tk.PhotoImage(file="imgs/productos.png"),
                              tk.PhotoImage(file="imgs/pedido.png"),
                              tk.PhotoImage(file="imgs/salir.png")]

    imagen = componentes['imagenes']

    
    componentes['botones'] = [tk.Button(contenedor[0],image=imagen[0],command = lambda:[root.destroy(),CRUD("CLIENTES")]),
                              tk.Button(contenedor[1],image=imagen[1],command = lambda:[root.destroy(),CRUD("PRODUCTOS")]),
                              tk.Button(contenedor[2],image=imagen[2],command = lambda:[root.destroy(),CRUD("PEDIDOS")]),
                              tk.Button(contenedor[3],image=imagen[3],command=root.destroy)]

    boton = componentes['botones']

    componentes['labels'] = [tk.Label(contenedor[0],text="CLIENTES"),
                             tk.Label(contenedor[1],text="PRODUCTOS"),
                             tk.Label(contenedor[2],text="PEDIDOS"),
                             tk.Label(contenedor[3],text="SALIR")]
    
    label = componentes['labels']

    for i in range(len(boton)):
        boton[i].pack()
        label[i].pack()

    root.mainloop()

    


 