from textwrap import fill
from model.db_dao import *
import tkinter as tk
from tkinter import StringVar, ttk
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
  
class menuCRUD:
    def __init__(self,title):
        self.title = title
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

        componentes['botones']  =  [tk.Button(contenedor[0],image=imagen[0],command=lambda:[root.destroy(),formulariosCrear(self.title)]),
                                    tk.Button(contenedor[1],image=imagen[1],command=lambda:[root.destroy(),formulariosModificar(self.title)]),
                                    tk.Button(contenedor[2],image=imagen[2],command=lambda:[root.destroy(),formulariosEliminar(self.title)]),
                                    tk.Button(contenedor[3],image=imagen[3]),
                                    tk.Button(contenedor[4],image=imagen[4],command=lambda:[root.destroy(),menuPrincipal()]),
                                    tk.Button(contenedor[5],image=imagen[5],command=root.destroy)]

        boton = componentes['botones']

        componentes['labels'] =[tk.Label(contenedor[0],text="CREAR "+ self.title),
                                tk.Label(contenedor[1],text="EDITAR "+ self.title),
                                tk.Label(contenedor[2],text="ELIMINAR "+ self.title),
                                tk.Label(contenedor[3],text="VER "+ self.title),
                                tk.Label(contenedor[4],text="VOLVER"),
                                tk.Label(contenedor[5],text="SALIR")]
        
        label = componentes['labels']

        for i in range(len(boton)):
            boton[i].pack()
            label[i].pack()

        root.mainloop()

class menuPrincipal:
    def __init__(self):

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

def formulariosModificar(title):
    if(title=='CLIENTES'):
        modificarClientes()
    elif(title=='PRODUCTOS'):
        pass
    elif(title=='PEDIDOS'):
        pass

#************************************************ FORMULARIOS *****************************************************************************
#---------------------------------------------------- CREAR -------------------------------------------------------------------------------

class crearCliente:
    def __init__(self):
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

class crearProducto:
    def __init__(self):
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

class crearPedido:
    def __init__(self):
        root = ventana()

        componentes = {}

        frame = tk.Frame(root)
        frame.pack(fill='x')
        header = tk.Label(frame,text="ELIMINAR PEDIDO",font=('Glacial indifference','16','bold'))
        header.pack(fill='x')

        nombreCliente = ttk.Combobox(frame,state='readonly')
        actualizarComboBox(nombreCliente,filtrarNombres(verClientesDao()))
        nombreCliente.pack()

        scroll = ttk.Scrollbar(frame)
        scroll.pack(fill='y',side='right')

        tabla = ttk.Treeview(frame,yscrollcommand=scroll.set,selectmode='browse',height=8)
        tabla.pack(fill='x',pady=20)

        scroll.config(command=tabla.yview)

        tabla['columns'] = ('Referencias','Precios','Cantiadad','Total')
        tabla.column("#0", width=0,  stretch='no')
        tabla.column("Referencias",anchor='center', width=80)
        tabla.column("Precios",anchor='center',width=80)
        tabla.column("Cantiadad",anchor='center',width=80)
        tabla.column("Total",anchor='center',width=80)

        tabla.heading("#0",text="")
        tabla.heading("Referencias",text="Referencias",anchor='center')
        tabla.heading("Precios",text="Precios",anchor='center')
        tabla.heading("Cantiadad",text="Cantiadad",anchor='center')
        tabla.heading("Total",text="Total",anchor='center')

        Input_frame = tk.Frame(root)
        Input_frame.pack()

        referencia = tk.Label(Input_frame,text="Referencia")
        referencia.grid(row=0,column=0)

        Cantidad = tk.Label(Input_frame,text="Cantidad")
        Cantidad.grid(row=0,column=2)

        referencia_comboBox = ttk.Combobox(Input_frame,state='readonly')
        referencia_comboBox.grid(row=1,column=0)
        actualizarComboBox(referencia_comboBox,verProductosDao())

        Cantidad_entry = tk.Entry(Input_frame)
        Cantidad_entry.grid(row=1,column=2)

        listaPedido = []

        def agregarProductoTabla():
            precio  = verPrecioProductosDao(referencia_comboBox.get())
            listaPedido.append(produto(referencia_comboBox.get(),'',precio,Cantidad_entry.get()))

            total = int(precio)*int(Cantidad_entry.get())
            tabla.insert(parent='',index='end',iid=len(tabla.get_children()),text='',
                        values=(referencia_comboBox.get(),precio,Cantidad_entry.get(),total)) 
            Cantidad_entry.delete(0,'end')

        def guardaPedido():
            crearPedidoDao(verIdClienteDao(nombreCliente.get()),listaPedido)
            limpiarTabla(tabla)
            listaPedido.clear()
        
        componentes['botones'] = [tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),
                                  command = lambda:[root.destroy(),menuCRUD('PEDIDOS')]),

                                  tk.Button(root,text='AGREGAR',bg='blue',width=10,font=('Glacial indifference','10','bold'),
                                  command=agregarProductoTabla),

                                  tk.Button(root,text="GUARDAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),
                                  fg="white",command = guardaPedido),

                                  tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),
                                  command = root.destroy)]

        boton = componentes['botones']

        for i in range(len(boton)):
            boton[i].pack(side='left',padx=25)

        root.mainloop()

