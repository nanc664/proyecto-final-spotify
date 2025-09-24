from datetime import
from conexion import conexion cursor

# Insertar artista
def insertar_artista(nombre, pais):
    con = crear_conexion()
    cursor = con.cursor()
    cursor.execute("INSERT INTO artistas (nombre, pais) VALUES (%s, %s)", (nombre, pais))
    con.commit()
    con.close()
    print("Artista agregado")

# Insertar álbum
def insertar_album(titulo, anio, id_artista):
    con = crear_conexion()
    cursor = con.cursor()
    cursor.execute("INSERT INTO albumes (titulo, anio, id_artista) VALUES (%s, %s, %s)", (titulo, anio, id_artista))
    con.commit()
    con.close()
    print("Álbum agregado")

# Insertar canción
def insertar_cancion(titulo, duracion, id_album):
    con = crear_conexion()
    cursor = con.cursor()
    cursor.execute("INSERT INTO canciones (titulo, duracion, id_album) VALUES (%s, %s, %s)", (titulo, duracion, id_album))
    con.commit()
    con.close()
    print("Canción agregada")

# Consultar canciones
def consultar_canciones():
    con = crear_conexion()
    cursor = con.cursor()
    cursor.execute("SELECT canciones.titulo, albumes.titulo, artistas.nombre FROM canciones  JOIN albumes ON canciones.id_album = albumes.id_album JOIN artistas ON albumes.id_artista = artistas.id_artista")
    datos = cursor.fetchall()
    con.close()
    return datos

# Borrar canción
def borrar_cancion(id_cancion):
    con = crear_conexion()
    cursor = con.cursor()
    cursor.execute("DELETE FROM canciones WHERE id_cancion = %s", (id_cancion,))
    con.commit()
    con.close()
    print("canción eliminada")

# Importar canciones desde Excel
def importar_excel(ruta_excel):
    con = crear_conexion()
    cursor = con.cursor()
    df = pd.read_excel(ruta_excel)

    for _, fila in df.iterrows():
        cursor.execute("INSERT INTO canciones (titulo, duracion, id_album) VALUES (%s, %s, %s)",
                    (fila['titulo'], fila['duracion'], fila['id_album']))

    con.commit()
    con.close()
    print(f" Canciones importadas desde Excel")