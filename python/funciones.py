from conector import conexion, cursor

# Insertar artista
def insertar_artista(nombre, pais):
    cursor.execute("INSERT INTO artistas (nombre, pais) VALUES (%s, %s)", (nombre, pais))
    conexion.commit()
    conexion.close()
    print("Artista agregado")

# Insertar álbum
def insertar_album(titulo, anio, id_artista):
    cursor.execute("INSERT INTO albumes (titulo, anio, id_artista) VALUES (%s, %s, %s)", (titulo, anio, id_artista))
    conexion.commit()
    conexion.close()
    print("Álbum agregado")

# Insertar canción
def insertar_cancion(titulo, duracion, id_album):
    cursor.execute("INSERT INTO canciones (titulo, duracion, id_album) VALUES (%s, %s, %s)", (titulo, duracion, id_album))
    conexion.commit()
    conexion.close()
    print("Canción agregada")

# Consultar canciones
def consultar_canciones():
    cursor.execute("SELECT canciones.titulo, albumes.titulo, artistas.nombre FROM canciones  JOIN albumes ON canciones.id_album = albumes.id_album JOIN artistas ON albumes.id_artista = artistas.id_artista")
    datos = cursor.fetchall()
    conexion.close()
    return datos

# Borrar canción
def borrar_cancion(id_cancion):
    cursor.execute("DELETE FROM canciones WHERE id_cancion = %s", (id_cancion,))
    conexion.commit()
    conexion.close()
    print("canción eliminada")

# Importar canciones desde Excel
def importar_excel(ruta_excel):
    df = pd.read_excel(ruta_excel)

    for _, fila in df.iterrows():
        cursor.execute("INSERT INTO canciones (titulo, duracion, id_album) VALUES (%s, %s, %s)",
                    (fila['titulo'], fila['duracion'], fila['id_album']))

    conexion.commit()
    conexion.close()
    print(f" Canciones importadas desde Excel")