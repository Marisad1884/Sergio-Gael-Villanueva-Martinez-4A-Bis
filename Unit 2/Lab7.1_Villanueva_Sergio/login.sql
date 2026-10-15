CREATE DATABASE IF NOT EXISTS login_system_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE login_system_db;

-- ---------------------------------------------------------------
-- Tabla de usuarios
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    nombre VARCHAR(50) NOT NULL
);

-- La contraseña se guarda como hash SHA-256 (no en texto plano).
-- Usuario: admin   |   Contraseña: admin!123
INSERT IGNORE INTO users (username, password, nombre)
VALUES ('admin', SHA2('admin!123', 256), 'Super Admin');

-- ---------------------------------------------------------------
-- Lab 7.1 - Tabla de productos
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS products (
    id_product INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

-- Datos de ejemplo. Llevan id explícito + INSERT IGNORE para poder volver
-- a ejecutar el script sin duplicar filas.
INSERT IGNORE INTO products (id_product, nombre, precio, stock) VALUES
(1, 'Laptop HP',         12500.50, 10),
(2, 'Mouse Inalámbrico',   350.00, 25),
(3, 'Teclado Mecánico',    850.00, 15),
(4, 'Monitor HP',         4000.00, 10);
