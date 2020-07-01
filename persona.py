from datetime import datetime

class Persona(object):
    def __init__(self, p_nombre, p_apellido, p_celular, p_direccion, p_fecha_nac):
        self.nombre = p_nombre
        self.apellido = p_apellido
        self.celular = p_celular
        self.direccion = p_direccion
        self.fecha_nac = p_fecha_nac
        self.estado = 1
    def saludar(self):
        respuesta=''
        if (self.estado==1):
            respuesta= "Hola Soy %s %s vivo en  %s" % (self.nombre,self.apellido, self.direccion)
        return respuesta
   
    def estadoSistema(self):
        if(self.estado==1):
            return"Soy %s, estoy habilitado en el sistema" % (self.nombre)
        else:
            return "Soy %s, no estoy habilidado en el sistema"%(self.nombre)
    def darBaja(self):
        self.estado=0
        return "Ahora %s, esta de baja e el sistema"%(self.nombre)
    def darAlta(self):
        if (self.estado==1):
            return "Advertencia.!, %s ya esta de Alta"%(self.nombre)
        else:
            self.estado=1
            return "Ahora %s esta de alta en el sistema"%(self.nombre)
    def obtenerEdad(self):
        fecha_nacimiento=datetime.strptime(self.fecha_nac,"%d/%m/%Y")
        hoy=datetime.now()
        fecha_edad=hoy - fecha_nacimiento
        edad=int(fecha_edad.days / 365)
        return  '{} tiene {} años'.format(self.nombre,edad)

pedro = Persona("Pedro", "Perez", "76618791",
"zona radial 10", "09/11/1979")
pablo = Persona("Pablo", "Marmol", "78107354",
"zona la guardia", "18/05/2003")    
vilma = Persona("Vilma", "Torrez", "75522341",
"zona barrio olender", "28/04/1985") 
betty = Persona("Betty", "Cardozo", "75544341",
"zona barrio heroes del chaco", "18/06/1987") 

print ('****************************************')
print (pedro.obtenerEdad())
print (pablo.obtenerEdad())
print (vilma.obtenerEdad())
print (betty.obtenerEdad())

print ('****************************************')

# print (pedro.estadoSistema())
# print (pablo.estadoSistema())
# print(pablo.estado)
# print (vilma.estadoSistema())
# print (betty.estadoSistema())

# print(pablo.darBaja())
# print(pablo.estado)
# print(pablo.estadoSistema())

# print (pedro.saludar())
# print (pablo.saludar())
# print (vilma.saludar())
# print (betty.saludar())

# print (pedro.darAlta())
# print (pablo.darAlta())
# print (vilma.darAlta())
# print (betty.darAlta())
# print ('**************NUEVO SALUDO***********')
# print (pedro.saludar())
# print (pablo.saludar())
# print (vilma.saludar())
# print (betty.saludar())
 