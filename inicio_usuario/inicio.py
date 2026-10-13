import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Inicio:
    def __init__(self, idusuario):
            self.idusuario = idusuario
    
    
    def identificarUsuario(idusuario):
        sql = "SELECT * FROM usuarios WHERE idusuario = %s"
        cursor.execute(sql, (idusuario,))
        return cursor.fetchone()


    def obtenerEjerciciosPorUsuario(idusuario):
            sql = """
                SELECT 
                    r.nombrerutina,
                    e.nombreejercicio, 
                    e.series, 
                    e.repeticiones 
                FROM rutinas_usuarios ru
                INNER JOIN rutinas r ON ru.idrutina = r.idrutina
                LEFT JOIN rutina_ejercicios re ON r.idrutina = re.idrutinas
                LEFT JOIN ejercicios e ON re.idejercicio = e.idejercicio
                WHERE ru.idusuario = %s
            """
            cursor.execute(sql, (idusuario,))
            return cursor.fetchall()

    def listarProgresoDeAprendiz():
        sql = """
            SELECT u.nombreusuario, u.apellidosusuario, 
                        sp.seguimiento, sp.peso, sp.altura, sp.grasa_corporal
                        FROM seguimiento_progreso sp
                        INNER JOIN usuarios u ON u.idusuario = sp.idusuario
        """
        cursor.execute(sql)
        return cursor.fetchall()