class registroMateria:
    def __init__(self,p_estudiante,p_apellido,p_carrera):
        self.estudiante=p_estudiante
        self.apellido=p_apellido
        self.carrera=p_carrera
        self.materias=[]

    def presentarse(self):
        print ('***********************PRESENTACION DE {} {}**************'.format(self.estudiante, self.apellido))
        for i in self.materias:
            print(i)
        return 'Soy el est: {} de la carrera de {}'.format(self.estudiante, self.carrera)

    def registrarMateria (self):
        print('gestion de registro de materias')
        materia=input('Digite la materia: ')
        self.materias.append(materia)
        print( 'materia {} registrado exitozamente.!'.format(materia))
        adicional=input('Desea registrar una materia adicional: y/n :: ')
        if (adicional=='y'):
            self.registrarMateria()
        else:
            print( 'Materia registradas exitosamente.!!')

    def menu(self):
        opciones= """
        Menu de la aplicacion
        1.-Registro de Materia
        2.-Presentarse
                          """
        print(opciones)
        eleccion=int(input('elija una opcion:'))
        if (eleccion==1):
            print(self.registrarMateria())
            self.menu()
        elif(eleccion==2):
            print(self.presentarse())
            self.menu()
        else:
            print('elija una opcion del menu')
            self.menu()

pedro=registroMateria('Pedro','Perez','Ing. Sistemas')
pablo=registroMateria('Pablo','Mercado','Ing. Sistemas')

print(pedro.menu())
#print(pedro.registrarMateria())
#print(pablo.presentarse())
#print(pablo.registrarMateria())


