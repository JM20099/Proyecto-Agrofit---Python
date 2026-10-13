from usuarios import acciones


while True:
   import pyfiglet


   texto_grande = pyfiglet.figlet_format("AGROFIT")
   print(texto_grande)


   print("""
   Acciones disponibles:
      - Registro
      - Iniciar Sesion
   """)

   hazel = acciones.Acciones()        #Conectar una variable del archivo con una clase de otro archivo 

   accion = input("¿Que accion desea hacer?: ")

   if accion == "registro":
      hazel.registro()                     #Invocar la funcion que se guardo en la variable hanzel

   elif accion == "Iniciar Sesion":
      hazel.login()
   else:
      print("\nOpción no válida. Intenta de nuevo.")







