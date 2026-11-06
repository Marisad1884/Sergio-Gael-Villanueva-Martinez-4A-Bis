CREATE DATABASE IF NOT EXISTS login_system_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE login_system_db;

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

-- ---------------------------------------------------------------------------
-- Lab 9: tabla de productos para el módulo de exportación
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

INSERT IGNORE INTO productos (nombre, precio, stock) VALUES
    ('Teclado mecánico', 899.00, 25),
    ('Ratón inalámbrico', 349.50, 40),
    ('Monitor 24 pulgadas', 3299.00, 12),
    ('Memoria USB 64 GB', 159.90, 80),
    ('Cámara web HD', 549.00, 18),
    ('Audífonos con micrófono', 429.00, 33);
