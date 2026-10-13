import inicio.rutina as rutina


class inicio:

    
            def crear_rutina_con_ejercicios(self, identrenador):
                print("\n--- Crear nueva rutina ---")
                nombrerutina = input("Nombre de la rutina: ")

                niveles = rutina.Rutina.listarNiveles()
                print("\nNiveles disponibles:")
                for n in niveles:
                    print(f"{n[0]} - {n[1]}")
                idnivel = int(input("Elige el id del nivel: "))

                nueva_rutina = rutina.Rutina(nombrerutina=nombrerutina, identrenador=identrenador, idnivel=idnivel)
                idrutina = nueva_rutina.crearRutina()

                if not idrutina:
                    print("\nNo se pudo crear la rutina.")
                    return

                print(f"\nRutina '{nombrerutina}' creada correctamente.")

                while True:
                    print("""
                    1 - Agregar un ejercicio existente
                    2 - Crear y agregar un ejercicio nuevo
                    3 - Terminar de agregar ejercicios
                    """)
                    opcion = input("Elige una opcion: ")

                    if opcion == "1":
                        ejercicios = rutina.Rutina.listarEjercicios()
                        if not ejercicios:
                            print("\nNo hay ejercicios registrados todavia, crea uno nuevo.")
                            continue
                        print("\nEjercicios disponibles:")
                        for e in ejercicios:
                            print(f"{e[0]} - {e[1]} (series: {e[2]}, repeticiones: {e[3]})")
                        idejercicio = int(input("Id del ejercicio a agregar: "))
                        if rutina.Rutina.agregarEjercicioARutina(idrutina, idejercicio):
                            print("\nEjercicio agregado a la rutina.")

                    elif opcion == "2":
                        idejercicio = self.crear_ejercicio_nuevo()
                        if idejercicio and rutina.Rutina.agregarEjercicioARutina(idrutina, idejercicio):
                            print("\nEjercicio creado y agregado a la rutina.")

                    elif opcion == "3":
                        break
                    else:
                        print("\nOpcion no valida.")

                print(f"\nLa rutina '{nombrerutina}' quedo lista con sus ejercicios.")

            def crear_ejercicio_nuevo(self):
                nombre = input("Nombre del ejercicio: ")
                descripcion = input("Descripcion del ejercicio: ")
                url = input("URL de referencia (video o imagen): ")
                series = int(input("Numero de series: "))
                repeticiones = int(input("Numero de repeticiones: "))

                idmusculo = self.elegir_o_crear_musculo()
                idmaquina = self.elegir_o_crear_maquina()

                return rutina.Rutina.crearEjercicio(nombre, descripcion, url, idmusculo, idmaquina, series, repeticiones)

            def elegir_o_crear_musculo(self):
                musculos = rutina.Rutina.listarMusculos()
                print("\nMusculos disponibles:")
                for m in musculos:
                    print(f"{m[0]} - {m[1]}")
                print("0 - Crear un musculo nuevo")
                idmusculo = int(input("Elige el id del musculo (o 0 para crear uno nuevo): "))

                if idmusculo == 0:
                    nombremusculo = input("Nombre del nuevo musculo: ")

                    partes = rutina.Rutina.listarPartesDelCuerpo()
                    print("\nPartes del cuerpo disponibles:")
                    for p in partes:
                        print(f"{p[0]} - {p[1]}")
                    print("0 - Crear una parte del cuerpo nueva")
                    idparte = int(input("Elige el id de la parte del cuerpo (o 0 para crear una nueva): "))

                    if idparte == 0:
                        nombreparte = input("Nombre de la nueva parte del cuerpo: ")
                        idparte = rutina.Rutina.crearPartedelCuerpo(nombreparte)

                    idmusculo = rutina.Rutina.crearMusculo(nombremusculo, idparte)

                return idmusculo

            def elegir_o_crear_maquina(self):
                maquinas = rutina.Rutina.listarMaquinas()
                print("\nMaquinas disponibles:")
                for m in maquinas:
                    print(f"{m[0]} - {m[1]}")
                print("0 - Crear una maquina nueva")
                idmaquina = int(input("Elige el id de la maquina (o 0 para crear una nueva): "))

                if idmaquina == 0:
                    nombremaquina = input("Nombre de la nueva maquina: ")
                    idmaquina = rutina.Rutina.crearMaquina(nombremaquina)

                return idmaquina

            

            def asignar_rutina_a_aprendiz(self):
                print("\n--- Asignar rutina a un aprendiz ---")

                email = input("Correo del aprendiz al que quieres asignar la rutina: ")
                usuario_destino = rutina.Rutina.buscarUsuarioPorEmail(email)

                if not usuario_destino:
                    print("\nNo se encontro ningun usuario con ese correo.")
                    return

                rutinas = rutina.Rutina.listarRutinasDeEntrenador()
                if not rutinas:
                    print("\nAun no has creado ninguna rutina. Crea una primero.")
                    return

                print("\nTus rutinas:")
                for r in rutinas:
                    print(f"{r[0]} - {r[1]} (nivel: {r[2]})")

                idrutina = int(input("Id de la rutina que quieres asignar: "))
                fecha = input("Fecha de la rutina (AAAA-MM-DD): ")
                hora = input("Hora de la rutina (HH:MM): ")
                observaciones = input("Observaciones (opcional): ")
                idestado = self.elegir_o_crear_estado()

                resultado = rutina.Rutina.asignarRutina(usuario_destino[0], idrutina, fecha, hora, observaciones, idestado)

                if resultado:
                    print(f"\nRutina asignada correctamente a {usuario_destino[1]} {usuario_destino[2]}.")
                else:
                    print("\nNo se pudo asignar la rutina.")

            def elegir_o_crear_estado(self):
                estados = rutina.Rutina.listarEstados()
                print("\nEstados disponibles:")
                for e in estados:
                    print(f"{e[0]} - {e[1]}")
                print("0 - Crear un estado nuevo")
                idestado = int(input("Elige el id del estado (o 0 para crear uno nuevo): "))

                if idestado == 0:
                    nombreestado = input("Nombre del nuevo estado: ")
                    idestado = rutina.Rutina.crearEstado(nombreestado)

                return idestado

            def ver_rutinas(self):
                rutinas = rutina.Rutina.listarRutinasDeEntrenador()
                if not rutinas:
                    print("\nAun no has creado ninguna rutina.")
                    return

                print("\n--- Tus rutinas ---")
                for r in rutinas:
                    print(f"{r[0]} - {r[1]} (nivel: {r[2]})")
                    ejercicios = rutina.Rutina.listarEjerciciosDeRutina(r[0])
                    for e in ejercicios:
                        print(f"      -> {e[1]} (series: {e[2]}, repeticiones: {e[3]})")
    
    
            def crear_progreso(self, identrenador):
                email = input("Correo del aprendiz al que quieres asignar el progreso: ")
                usuario_destino = rutina.Rutina.buscarUsuarioPorEmail(email)

                if not usuario_destino:
                    print("\nNo se encontro ningun usuario con ese correo.")
                    return

                idusuario_destino = usuario_destino[0]

                seguimiento = input("Observaciones del Usuario: ")
                peso = float(input("Ingrese su peso en Kg: "))
                altura = float(input("Ingrese su altura en metros: "))
                grasacorporal = float(input("Ingrese su grasa corporal: "))
                progreso = rutina.Rutina(seguimiento=seguimiento, peso=peso, altura=altura, grasa_corporal=grasacorporal, identrenador=identrenador, idusuario=idusuario_destino)
                insertar_progreso = progreso.crearProgreso()

                if not insertar_progreso:
                    print("\nNo se pudo registrar el progreso.")
                    return

                print(f"\nProgreso asignado correctamente al usuario: '{email}'")


            def ver_progresos(self):
                print("\n--- Progreso de los Aprendices ---")
                progresos = rutina.Rutina.listarProgresoDeAprendiz()

                if not progresos:
                    print("\nAún no has registrado progresos para ningún aprendiz.")
                    return

                print("\n------------------------------------------------------------")
                for p in progresos:
                    nombre = p[0]
                    apellidos = p[1]
                    email = p[2]
                    observaciones = p[3]
                    peso = p[4]
                    altura = p[5]
                    grasa = p[6]

                    print(f"Aprendiz: {nombre} {apellidos} ({email})")
                    print(f"  -> Peso: {peso} Kg | Altura: {altura} m | Grasa Corporal: {grasa}%")
                    print(f"  -> Observaciones: {observaciones}")
                
    
        
    
        
    
    
    
    
    

