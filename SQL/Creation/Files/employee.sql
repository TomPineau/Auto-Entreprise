-- autoentreprise.employee definition

-- Drop table

-- DROP TABLE autoentreprise.employee;

CREATE TABLE autoentreprise.employee (
	id int8 NOT NULL,
	firstname varchar NOT NULL,
	lastname varchar NOT NULL,
	birthdate date NOT NULL,
	email varchar NOT NULL,
	address_id int8 NOT NULL,
	from_date date NOT NULL,
	to_date date NULL
);