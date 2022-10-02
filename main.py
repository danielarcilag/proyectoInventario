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

    lbNombre = tk.Label(root,text="Nombre: ",font=('Glacial indifference','10','bold'))
    lbNombre.grid(column=1,row=1,pady=5)

    txtNombre = tk.Entry(root)
    txtNombre.grid(column=2,row=1,sticky="WE",pady=5,columnspan=2)

    lbCiudad = tk.Label(root,text="Ciudad: ",font=('Glacial indifference','10','bold'))
    lbCiudad.grid(column=1,row=2,pady=5)

    txtCiudad = tk.Entry(root)
    txtCiudad.grid(column=2,row=2,sticky="WE",pady=5,columnspan=2)

    btnVolver = tk.Button(root,text="VOLVER",bg="ORANGE",font=('Glacial indifference','10','bold'),width=15,command = lambda:[root.destroy(),menuCRUD("CLIENTE")])
    btnVolver.grid(column=1,row=3,sticky="S",pady=20)

    btnGurdar = tk.Button(root,text="GUARDAR",bg="GREEN",width=15,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[crearClienteDao(cliente(txtNombre.get(),txtCiudad.get())),root.destroy()])
    btnGurdar.grid(column=2,row=3,sticky="S",pady=20)

    btnGurdar = tk.Button(root,text="SALIR",bg="RED",width=15,font=('Glacial indifference','10','bold'),command = root.destroy)
    btnGurdar.grid(column=3,row=3,sticky="S",pady=20)

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

    lbReferencia = tk.Label(root,text="Referencia: ",font=('Glacial indifference','10','bold'))
    lbReferencia.grid(column=1,row=1,pady=5,sticky="E")

    txtReferencia = tk.Entry(root,width=13,justify='right')
    txtReferencia.grid(column=2,row=1,pady=5,columnspan=2)

    lbTipo = tk.Label(root,text="Tipo: ",font=('Glacial indifference','10','bold'))
    lbTipo.grid(column=1,row=2,pady=5,sticky="E")

    comboBoxTipo = ttk.Combobox(root,width=10,values=["CONJUNTO","SHORT"],state="readonly")
    comboBoxTipo.grid(column=2,row=2,columnspan=2)

    lbPrecio = tk.Label(root,text="Precio: ",font=('Glacial indifference','10','bold'))
    lbPrecio.grid(column=1,row=3,pady=5,sticky="E")

    txtPrecio = tk.Entry(root,width=13,justify='right')
    txtPrecio.grid(column=2,row=3,pady=5,columnspan=2)
    
    lbCantInventario = tk.Label(root,text="Cantidad en \nel inventario: ",font=('Glacial indifference','10','bold'))
    lbCantInventario.grid(column=1,row=4,pady=5,sticky="E")

    txtCantInventario = tk.Entry(root,width=13,justify='right')
    txtCantInventario.grid(column=2,row=4,pady=5,columnspan=2)

    btnVolver = tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),command = lambda:[root.destroy(),menuCRUD('PRODUCTOS')])
    btnVolver.grid(column=1,row=5,sticky="S",pady=20)

    btnGurdar = tk.Button(root,text="GUARDAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[crearProductoDao(produto(txtReferencia.get(),comboBoxTipo.get(),txtPrecio.get(),txtCantInventario.get())),root.destroy()])
    btnGurdar.grid(column=2,row=5,sticky="S",pady=20)

    btnGurdar = tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),command = root.destroy)
    btnGurdar.grid(column=3,row=5,sticky="S",pady=20)

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

    nombreCliente = []
    
    clientes  = verClientesDao()
    for cliente in clientes:
        nombreCliente.append(cliente[1])

    lbCliente = tk.Label(root,text="Cliente: ",font=('Glacial indifference','10','bold'))
    lbCliente.grid(column=1,row=1,pady=5,sticky="E")

    comboBoxCliente = ttk.Combobox(root,width=10,values=nombreCliente,state="readonly")
    comboBoxCliente.grid(column=2,row=1,columnspan=2)

    referenciasProductos = []

    productos  = verProductosDao()

    for producto in productos:
        referenciasProductos.append(producto[0])

    lbProducto = tk.Label(root,text="referencia: ",font=('Glacial indifference','10','bold'))
    lbProducto.grid(column=1,row=2,pady=5,sticky="E")

    comboBoxProducto = ttk.Combobox(root,width=10,values=referenciasProductos,state="readonly")
    comboBoxProducto.grid(column=2,row=2,columnspan=2)

    lbCantidad = tk.Label(root,text="Cantidad: ",font=('Glacial indifference','10','bold'))
    lbCantidad.grid(column=1,row=3,pady=5,sticky="E")

    txtCantidad = tk.Entry(root,justify='right',width=13)
    txtCantidad.grid(column=2,row=3,pady=5,columnspan=2)

    btnVolver = tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),command = lambda:[root.destroy(),menuCRUD('PEDIDOS')])
    btnVolver.grid(column=1,row=4,sticky="S",pady=20)

    btnGurdar = tk.Button(root,text="GUARDAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[crearPedidoDao(pedido(verClienteDao(comboBoxCliente.get()),comboBoxProducto.get(),txtCantidad.get())),root.destroy()])
    btnGurdar.grid(column=2,row=4,sticky="S",pady=20)

    btnGurdar = tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),command = root.destroy)
    btnGurdar.grid(column=3,row=4,sticky="S",pady=20)


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

    nombreCliente = []

    clientes  = verClientesDao()
    for cliente in clientes:
        nombreCliente.append(cliente[1])

    lbCliente = tk.Label(root,text="Cliente: ",font=('Glacial indifference','10','bold'))
    lbCliente.grid(column=1,row=1,pady=5,sticky="E")

    comboBoxCliente = ttk.Combobox(root,width=10,values=nombreCliente,state="readonly")
    comboBoxCliente.grid(column=2,row=1,columnspan=2)

    btnVolver = tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),command = lambda:[root.destroy(),menuCRUD('CLIENTES')])
    btnVolver.grid(column=1,row=4,sticky="S",pady=20)

    btnGurdar = tk.Button(root,text="ELIMINAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[eliminarClienteDao(comboBoxCliente.get()),root.destroy()])
    btnGurdar.grid(column=2,row=4,sticky="S",pady=20)

    btnGurdar = tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),command = root.destroy)
    btnGurdar.grid(column=3,row=4,sticky="S",pady=20)

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

    referenciaProductos = []

    productos  = verProductosDao()
    for producto in productos:
        referenciaProductos.append(producto[0])

    lbCliente = tk.Label(root,text="Producto: ",font=('Glacial indifference','10','bold'))
    lbCliente.grid(column=1,row=1,pady=5,sticky="E")

    comboBoxProducto = ttk.Combobox(root,width=10,values=referenciaProductos,state="readonly")
    comboBoxProducto.grid(column=2,row=1,columnspan=2)

    btnVolver = tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),command = lambda:[root.destroy(),menuCRUD('PRODUCTOS')])
    btnVolver.grid(column=1,row=4,sticky="S",pady=20)

    btnGurdar = tk.Button(root,text="ELIMINAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[eliminarProductoDao(comboBoxProducto.get()),root.destroy()])
    btnGurdar.grid(column=2,row=4,sticky="S",pady=20)

    btnGurdar = tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),command = root.destroy)
    btnGurdar.grid(column=3,row=4,sticky="S",pady=20)

    root.mainloop()


if __name__ == "__main__":
    eliminarProducto()