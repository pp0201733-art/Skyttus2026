 
DROP TABLE IF EXISTS account;

CREATE TABLE account(
		account_id INT PRIMARY KEY,
		name VARCHAR(50),
			balance INT
);




START TRANSACTION;

INSERT INTO account VALUES (3,'Payal',5000),(4,'Neha',3000);

UPDATE account
SET balance = balance - 1000
where name = 'Payal';

UPDATE account 
SET balance = balance + 1000
where name = 'Neha';

SELECT * FROM account;
COMMIT;
ROLLBACK;