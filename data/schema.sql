CREATE DATABASE pythonistas2017;

USE pythonistas2017;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE products (
  id_product int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  product varchar(100) NOT NULL,
  stock float NOT NULL,
  description varchar(200) NOT NULL,
  purchase_price float NOT NULL,
  price_sale float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO products(product,stock,description,purchase_price,price_sale) VALUES 
('Moto Maxx',10,'Motorola Moto Maxx',8500,10500 ),
('Pebble',100,'Pebble Red',1800,2000),
('Laptop Asus Mx34',5,'Laptop Asus i7 8GB Ram 1TB HHD',17000,21000);


INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);



SELECT * FROM users;
SELECT * FROM sessions;
SELECT * FROM products;