#-------------------------------------------------- ELIMINAR -------------------------------------------------------------------------------
class eliminarCliente:
    def __init__(self):
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
        actualizarComboBox(comboBox[0],filtrarNombres(verClientesDao()))
        

        componentes['botones'] = [tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),command = lambda:[root.destroy(),menuCRUD('CLIENTES')]),
                                tk.Button(root,text="ELIMINAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[eliminarClienteDao(comboBox[0].get()),actualizarComboBox(comboBox[0],filtrarNombres(verClientesDao()))]),
                                tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),command = root.destroy)]

        boton = componentes['botones']

        boton[0].grid(column=1,row=4,sticky="S",pady=20)
        boton[1].grid(column=2,row=4,sticky="S",pady=20)
        boton[2].grid(column=3,row=4,sticky="S",pady=20)

        root.mainloop()

class eliminarProducto:
    def __init__(self):
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

        actualizarComboBox(comboBox[0],verProductosDao())

        componentes['botones'] = [tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),command = lambda:[root.destroy(),menuCRUD('PRODUCTOS')]),
                                tk.Button(root,text="ELIMINAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),fg="white",command = lambda:[eliminarProductoDao(comboBox[0].get()),actualizarComboBox(comboBox[0],verProductosDao())]),
                                tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),command = root.destroy)]
        
        boton = componentes['botones']

        boton[0].grid(column=1,row=4,sticky="S",pady=20)
        boton[1].grid(column=2,row=4,sticky="S",pady=20)
        boton[2].grid(column=3,row=4,sticky="S",pady=20)



        root.mainloop()

class eliminarPedido:
    def __init__(self):
        root = ventana()

        componentes = {}

        frame = tk.Frame(root)
        frame.pack(fill='x')
        header = tk.Label(frame,text="ELIMINAR PEDIDO",font=('Glacial indifference','16','bold'))
        header.pack(fill='x')

        nombreCliente = ttk.Combobox(frame,state='readonly')
        actualizarComboBox(nombreCliente,verNombreCliente_Pedido())   
        nombreCliente.pack()

        scroll = ttk.Scrollbar(frame)
        scroll.pack(fill='y',side='right')

        tabla = ttk.Treeview(frame,yscrollcommand=scroll.set,selectmode='browse')
        tabla.pack(fill='x',pady=20)

        scroll.config(command=tabla.yview)

        tabla['columns'] = ('Referencias','Precios','Cantiadad','Total')
        tabla.column("#0", width=0,  stretch='no')
        tabla.column("Referencias",anchor='center', width=80)
        tabla.column("Precios",anchor='center',width=80)
        tabla.column("Cantiadad",anchor='center',width=80)
        tabla.column("Total",anchor='center',width=80)

        tabla.heading("#0",text="")
        tabla.heading("Referencias",text="Referencias",anchor='center')
        tabla.heading("Precios",text="Precios",anchor='center')
        tabla.heading("Cantiadad",text="Cantiadad",anchor='center')
        tabla.heading("Total",text="Total",anchor='center')

        #a partir del contenido del comboBox muestra los datos
        def hacerTabla(event=None):
            limpiarTabla(tabla)
            if(nombreCliente.get() != ''):
                idCliente = verIdClienteDao(nombreCliente.get())
                pedidos = verPedidosDao(idCliente)
                if(len(pedidos)>0):
                    for i in range(len(pedidos)):
                        referencia = pedidos[i][2]
                        cantidad = pedidos[i][3]
                        precio = verPrecioProductosDao(referencia)
                        total = precio*cantidad
                        tabla.insert(parent='',index='end',iid=i,text='',
                        values=(referencia,precio,cantidad,total)) 

        def eliminarPedidoRegistrado():
            limpiarTabla(tabla)
            eliminarPedidoDao(nombreCliente.get()),actualizarComboBox(nombreCliente,verNombreCliente_Pedido())
            actualizarComboBox(nombreCliente,verNombreCliente_Pedido())
            hacerTabla()

        hacerTabla()
        nombreCliente.bind('<<ComboboxSelected>>',hacerTabla) 

        componentes['botones'] = [tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),
                                  command = lambda:[root.destroy(),menuCRUD('PEDIDOS')]),

                                  tk.Button(root,text="ELIMINAR",bg="GREEN",width=10,font=('Glacial indifference','10','bold'),
                                  fg="white",command = eliminarPedidoRegistrado),

                                  tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),
                                  command = root.destroy)]
        
        boton = componentes['botones']


        boton[0].pack(side='left',padx=50)
        boton[1].pack(side='left',padx=50)
        boton[2].pack(side='left',padx=50)

        root.mainloop()

