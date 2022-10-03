from model.db_dao import *
import tkinter as tk
from tkinter import ttk
from model.models import *

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

    
    return root
  
def menuCRUD(title):
    
    componentes = {}

    root = ventana()
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
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

    tk.Label(root,text=title,font=('helvetica','18','bold')).grid(column=1,row=0,sticky="N")

    componentes['imagenes']  = [tk.PhotoImage(file="imgs/crear.png"),
                                tk.PhotoImage(file="imgs/editar.png"),
                                tk.PhotoImage(file="imgs/eliminar.png"),
                                tk.PhotoImage(file="imgs/ver.png"),
                                tk.PhotoImage(file="imgs/volver.png"),
                                tk.PhotoImage(file="imgs/salir.png")]

    imagen = componentes['imagenes']

    componentes['botones']  =  [tk.Button(contenedor[0],image=imagen[0],command=lambda:[root.destroy(),formulariosCrear(title)]),
                                tk.Button(contenedor[1],image=imagen[1]),
                                tk.Button(contenedor[2],image=imagen[2],command=lambda:[root.destroy(),formulariosEliminar(title)]),
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
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)

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

    
    componentes['botones'] = [tk.Button(contenedor[0],image=imagen[0],command = lambda:[root.destroy(),menuCRUD("CLIENTES")]),
                              tk.Button(contenedor[1],image=imagen[1],command = lambda:[root.destroy(),menuCRUD("PRODUCTOS")]),
                              tk.Button(contenedor[2],image=imagen[2],command = lambda:[root.destroy(),menuCRUD("PEDIDOS")]),
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

def formulariosCrear(title):
    if(title=='CLIENTES'):
        crearCliente()
    elif(title=='PRODUCTOS'):
        crearProducto()
    elif(title=='PEDIDOS'):
        crearPedido()

def formulariosEliminar(title):
    if(title=='CLIENTES'):
        eliminarCliente()
    elif(title=='PRODUCTOS'):
        eliminarProducto()
    elif(title=='PEDIDOS'):
        eliminarPedido()

#************************************************ FORMULARIOS *****************************************************************************
#--------------------------------------------------- CREAR -------------------------------------------------------------------------------

def crearCliente():
    root = ventana()

    root.columnconfigure(0,weight=3)
    root.columnconfigure(1,weight=1)
    root.columnconfigure(2,weight=1)
    root.columnconfigure(3,weight=1)
    root.columnconfigure(4,weight=3)
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.rowconfigure(2,weight=1)
    root.rowconfigure(3,weight=8)


    header = tk.Label(root,text='CREAR CLIENTE',font=('Glacial indifference','16','bold'))
    header.grid(column=0,row=0,columnspan=5,pady=5)

    componentes = {}

    componentes['labels'] = [tk.Label(root,text="Nombre: ",font=('Glacial indifference','10','bold')),
                             tk.Label(root,text="Ciudad: ",font=('Glacial indifference','10','bold'))]

    label = componentes['labels']

    label[0].grid(column=1,row=1,pady=5)
    label[1].grid(column=1,row=2,pady=5)

    componentes['entries'] = [tk.Entry(root),tk.Entry(root)]

    entry = componentes['entries']

    entry[0].grid(column=2,row=1,sticky="WE",pady=5,columnspan=2)
    entry[1].grid(column=2,row=2,sticky="WE",pady=5,columnspan=2)
    

    componentes['botones'] = [tk.Button(root,text="VOLVER",bg="ORANGE",font=('Glacial indifference','10','bold'),width=15,command = lambda:[root.destroy(),menuCRUD("CLIENTES")]),
                              tk.Button(root,text="GUARDAR",bg="GREEN",width=15,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[crearClienteDao(cliente(entry[0].get(),entry[1].get())),limpiar(entry)]),
                              tk.Button(root,text="SALIR",bg="RED",width=15,font=('Glacial indifference','10','bold'),command = root.destroy)]
    
    botones = componentes['botones']

    botones[0].grid(column=1,row=3,sticky="S",pady=20)
    botones[1].grid(column=2,row=3,sticky="S",pady=20)
    botones[2].grid(column=3,row=3,sticky="S",pady=20)

    root.mainloop()

def crearProducto():
    root = ventana()

    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    root.columnconfigure(2,weight=1)
    root.columnconfigure(3,weight=1)
    root.columnconfigure(4,weight=1)
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.rowconfigure(2,weight=1)
    root.rowconfigure(3,weight=1)
    root.rowconfigure(4,weight=1)
    root.rowconfigure(5,weight=3)


    header = tk.Label(root,text='CREAR PRODUCTO',font=('Glacial indifference','16','bold'))
    header.grid(column=0,row=0,columnspan=5,pady=20)

    componentes = {}

    componentes['labels'] = [tk.Label(root,text="Referencia: ",font=('Glacial indifference','10','bold')),
                             tk.Label(root,text="Tipo: ",font=('Glacial indifference','10','bold')),
                             tk.Label(root,text="Precio: ",font=('Glacial indifference','10','bold')),
                             tk.Label(root,text="Cantidad en \nel inventario: ",font=('Glacial indifference','10','bold'))]

    label = componentes['labels']

    label[0].grid(column=1,row=1,pady=5,sticky="E")
    label[1].grid(column=1,row=2,pady=5,sticky="E")
    label[2].grid(column=1,row=3,pady=5,sticky="E")
    label[3].grid(column=1,row=4,pady=5,sticky="E")

    componentes['entries'] = [tk.Entry(root,width=13,justify='right'),
                              tk.Entry(root,width=13,justify='right'),
                              tk.Entry(root,width=13,justify='right')]

    entry = componentes['entries']

    entry[0].grid(column=2,row=1,pady=5,columnspan=2)
    entry[1].grid(column=2,row=3,pady=5,columnspan=2)
    entry[2].grid(column=2,row=4,pady=5,columnspan=2)

    componentes['comboboxes'] = [ttk.Combobox(root,width=10,values=["CONJUNTO","SHORT"],state="readonly")]
    comboBox = componentes['comboboxes']

    comboBox[0].grid(column=2,row=2,columnspan=2)

    componentes['botones'] = [tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),command = lambda:[root.destroy(),menuCRUD('PRODUCTOS')]),
                              tk.Button(root,text="GUARDAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[crearProductoDao(produto(entry[0].get(),comboBox[0].get(),entry[1].get(),entry[2].get())),limpiar(entry)]),
                              tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),command = root.destroy)]

    boton = componentes['botones']

    boton[0].grid(column=1,row=5,sticky="S",pady=20)
    boton[1].grid(column=2,row=5,sticky="S",pady=20)
    boton[2].grid(column=3,row=5,sticky="S",pady=20)

    root.mainloop()

