class Producto:
    def __init__(self):
        self.codigo=[]
        self.nombre=[]
        self.precio_compra=[]
        self.precio_venta=[]
        self.fecha_fabricacion=[]
        self.fecha_vencimiento=[]
        self.proveedor=[]
        self.estado=[]
    def saludos(self):
        saludos="Gracias por utilizar el sistema, datos registrados correctamente "
        print(saludos.upper())

    def menu(self):
        opcion = """
          1.-AGREGAR PRODUCTO
          2.-MOSTRAR DESCRIPCION
          3.-ACTUALIZAR PRECION DE VENTA
          4.-TIEMPO DE VIGENCIA DE PRODUCTO
          5.-TIEMPO DE VALIDEZ DE PRODUCTO
          6.-ELIMINAR PRODUCTO
          7.-DAR DE ALTA PRODUCTO
          8.-DAR DE BAJA PRODUCTO
          9.-MOSTRAR INVENTARIO DE BAJA
          10.-SALIR
          """
        print(opcion)
        selecciona = int(input('Seleccione una opcion: \n'))
        if (selecciona == 1):
            print(self.agregarP())
            self.menu()
        elif (selecciona == 2):
            print(self.verinventAlta())
            self.menu()
        elif (selecciona == 3):
            print(self.editarPrecioventa())
            self.menu()
        elif (selecciona == 4):
            self.menu()
        elif (selecciona == 5):
            self.menu()
        elif (selecciona == 6):
            self.realizarEliminacion()
            self.menu()
        elif (selecciona==7):
            print(self.realizarAlta())
            self.menu()
        elif (selecciona == 7):
            print(self.realizarBaja())
        elif (selecciona == 8):
            print(self.verinventBaja())
            self.menu()
        elif (selecciona == 9):
            self.saludos()

        else:
            print('Seleccione una opcion del menu')
            self.menu()
    def realizarAlta(self):
        print('******DAR DE ALTA UN PRODUCTO*****')
        posicion=self.buscarProducto(0)
        return self.darAlta(posicion)
    def darAlta(self,posicion):
        self.estado[posicion]=1
        return 'El producto {} esta de alta'.format(self.nombre[posicion])

    def realizarBaja(self):
        print('******DAR BAJA A UN PRODUCTO******')
        posicion = self.buscarProducto(1)
        return self.darBaja(p0.osicion)

    def darBaja(self, posicion):
        self.estado[posicion] = 0
        return 'El producto {} esta de baja'.format(self.nombre[posicion])

    def agregarP(self):
        codigo=input('Ingrese codigo de producto: \n')
        nombre=input('Nombre del Producto: \n')
        precio_compra=int(input('Precio de compra: \n'))
        fecha_fabricacion=input('Feha de Fabricacion : \n')
        fecha_vencimiento=input('Fecha de Vencimiento: \n')
        proveedor=input('Proveedor: \n')
        print(self.guardarP(codigo,nombre,precio_compra,fecha_fabricacion,fecha_vencimiento,proveedor))
        agregarOtro=input('Desea agregar otro Producto: y/n \n')
        if (agregarOtro== 'y'and agregarOtro=='Y'):
            self.agregarP()
        return 'Se Registro correctamente el Producto'

    def guardarP(self,codigo,nombre,precioCompra,fechaFabricacion,fechaVencimiento,proveedor):
        self.codigo.append(codigo)
        self.nombre.append(nombre)
        self.precio_compra.append(precioCompra)
        self.precio_venta.append((precioCompra * 0.4)+precioCompra)
        self.fecha_fabricacion.append(fechaFabricacion)
        self.fecha_vencimiento.append(fechaVencimiento)
        self.proveedor.append(proveedor)
        self.estado.append(1)
        return 'Producto {} agregado correctamente'.format(nombre)

    def verinventAlta(self):
        print(self.inventario())
    def verinventBaja(self):
        pass
    def inventario(self,estado):
        if  (self.nombre):
            for i in range(len(self.nombre)):
               self.descripcion(i)
            return 'Inventario cargado correctamente'
        else:
            return 'Todavia no se agregaron productos'

    def descripcion(self,posicion):
        if (self.estado[posicion]==1):
                print("********* DESCRIPCION DEL PRODUCTO {} ********".format(self.nombre[posicion]))
                print('CODIGO DE PRODUCTO: {}'.format(self.codigo[posicion]))
                print('PRECIO DE COMPRA:{} Bs. '.format(self.precio_compra[posicion]))
                print('PRECIO DE VENTA:{} Bs.'.format(self.precio_venta[posicion]))
                print('FECHA DE FABRICACION:{} '.format(self.fecha_fabricacion[posicion]))
                print('FECHA DE VENCIMIENTO:{} '.format(self.fecha_vencimiento[posicion]))
                print('PROVEEDOR:{} '.format(self.proveedor[posicion]))
                print('Estado:{}'.format(self.estado[posicion]))
                print("**************************")
        else:
            return 'EL DATO RECIBIDO ESTA VACIO'
    def editarPrecioventa(self):
        print(self.inventario())
        digito = int(input('Digite el numero del elemento a modificar: \n'))
        posicion = digito - 1
        self.descripcion(posicion)
        nuevo_precio=int(input('DIGITE EL NUEVO PRECIO DE VENTA DEL PRODUCTO {}'.format(self.nombre[posicion])))
        print(self.modificarPv(posicion,nuevo_precio))
        self.descripcion(posicion)
        return 'Modificacion de precio de venta completado'
    def modifcarPv(self,posicion,pvn):
        self.precio_venta[posicion]=pvn
        return 'Precio de venta del producto{} modificado correctamente'.format(self.nombre[posicion])
    def eliminar(self, posicion):
        cod=self.codigo.pop[posicion]
        self.codigo.pop(posicion)
        self.nombre.pop(posicion)
        self.precio_compra.pop(posicion)
        self.precio_venta.pop(posicion)
        self.fecha_fabricacion.pop(posicion)
        self.fecha_vencimiento.pop(posicion)
        self.proveedor.pop(posicion)
        self.estado.pop(posicion)
        return 'Eliminacion realizada del producto {} '.format(cod)

    def realizarEliminacion(self):
        print('********* SELECCIONAR EL PRODICTO A ELIMINAR*********')
        posicion=self.buscarProducto()
        return self.eliminar(posicion)
    def buscarProducto(self):
        print(self.inventario(1))
        seleccion=input('Registre el codigo del producto:\n')
        posicion=self.codigo.index(seleccion)
        return posicion



producto=Producto()
producto.guardarP('A101','CAFE NEGRO',8,'05-02-2020','05-02-2021','PIL')
producto.guardarP('A102','LECHE PIL',7,'05-02-2020','05-02-2021','PIL')
producto.guardarP('A103','CAFE COROICO',15,'05-02-2020','05-02-2021','PIL')
producto.menu()