#-------------------------------------------------- MODIFICAR ---------------------------------------------------------------------------
class modificarClientes:
    def __init__(self):
        root = ventana()

        componentes = {}

        frame = tk.Frame(root)
        frame.pack(fill='x')
        header = tk.Label(frame,text="EDITAR CLIENTES",font=('Glacial indifference','16','bold'))
        header.pack(fill='x')

        scroll = ttk.Scrollbar(frame)
        scroll.pack(fill='y',side='right')

        tabla = ttk.Treeview(frame,yscrollcommand=scroll.set,selectmode='browse')
        tabla.pack(fill='x',pady=20)

        scroll.config(command=tabla.yview)

        tabla['columns'] = ('Nombre','Ciudad')
        tabla.column("#0", width=0,  stretch='no')
        tabla.column("Nombre",anchor='center', width=80)
        tabla.column("Ciudad",anchor='center',width=80)

        tabla.heading("#0",text="")
        tabla.heading("Nombre",text="Nombre",anchor='center')
        tabla.heading("Ciudad",text="Ciudad",anchor='center')

        clientes = verClientesDao()
        for i in range(len(clientes)):
            tabla.insert(parent='',index='end',iid=i,text='',values=(clientes[i][1],clientes[i][2])) 

        Input_frame = tk.Frame(root)
        Input_frame.pack()

        Nombre = tk.Label(Input_frame,text="Nombre")
        Nombre.grid(row=0,column=0)

        Ciudad = tk.Label(Input_frame,text="Ciudad")
        Ciudad.grid(row=0,column=2)

        Nombre_Entry = tk.Entry(Input_frame)
        Nombre_Entry.grid(row=1,column=0)

        Ciudad_entry = tk.Entry(Input_frame)
        Ciudad_entry.grid(row=1,column=2)

        #actualiza los datos de los entries con el registro seleccionado 
        def registroSeleccionado(event):
            boton[1].config(bg='GREEN',state='normal')
            #clear entry boxes
            Nombre_Entry.delete(0,'end')
            Ciudad_entry.delete(0,'end')
            
            #grab record
            seleccionado = tabla.focus()
            #grab record values
            values = tabla.item(seleccionado,'values')
            #temp_label.config(text=selected)

            #output to entry boxes
            Nombre_Entry.insert(0,values[0])
            Ciudad_entry.insert(0,values[1])
        
        def modificarRegistro():
            modificarClienteDao(verIdClienteDao(tabla.item(tabla.focus(),'values')[0]),Nombre_Entry.get(),Ciudad_entry.get())
            #save new data 
            tabla.item(tabla.focus(),text="",values=(Nombre_Entry.get(),Ciudad_entry.get()))
            
             #clear entry boxes
            Nombre_Entry.delete(0,'end')
            Ciudad_entry.delete(0,'end')

            boton[1].config(bg='WHITE',state='disable')

        tabla.bind('<<TreeviewSelect>>',registroSeleccionado)

        componentes['botones'] = [tk.Button(root,text="VOLVER",bg="ORANGE",width=10,font=('Glacial indifference','10','bold'),
                                command = lambda:[root.destroy(),menuCRUD('CLIENTES')]),
                                tk.Button(root,text="EDITAR",state='disable',bg="WHITE",width=10,font=('Glacial indifference','10','bold'),
                                fg="white",command= modificarRegistro),
                                tk.Button(root,text="SALIR",bg="RED",width=10,font=('Glacial indifference','10','bold'),
                                command = root.destroy)]
        
        boton = componentes['botones']


        boton[0].pack(side='left',padx=50)
        boton[1].pack(side='left',padx=50)
        boton[2].pack(side='left',padx=50)

        root.mainloop()

#------------------------------------------------ FUNCIONES EXTRA ----------------------------------------------------------------------

#Limpia el contenido de los entries que se le pasen
def limpiar(entries):
    for entry in entries:
        entry.delete(first=0,last=tk.END)

def limpiarTabla(tabla):
    for child in tabla.get_children():
        tabla.delete(child)

#Recibe el comboBox ha actualizar, el dato que 
#va a mostrar este y la tabla de donde este sale.
def actualizarComboBox(comboBox ,datos):
    comboBox.config(values = datos)
    if(len(datos)>0):
        comboBox.current(0)
    else:
        comboBox.set('')

def filtrarNombres(datos):
    nombres = []
    for dato in datos:
        nombres.append(dato[1])
    return nombres

if __name__ == "__main__":
    menuPrincipal()