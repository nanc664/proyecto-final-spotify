 CREATE DATABASE de_DATOS;
CREATE DATABASE MusicaDB;
USE MusicaDB;

-- Tabla de géneros
CREATE TABLE Genero (
    id_genero INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla de artistas
CREATE TABLE Artista (
    id_artista INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL
);

-- Tabla de canciones
CREATE TABLE Cancion (
    id_cancion INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    duracion TIME NOT NULL, -- formato hh:mm:ss
    id_genero INT,
    id_artista INT,
    FOREIGN KEY (id_genero) REFERENCES Genero(id_genero),
    FOREIGN KEY (id_artista) REFERENCES Artista(id_artista)
);
INSERT INTO Cancion (titulo, duracion, id_genero, id_artista) VALUES
('Bohemian Rhapsody', '00:05:55', 1, 1),
('Hips Don''t Lie', '00:03:38', 2, 2),
('Vivir Mi Vida', '00:04:13', 3, 3);
