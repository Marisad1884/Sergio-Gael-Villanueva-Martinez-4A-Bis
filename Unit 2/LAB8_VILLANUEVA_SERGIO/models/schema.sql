CREATE DATABASE IF NOT EXISTS lab8_login
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE lab8_login;

CREATE TABLE IF NOT EXISTS users (
    id_user       INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username      VARCHAR(100) NOT NULL,
    password_user VARCHAR(255) NOT NULL,
    email         VARCHAR(100) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
