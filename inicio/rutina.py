import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Rutina:

    def __init__(self, idrutina=None, nombrerutina=None, identrenador=None, idnivel=None, seguimiento=None, peso=None, altura=None, grasa_corporal=None, idusuario=None):
        self.idrutina = idrutina
        self.nombrerutina = nombrerutina
        self.identrenador = identrenador
        self.idnivel = idnivel
        self.seguimiento = seguimiento
        self.peso = peso
        self.altura = altura
        self.grasa_corporal = grasa_corporal
        self.idusuario = idusuario


    def identificarEntrenador(idusuario):
        sql = "SELECT * FROM entrenadores WHERE idusuario = %s"
        cursor.execute(sql, (idusuario,))
        return cursor.fetchone()

    def listarNiveles():
        sql = "SELECT idnivel, nombrenivel FROM niveles LIMIT 3 OFFSET 3"
        cursor.execute(sql)
        return cursor.fetchall()

    def listarMusculos():
        cursor.execute("SELECT idmusculo, nombremusculo FROM musculos")
        return cursor.fetchall()

    def listarPartesDelCuerpo():
        cursor.execute("SELECT idpartedelcuerpo, nombrepartedelcuerpo FROM partes_del_cuerpo")
        return cursor.fetchall()

    def listarMaquinas():
        cursor.execute("SELECT idmaquina, nombremaquina FROM maquinas")
        return cursor.fetchall()

    def listarEstados():
        cursor.execute("SELECT idestado, nombreestado FROM estados")
        return cursor.fetchall()

    def listarEjercicios():
        cursor.execute("SELECT idejercicio, nombreejercicio, series, repeticiones FROM ejercicios")
        return cursor.fetchall()

    def buscarUsuarioPorEmail(email):
        sql = ("SELECT * FROM usuarios WHERE correoinstitucionalusuario = %s")
        correo = (email)
        cursor.execute(sql, (correo,))
        return cursor.fetchone()

    def listarRutinasDeEntrenador():
        sql = "SELECT idrutina, nombrerutina, idnivel FROM rutinas"
        cursor.execute(sql)
        return cursor.fetchall()

    def listarEjerciciosDeRutina(idrutina):
        sql = ("SELECT e.idejercicio, e.nombreejercicio, e.series, e.repeticiones "
               "FROM rutina_ejercicios re "
               "INNER JOIN ejercicios e ON e.idejercicio = re.idejercicio "
               "WHERE re.idrutinas = %s")
        cursor.execute(sql, (idrutina,))
        return cursor.fetchall()

    def crearPartedelCuerpo(nombre):
        sql = "INSERT INTO partes_del_cuerpo (idpartedelcuerpo, nombrepartedelcuerpo) VALUES (null, %s)"
        try:
            cursor.execute(sql, (nombre,))
            database.commit()
            return cursor.lastrowid
        except Exception as error:
            database.rollback()
            print(f"\nError al crear la parte del cuerpo: {error}")
            return None

    def crearMusculo(nombre, idpartedelcuerpo):
        sql = "INSERT INTO musculos (idmusculo, nombremusculo, idpartedelcuerpo) VALUES (null, %s, %s)"
        try:
            cursor.execute(sql, (nombre, idpartedelcuerpo))
            database.commit()
            return cursor.lastrowid
        except Exception as error:
            database.rollback()
            print(f"\nError al crear el musculo: {error}")
            return None


    def crearMaquina(nombre, idestado):
        sql = "INSERT INTO maquinas (idmaquina, nombremaquina, idestado) VALUES (null, %s, %s)"
        try:
            cursor.execute(sql, (nombre, idestado))
            database.commit()
            return cursor.lastrowid
        except Exception as error:
            database.rollback()
            print(f"\nError al crear la maquina: {error}")
            return None

    def crearEjercicio(nombre, descripcion, url, idmusculo, idmaquina, series, repeticiones):
        sql = """INSERT INTO ejercicios
                 (idejercicio, nombreejercicio, descripcionejercicio, urlejercicio,
                  idmusculo, idmaquina, series, repeticiones)
                 VALUES (null, %s, %s, %s, %s, %s, %s, %s)"""
        datos = (nombre, descripcion, url, idmusculo, idmaquina, series, repeticiones)
        try:
            cursor.execute(sql, datos)
            database.commit()
            return cursor.lastrowid
        except Exception as error:
            database.rollback()
            print(f"\nError al crear el ejercicio: {error}")
            return None

    def crearRutina(self):
        sql = "INSERT INTO rutinas (idrutina, nombrerutina, identrenador, idnivel) VALUES (null, %s, %s, %s)"
        datos = (self.nombrerutina, self.identrenador, self.idnivel)
        try:
            cursor.execute(sql, datos)
            database.commit()
            self.idrutina = cursor.lastrowid
            return self.idrutina
        except Exception as error:
            database.rollback()
            print(f"\nError al crear la rutina: {error}")
            return None

    def agregarEjercicioARutina(idrutina, idejercicio):
        sql = "INSERT INTO rutina_ejercicios (id_rutinas_ejercicios, idrutinas, idejercicio) VALUES (null, %s, %s)"
        try:
            cursor.execute(sql, (idrutina, idejercicio))
            database.commit()
            return True
        except Exception as error:
            database.rollback()
            print(f"\nError al agregar el ejercicio a la rutina: {error}")
            return False

    def asignarRutina(idusuario, idrutina, fecha, hora, observaciones, idestado):
        sql = """INSERT INTO rutinas_usuarios
                 (idrutinasusuarios, idusuario, idrutina, fecharutinausuario,
                  horarutinausuario, observacionesusuario, idestado)
                 VALUES (null, %s, %s, %s, %s, %s, %s)"""
        datos = (idusuario, idrutina, fecha, hora, observaciones, idestado)
        try:
            cursor.execute(sql, datos)
            database.commit()
            return cursor.lastrowid
        except Exception as error:
            database.rollback()
            print(f"\nError al asignar la rutina: {error}")
            return None


    def crearProgreso(self):
        sql = "INSERT INTO seguimiento_progreso (seguimiento, peso, altura, grasa_corporal, idusuario, identrenador) VALUES (%s, %s, %s, %s, %s, %s)"
        progreso = (self.seguimiento, self.peso, self.altura, self.grasa_corporal, self.idusuario, self.identrenador)
        try:
            cursor.execute(sql, progreso)
            database.commit()
            return cursor.lastrowid
        except Exception as error:
            database.rollback()
            print(f"\nError al crear la maquina: {error}")
            return None


    def listarProgresoDeAprendiz():
        sql = """
            SELECT u.nombreusuario, u.apellidosusuario, correoinstitucionalusuario,
                        sp.seguimiento, sp.peso, sp.altura, sp.grasa_corporal
                        FROM seguimiento_progreso sp
                        INNER JOIN usuarios u ON u.idusuario = sp.idusuario
        """
        cursor.execute(sql)
        return cursor.fetchall()