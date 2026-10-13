
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre=None, apellidos=None, telefono=None, email=None, idtipodedocumento=None, numerodedocumento=None, fechanacimiento=None, idtipodeusuario=None, password=None, peso=None, altura=None, grasacorporal=None, numerocontrato=None, fechainiciocontrato=None, fechafincontrato=None, idcontrato= None, dependencia=None, numeroficha=None, iddependencia=None, usuario_id=None, ficha_id=None, idcentrodeformacion=None, centrodeformacion=None, especialidad=None, descripcionespecialidad=None, id_especialidad=None):  
        self.usuario_id = usuario_id
        self.ficha_id = ficha_id
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email
        self.idtipodedocumento = idtipodedocumento
        self.numerodedocumento = numerodedocumento
        self.fechadenacimiento = fechanacimiento
        self.peso = peso
        self.altura = altura
        self.grasacorporal = grasacorporal
        self.idtipodeusuario = idtipodeusuario
        self.password = password
        self.numeroficha = numeroficha
        self.iddependencia = iddependencia
        self.idcentrodeformacion = idcentrodeformacion 
        self.centrodeformacion = centrodeformacion
        self.dependencia = dependencia
        self.idcontrato = idcontrato
        self.numerocontrato = numerocontrato
        self.fechainiciocontrato = fechainiciocontrato
        self.fechafincontrato = fechafincontrato
        self.especialidad = especialidad
        self.descripcionespecialidad = descripcionespecialidad
        self.id_especialidad = id_especialidad

   
    def Identificarficha(numeroficha):

        sql = "SELECT * FROM fichas WHERE numeroFicha = %s AND estadoFicha = 'ACTIVA'"

        fichas = (numeroficha)

        cursor.execute(sql, (fichas,))
        result = cursor.fetchone()              
        database.commit()
        return result 




    def registrar(self):

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))         #Convertir password a bites       
        
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"               #Con %s se remplazan los datos que estan en la tupla
        usuario = (self.nombre, self.apellidos, self.telefono, self.email, self.idtipodedocumento, self.numerodedocumento, self.fechadenacimiento, self.peso, self.altura, self.grasacorporal, cifrado.hexdigest(), self.idtipodeusuario) 


        
       

        try:  
            cursor.execute(sql, usuario)

            usuario_id = cursor.lastrowid

            

            self.usuario_id = usuario_id
            
            if self.idtipodeusuario == 1 and self.numeroficha:
                sql = "INSERT INTO aprendices (idusuario, idficha) VALUES (%s, %s)"
                fichas = (usuario_id, self.ficha_id)
                cursor.execute(sql, fichas)

            elif self.idtipodeusuario == 2:
                sql = "INSERT INTO funcionarios (idusuario, iddependencia, idcentrodeformacion, idtipocontrato) VALUES (%s, %s, %s, %s)"
                fichas = (usuario_id, self.iddependencia, self.idcentrodeformacion, self.idcontrato)
                cursor.execute(sql, fichas)

            if self.idcontrato == 1:
                sql = "INSERT INTO contratos (numerocontrato, fechainiciocontrato, fechafincontrato, idusuario) VALUES (%s, %s, %s, %s)"
                fichas = (self.numerocontrato, self.fechainiciocontrato, self.fechafincontrato, usuario_id)
                cursor.execute(sql, fichas)


            if self.idtipodeusuario == 3:
                sql = "INSERT INTO especialidades (nombre_especialidad, descripcion_especialidad) VALUES (%s, %s)"
                especialidad = (self.especialidad, self.descripcionespecialidad)
                cursor.execute(sql, especialidad)

            id_especialidad = cursor.lastrowid

            if self.idtipodeusuario == 3:
                sql = "INSERT INTO entrenadores (idespecialidad, idusuario) VALUES (%s, %s)"
                entrenadores = (id_especialidad, usuario_id)
                cursor.execute(sql, entrenadores)
            database.commit()
            result = [cursor.rowcount, self]
        except Exception as error:
            database.rollback()
            print(f"\nError al registrar en la BD: {error}")
            result = [0, self]

        return result


    def IdentificarCentro(centrodeformacion):
        
        sql = "SELECT * FROM centros_de_formacion WHERE nombrecentrodeformacion	 = %s"

        centros = (centrodeformacion)

        cursor.execute(sql, (centros,))
        result = cursor.fetchone()              
        database.commit()
        return result


    def IdentificarDependencia(dependencia):
            
        sql = "SELECT * FROM dependencias WHERE nombredependencia = %s"

        dep = (dependencia)

        cursor.execute(sql, (dep,))
        result = cursor.fetchone()              
        database.commit()
        return result


    
   
    def pedir_email_valido(mensaje):
        email = input(mensaje)
        while "@sena.edu.co" not in email:
            print(" Error: El correo debe ser institucional ('@sena.edu.co'). Inténtalo de nuevo.")
            email = input(mensaje)
        return email


    def identificarUsuario(self):
        #Consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE correoinstitucionalusuario = %s AND password = %s"

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) 

        #Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()              #Mostrar solo un registro

        return result 