def crearPedido():
    root = ventana()

    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    root.columnconfigure(2,weight=1)
    root.columnconfigure(3,weight=1)
    root.columnconfigure(4,weight=1)
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.rowconfigure(2,weight=1)
    root.rowconfigure(3,weight=1)
    root.rowconfigure(4,weight=5)

    header = tk.Label(root,text='CREAR PEDIDO',font=('Glacial indifference','16','bold'))
    header.grid(column=0,row=0,columnspan=5,pady=20)

    componentes = {}

    componentes['labels'] = [tk.Label(root,text="Cliente: ",font=('Glacial indifference','10','bold')),
                             tk.Label(root,text="referencia: ",font=('Glacial indifference','10','bold')),
                             tk.Label(root,text="Cantidad: ",font=('Glacial indifference','10','bold'))]
    
    label = componentes['labels']

    label[0].grid(column=1,row=1,pady=5,sticky="E")
    label[1].grid(column=1,row=2,pady=5,sticky="E")
    label[2].grid(column=1,row=3,pady=5,sticky="E")

    componentes['comboBoxes'] = [ttk.Combobox(root,width=10,state="readonly"),
                                 ttk.Combobox(root,width=10,state="readonly")]

    comboBox = componentes['comboBoxes']

    comboBox[0].grid(column=2,row=1,columnspan=2)
    comboBox[1].grid(column=2,row=2,columnspan=2)

    actualizarComboBox(comboBox[0],"nombre","Clientes")
    actualizarComboBox(comboBox[1],"referencia","Productos")

    componentes['entries'] = [tk.Entry(root,justify='right',width=13)]
    entry = componentes['entries']

    entry[0].grid(column=2,row=3,pady=5,columnspan=2)

    componentes['botones'] = [tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),command = lambda:[root.destroy(),menuCRUD('PEDIDOS')]),
                              tk.Button(root,text="GUARDAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[crearPedidoDao(pedido(verDatoDao('id_cliente','Clientes','nombre',comboBox[0].get()),comboBox[1].get(),entry[0].get())),limpiar(entry)]),
                              tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),command = root.destroy)]
    
    boton = componentes['botones']

    boton[0].grid(column=1,row=4,sticky="S",pady=20)
    boton[1].grid(column=2,row=4,sticky="S",pady=20)
    boton[2].grid(column=3,row=4,sticky="S",pady=20)

    root.mainloop()

