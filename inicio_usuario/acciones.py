import inicio_usuario.inicio



class Usuario:
    
        def mostrarRutina(self, idusuario):
            rutinas = inicio_usuario.inicio.Inicio.obtenerEjerciciosPorUsuario(idusuario)

            if not rutinas:
                print("\nAún no tienes rutinas asignadas.")
                return

            print("\n--- Tus rutinas ---")
            
            for r in rutinas:
                nombrerutina = r[0]
                ejercicio = r[1]
                series = r[2]
                repeticiones = r[3]

                print(f"\nRutina: {nombrerutina}")

                print(f"  -> {ejercicio} (series: {series}, repeticiones: {repeticiones})")


        def ver_progresos(self):
            print("\n--- Progreso de los Aprendices ---")
            progresos = inicio_usuario.inicio.Inicio.listarProgresoDeAprendiz()

            if not progresos:
                print("\nAún no se te ha registrado tu progreso.")
                return

            print("\n------------------------------------------------------------")
            for p in progresos:
                nombre = p[0]
                apellidos = p[1]
                observaciones = p[2]
                peso = p[3]
                altura = p[4]
                grasa = p[5]

                print(f"{nombre} {apellidos}")
                print(f"  -> Peso: {peso} Kg | Altura: {altura} m | Grasa Corporal: {grasa}%") 
                print(f"  -> Observaciones: {observaciones}")

        


