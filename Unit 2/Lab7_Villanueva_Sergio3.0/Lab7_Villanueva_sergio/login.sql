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