#-------------------------------------------------- ELIMINAR -------------------------------------------------------------------------------
def eliminarCliente():
    root = ventana()

    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    root.columnconfigure(2,weight=1)
    root.columnconfigure(3,weight=1)
    root.columnconfigure(4,weight=1)
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.rowconfigure(2,weight=8)

    header = tk.Label(root,text='ELIMINAR CLIENTE',font=('Glacial indifference','16','bold'))
    header.grid(column=0,row=0,columnspan=5,pady=20)
    componentes = {}

    componentes['labels'] = [tk.Label(root,text="Cliente: ",font=('Glacial indifference','10','bold'))]

    label = componentes['labels']

    label[0].grid(column=1,row=1,pady=5,sticky="E")

    componentes['comboBoxes'] = [ttk.Combobox(root,width=10,state="readonly")]
    comboBox = componentes['comboBoxes']

    comboBox[0].grid(column=2,row=1,columnspan=2)
    actualizarComboBox(comboBox[0],"nombre","Clientes")
    

    componentes['botones'] = [tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),command = lambda:[root.destroy(),menuCRUD('CLIENTES')]),
                              tk.Button(root,text="ELIMINAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[eliminarClienteDao(comboBox[0].get()),actualizarComboBox(comboBox[0],"nombre","Clientes")]),
                              tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),command = root.destroy)]

    boton = componentes['botones']

    boton[0].grid(column=1,row=4,sticky="S",pady=20)
    boton[1].grid(column=2,row=4,sticky="S",pady=20)
    boton[2].grid(column=3,row=4,sticky="S",pady=20)

    root.mainloop()

def eliminarProducto():
    root = ventana()

    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    root.columnconfigure(2,weight=1)
    root.columnconfigure(3,weight=1)
    root.columnconfigure(4,weight=1)
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.rowconfigure(2,weight=8)

    header = tk.Label(root,text='ELIMINAR PRODUCTOS',font=('Glacial indifference','16','bold'))
    header.grid(column=0,row=0,columnspan=5,pady=20)

    componentes = {}


    componentes['labels'] = [tk.Label(root,text="Producto: ",font=('Glacial indifference','10','bold'))]
    label = componentes['labels']                         

    label[0].grid(column=1,row=1,pady=5,sticky="E")

    componentes['comboBoxes'] = [ttk.Combobox(root,width=10,state="readonly")]
    comboBox = componentes['comboBoxes']
    comboBox[0].grid(column=2,row=1,columnspan=2)

    actualizarComboBox(comboBox[0],"referencia","Productos")

    componentes['botones'] = [tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),command = lambda:[root.destroy(),menuCRUD('PRODUCTOS')]),
                              tk.Button(root,text="ELIMINAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[eliminarProductoDao(comboBox[0].get()),actualizarComboBox(comboBox[0],"referencia","Productos")]),
                              tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),command = root.destroy)]
    
    boton = componentes['botones']

    boton[0].grid(column=1,row=4,sticky="S",pady=20)
    boton[1].grid(column=2,row=4,sticky="S",pady=20)
    boton[2].grid(column=3,row=4,sticky="S",pady=20)



    root.mainloop()

def eliminarPedido():
    root = ventana()

    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    root.columnconfigure(2,weight=1)
    root.columnconfigure(3,weight=1)
    root.columnconfigure(4,weight=1)
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.rowconfigure(2,weight=1)
    root.rowconfigure(3,weight=8)

    header = tk.Label(root,text='ELIMINAR PEDIDO',font=('Glacial indifference','16','bold'))
    header.grid(column=0,row=0,columnspan=5,pady=20)

    componentes = {}
    idpedidos  = []
    referencias = []
    idcliente = []


    pedidos  = verDatosDao('*','Productos')
    for pedido in pedidos:
        idpedidos.append(pedido[0])
        referencias.append(pedido[1])
        idcliente.append(pedido[2])


    componentes['labels'] = [tk.Label(root,text="Pedido: ",font=('Glacial indifference','10','bold'))]
    label = componentes['labels']

    label[0].grid(column=1,row=1,pady=5,sticky="E")
    
    componentes['entries'] = [tk.Entry(root,state='readonly')]

    componentes['comboBoxes'] = [ttk.Combobox(root,width=10,values=idpedidos,state="readonly")]
    comboBox = componentes['comboBoxes']
    comboBox[0].grid(column=2,row=1,columnspan=2)

    actualizarComboBox(comboBox[0],"nombre","Clientes")

    componentes['botones'] = [tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),command = lambda:[root.destroy(),menuCRUD('PEDIDOS')]),
                              tk.Button(root,text="ELIMINAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[root.destroy()]),
                              tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),command = root.destroy)]
    boton = componentes['botones']

    boton[0].grid(column=1,row=3,sticky="S",pady=20)
    boton[1].grid(column=2,row=3,sticky="S",pady=20)
    boton[2].grid(column=3,row=3,sticky="S",pady=20)

    root.mainloop()

#------------------------------------------------ FUNCIONES EXTRA ----------------------------------------------------------------------

def limpiar(entries):
    for entry in entries:
        entry.delete(first=0,last=tk.END)

def actualizarComboBox(comboBox,dato,table):
    datos = verDatosDao(dato,table)
    comboBox.config(values = datos)
    if(len(datos)>0):
        comboBox.current(0)
    else:
        comboBox.set('')
    

if __name__ == "__main__":
    crearCliente()