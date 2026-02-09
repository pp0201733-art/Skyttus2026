CREATE TABLE users(
user_id INT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(150) UNIQUE,
password VARCHAR(100) NOT NULL
);

CREATE TABLE orders(
order_id INT PRIMARY KEY,
user_id INT,
product_name VARCHAR(100),
order_amount DECIMAL(10,2),
FOREIGN KEY (user_id) REFERENCES
users(user_id)
);

CREATE INDEX idx_users_email ON users(email);

INSERT INTO users VALUES
(1,'Payal','payal@gmail.com','payal123'),
(2,'Hina','hina@gmail.com','hina321'),
(3,'Amit','amit@gmail.com','amit123');

INSERT INTO orders VALUES
(101,1,'Laptop',55000),
(102,2,'Mouse',500),
(103,3,'Mobile',20000);



CREATE VIEW user_order_summry AS
SELECT
	u.user_id,
	u.name,
	u.email,
	COUNT(o.order_id) AS total_orders,
	SUM(o.order_amount) AS total_amount
FROM users u
LEFT JOIN orders o
ON u.user_id = o.user_id
GROUP BY u.user_id, u.name, u.email;

SELECT * FROM user_order_summry;