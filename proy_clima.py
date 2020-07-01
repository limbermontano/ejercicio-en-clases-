class  Climas:
    def __init__(self):
        self.codigo = []
        self.ciudad = []
        self.tempMinima = []
        self.tempMaxima = []
        self.zona = []
        self.estado = []
        print('***********CLIMAS DE LOS DEPARTAMENTOS DE BOLIVIA***********')

    def menu(self):
        opciones = """        
        1.-MOSTRAR CLIMAS DE CIUDADES
        2.-PROMEDIO DE LAS TEMPERATURAS MAX.
        3.-MOSTRAR TEMPERATURA MINIMAS
        4.-MOSTRAR TEMPERATURA MAXIMAS
        5.-SALIR

        """
        print(opciones)
        elegir = int(input("Elija una opción del menú: \n "))
        if (elegir == 1):
            print(self.mostrar())
            self.volverMenu()
        elif (elegir == 2):
            print(self.promedio())
            self.volverMenu()
        elif (elegir == 3):
            print(self.promedioMin())
            self.volverMenu()
        elif (elegir == 4):
            print(self.promedioMax())
            self.volverMenu()
        elif (elegir == 5):
            print("GRACIAS POR UTILIZAR EL SISTEMA")

        #print("Elija una opcion del menu!")
        #self.menu()

    def volverMenu(self):
            eleccion = input("Desea volver al menu? y / n: \n ")
            if (eleccion == "y"  or  eleccion == "Y"):
                self.menu()

    def registrador (self):
            codigo = int(input("Agregue un codigo: \n "))
            ciudad = input("Agregar nueva ciudad: \n ")
            minima = int(input("Tempertura minima: \n "))
            maxima = int(input("Temperatura maxima: \n "))
            zona = input("agregue una zona:\n")
            print(self.guardar(codigo, ciudad, minima, maxima, zona))
    def guardar(self,cd,cid,min,max,zn):
            self.codigo.append(cd)
            self.ciudad.append(cid)
            self.tempMinima.append(min)
            self.tempMaxima.append(max)
            self.zona.append(zn)
            self.estado.append(1)
            return "Ciudad {} registrada exitosamente. !!".format(self.ciudad)
    def mostrar(self):
            for i  in range(len(self.ciudad)):
                self.detalle(i)
    def detalle(self, posicion):
            print("Codigo de ciudad {}".format(self.codigo[posicion]))
            print("Nombre de la ciudad: {}".format(self.ciudad[posicion]))
            print("temperatura mínima: {}".format(self.tempMinima[posicion]))
            print("temperatura máxima: {}".format(self.tempMaxima[posicion]))
            print("Zona: {}".format(self.zona[posicion]))
            print("***********************************")
    def promedio(self):
        print("*** PROMEDIO DE TEMPERATURAS ***")
        prom = 0
        for i in range(len(self.zona)):
            print(self.tempMaxima[i], (""), self.zona[i])
            prom = prom + self.tempMaxima[i]
        return '*****EL PROMEDIO MAX ES: {}*****'.format(prom / len(self.zona))

    def promedioMin(self):
            print("*** Temperaturas minimas ***")
            for i in range(len(self.zona)):
                print(self.tempMinima[i], (""), self.zona[i])

            suma = 0
            for i in  range(len(self.zona)):
                suma = self.tempMinima[i]

    def promedioMax(self):
            print("*** Temperaturas maximas ***")
            for  i in range(len(self.zona)):
                print(self.tempMaxima[i], (""), self.zona[i])



climas = Climas()
climas.guardar(1, "SANTA CRUZ", 15, 29, "Llano")
climas.guardar(2, "BENI", 17, 31, "Llano")
climas.guardar(3, "PANDO", 18, 30, "Llano")
climas.guardar(4, "LA PAZ", 1, 13, "Altiplano")
climas.guardar(5, "ORURO", 2, 15, "Altiplano")
climas.guardar(6, "POTOSI", 2, 14, "Altiplano")
climas.guardar(7, "CBBA", 5, 18, "Valle")
climas.guardar(8, "SUCRE", 9, 23, "Valle")
climas.guardar(9, "TARIJA", 10, 25, "Valle")
climas.menu()