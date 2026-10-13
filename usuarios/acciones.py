import usuarios.usuario as aprendiz
import inicio.acciones
import inicio.rutina
import inicio_usuario.inicio
import inicio_usuario.acciones

class Acciones:

    def registro(self):
        print("\nBienvenido al registro de AGROFIT")

        print("""
            1 - Aprendiz
            2 - Funcionario
            3 - Entrenador
                    """)
        idtipodeusuario = int(input("¿Que tipo de usuario eres? (Ingrese el numero): "))

        if idtipodeusuario == 1:

            nombre = input("¿Cual es tu nombre?: ")
            apellidos = input("¿Cuales son tus apellidos?: ")
            telefono = input("¿Cual es tu telefono?: ")
            email = aprendiz.Usuario.pedir_email_valido("Digita tu correo institucional: ")

            numeroficha = input("Digite su numero de ficha: ")

            fichas = aprendiz.Usuario.Identificarficha(numeroficha)

            if not fichas:
                print("\nLa ficha ingresada no existe en el sistema o no esta activa.")
                return

            print("""
            1 - Cedula de Ciudadania
            2 - Cedula de Extranjeria
            3 - Tarjeta de Identidad
            """)

            idtipodedocumento = int(input("¿Cual es tu tipo de documento: ? (Ingrese el numero): "))
            numerodedocumento = input("¿Digite su numero de documento: ")
            fechanacimiento = (input("Ingrese su fecha de nacimiento: "))
            peso = float(input("Ingrese su peso en Kg: "))
            altura = float(input("Ingrese su altura en metros: "))
            grasacorporal = float(input("Ingrese su grasa corporal: "))
            password = input("Digita tu contraseña: ")


            usuario = aprendiz.Usuario(
            nombre=nombre,
            apellidos=apellidos,
            telefono=telefono,
            email=email,
            idtipodedocumento=idtipodedocumento,
            numerodedocumento=numerodedocumento,
            fechanacimiento=fechanacimiento,
            peso=peso,
            altura=altura,
            grasacorporal=grasacorporal,
            idtipodeusuario=idtipodeusuario,
            password=password,
            numeroficha=numeroficha,
            ficha_id=fichas[0]
            )
            registro = usuario.registrar()
            if registro[0] >= 1:
                print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
            else:
                print("\nNo te has registrado correctamente!!")


    
        elif idtipodeusuario == 2:

            print("""
            1 - Contrato
            2 - planta
            """)

            idcontrato = int(input("¿que tipo de contrato tienes? (ingrese el numero): "))

            if idcontrato == 1:
                numerocontrato = input("Numero de Contrato: ")
                fechainiciocontrato = input("Fecha inicio de contrato: ")
                fechafincontrato = input("Fecha fin de contrato: ")



            dependencia = input("Ingrese su dependencia: ")

            dependencias = aprendiz.Usuario.IdentificarDependencia(dependencia)

            if not dependencias:
                print("\nLa dependencia ingresada no existe en el sistema.")
                return

            centrodeformacion = input("Ingrese su centro de formacion:")

            centros = aprendiz.Usuario.IdentificarCentro(centrodeformacion)

            if not centros:
                print("\nEl centro de formacion ingresado no existe en el sistema.")
                return

            nombre = input("¿Cual es tu nombre?: ")
            apellidos = input("¿Cuales son tus apellidos?: ")
            telefono = input("¿Cual es tu telefono?: ")
            email = input("Digita tu correo institucional o electronico: ")
            

            print("""
            1 - Cedula de Ciudadania
            2 - Cedula de Extranjeria
            3 - Tarjeta de Identidad
            """)

            idtipodedocumento = int(input("¿Cual es tu tipo de documento: ? (Ingrese el numero): "))
            numerodedocumento = input("¿Digite su numero de documento: ")
            fechanacimiento = (input("Ingrese su fecha de nacimiento: "))
            peso = float(input("Ingrese su peso en Kg: "))
            altura = float(input("Ingrese su altura en metros: "))
            grasacorporal = float(input("Ingrese su grasa corporal: "))
            password = input("Digita tu contraseña: ")

            usuario = aprendiz.Usuario(
            nombre=nombre,
            apellidos=apellidos,
            telefono=telefono,
            email=email,
            idtipodedocumento=idtipodedocumento,
            numerodedocumento=numerodedocumento,
            fechanacimiento=fechanacimiento,
            peso=peso,
            altura=altura,
            grasacorporal=grasacorporal,
            idtipodeusuario=idtipodeusuario,
            password=password,
            idcontrato=idcontrato,  # Pasa explícitamente el tipo de contrato seleccionante (1 o 2)
            numerocontrato=numerocontrato if idcontrato == 1 else None,
            fechainiciocontrato=fechainiciocontrato if idcontrato == 1 else None,
            fechafincontrato=fechafincontrato if idcontrato == 1 else None,
            idcentrodeformacion=centros[0],
            iddependencia=dependencias[0]
)
            registro = usuario.registrar()
            if registro[0] >= 1:
                print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")                                                                                    
            else:
                print("\nNo te has registrado correctamente!!")




        elif idtipodeusuario == 3:
        
            print("""
            1 - Contrato
            2 - planta
            """)

            idcontrato = int(input("¿que tipo de contrato tienes? (ingrese el numero): "))

            if idcontrato == 1:
                numerocontrato = input("Numero de Contrato: ")
                fechainiciocontrato = input("Fecha inicio de contrato: ")
                fechafincontrato = input("Fecha fin de contrato: ")



            dependencia = input("Ingrese su dependencia: ")

            dependencias = aprendiz.Usuario.IdentificarDependencia(dependencia)

            if not dependencias:
                print("\nLa dependencia ingresada no existe en el sistema.")
                return

            centrodeformacion = input("Ingrese su centro de formacion:")

            centros = aprendiz.Usuario.IdentificarCentro(centrodeformacion)

            if not centros:
                print("\nEl centro de formacion ingresado no existe en el sistema.")
                return

            especialidad = input("Ingrese su especialidad")
            descripcionespecialidad = input("Ingrese la descripcion de su especialidad")
            nombre = input("¿Cual es tu nombre?: ")
            apellidos = input("¿Cuales son tus apellidos?: ")
            telefono = input("¿Cual es tu telefono?: ")
            email = input("Digita tu correo institucional o electronico: ")
            

            print("""
            1 - Cedula de Ciudadania
            2 - Cedula de Extranjeria
            3 - Tarjeta de Identidad
            """)

            idtipodedocumento = int(input("¿Cual es tu tipo de documento: ? (Ingrese el numero): "))
            numerodedocumento = input("¿Digite su numero de documento: ")
            fechanacimiento = (input("Ingrese su fecha de nacimiento: "))
            password = input("Digita tu contraseña: ")
            peso=peso = None,
            altura=altura = None,
            grasacorporal=grasacorporal = None,

            usuario = aprendiz.Usuario(
            nombre=nombre,
            apellidos=apellidos,
            telefono=telefono,
            email=email,
            idtipodedocumento=idtipodedocumento,
            numerodedocumento=numerodedocumento,
            fechanacimiento=fechanacimiento,
            peso=None,
            altura=None,
            grasacorporal=None,
            idtipodeusuario=idtipodeusuario,
            password=password,
            especialidad=especialidad,
            descripcionespecialidad=descripcionespecialidad
            )

            registro = usuario.registrar()
            if registro[0] >= 1:
                print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")                                                                                    
            else:
                print("\nNo te has registrado correctamente!!")



    def login(self):
        print("\nBienvenido a AGROFIT")

        email = input("Digita tu correo institucional o electronico: ")
        password = input("Digita tu contraseña: ")

        usuario = aprendiz.Usuario(email=email, password=password)
        inicio = usuario.identificarUsuario()

        if inicio:
            # inicio[1] = Nombre, inicio[0] = idusuario, inicio[12] = idtipodeusuario
            print(f"\nBienvenid@ {inicio[1]}, has ingresado correctamente al sistema.")

            idtipodeusuario = int(inicio[12])

            if idtipodeusuario == 3:
                self.acciones(inicio[0])

            elif idtipodeusuario in (1, 2):
                self.accionesUsuario(inicio[0])

            return inicio

           
    
        else:
            print("\nEmail o contraseña incorrectos.")


    def acciones(self, idusuario):
        entrenador = inicio.rutina.Rutina.identificarEntrenador(idusuario)
            
        if not entrenador:
            print("\nTu usuario no esta registrado como entrenador.")
            return

        identrenador = entrenador[0]

        while True:
            print("""
            --- Panel del Entrenador ---
            1 - Crear rutina con ejercicios
            2 - Asignar una rutina a un usuario
            3 - Ver mis rutinas
            4 - Ver progreso de usuarios
            5 - Asignar progreso
            6 - Salir
            """)
            opcion = input("Elige una opcion: ")
            hazEl = inicio.acciones.inicio()

            if opcion == "1":
                hazEl.crear_rutina_con_ejercicios(identrenador)
            elif opcion == "2":
                hazEl.asignar_rutina_a_aprendiz()
            elif opcion == "3":
                hazEl.ver_rutinas()
            elif opcion == "4":
                hazEl.ver_progresos()
            elif opcion == "5":
                hazEl.crear_progreso(identrenador)
            elif opcion == "6":
                return
            else:
                print("\nOpcion no valida.")



    def accionesUsuario(self, idusuario):
        usuario = inicio_usuario.inicio.Inicio.identificarUsuario(idusuario)
                    
        if not usuario:
            print("\nTu usuario no esta registrado en el sistema.")
            return


        while True:
            print("""
            --- Panel del Usuario ---
            1 - Ver mi Rutina
            2 - Ver mi Progreso
            3 - Salir
            """)
            opcion = input("Elige una opcion: ")
            hazEl = inicio_usuario.acciones.Usuario()

            if opcion == "1":
                hazEl.mostrarRutina(idusuario)
            elif opcion == "2":
                hazEl.ver_progresos()
            elif opcion == "3":
                return
            else:
                print("\nOpcion no valida.")

        


        


    