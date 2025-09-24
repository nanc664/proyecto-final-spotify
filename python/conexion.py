from funciones import insertar_artista, insertar_album, insertar_cancion, consultar_canciones, borrar_cancion, importar_excel

def menu():
    while True:
        print(f"\nMenú Spotify ")
        print("1. Agregar artista")
        print("2. Agregar álbum")
        print("3. Agregar canción")
        print("4. Ver canciones")
        print("5. Eliminar canción")
        print("6. Importar canciones desde Excel")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del artista: ")
            pais = input("País: ")
            insertar_artista(nombre, pais)
        elif opcion == "2":
            titulo = input("Título del álbum: ")
            anio = int(input("Año: "))
            id_artista = int(input("ID del artista: "))
            insertar_album(titulo, anio, id_artista)
        elif opcion == "3":
            titulo = input("Título de la canción: ")
            duracion = int(input("Duración (segundos): "))
            id_album = int(input("ID del álbum: "))
            insertar_cancion(titulo, duracion, id_album)
        elif opcion == "4":
            canciones = consultar_canciones()
            for c in canciones:
                print(f"Canción: {c[0]}, Álbum: {c[1]}, Artista: {c[2]}")
        elif opcion == "5":
            id_cancion = int(input("ID de la canción a eliminar: "))
            borrar_cancion(id_cancion)
        elif opcion == "6":
            ruta_excel = input("Ruta del archivo Excel: ")
            importar_excel(ruta_excel)
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()