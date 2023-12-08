CREATE DATABASE IF NOT EXISTS complaint_management_system;
USE complaint_management_system;

DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    email VARCHAR(45) NOT NULL UNIQUE,
    phone_no VARCHAR(20) NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    role_type bool NOT NULL DEFAULT true,
    role_type ENUM("superadmin", "admin", "staff") NOT NULL,
    PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO user (email, password, role_type) VALUE ("admin@gmail.com", "admin", "superadmin");  

DROP TABLE IF EXISTS complaint_type;
CREATE TABLE complaint_type (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS complaint_status;
CREATE TABLE complaint_status (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(45) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO complaint_status (name) VALUES ("PENDING"), ("ASSIGNED"), ("DONE"), ("RESOLVED");

DROP TABLE IF EXISTS complaint;
CREATE TABLE complaint (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    title VARCHAR(45) NOT NULL,
    description VARCHAR(45) NOT NULL,
    complaint_type_id INT UNSIGNED NOT NULL,
    complaint_status_id INT UNSIGNED NOT NULL,
    assignee_id INT UNSIGNED NOT NULL,
    file_url TEXT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id),
    CONSTRAINT fk_complaint_type_id FOREIGN KEY (complaint_type_id) REFERENCES complaint_type(id),
    CONSTRAINT fk_complaint_status_id FOREIGN KEY (complaint_status_id) REFERENCES complaint_status(id),
    CONSTRAINT fk_complaint_assignee_id FOREIGN KEY (assignee_id) REFERENCES user(id)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

