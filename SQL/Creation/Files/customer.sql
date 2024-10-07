-- autoentreprise.customer definition

-- Drop table

-- DROP TABLE autoentreprise.customer;

CREATE TABLE autoentreprise.customer (
	code varchar NOT NULL,
	"name" varchar NOT NULL,
	phone varchar NULL,
	email varchar NULL,
	first_contact_date date NOT NULL,
	headquarters_address_id int8 NOT NULL,
	CONSTRAINT customer_pk PRIMARY KEY (code),
	CONSTRAINT customer_to_address_fk FOREIGN KEY (headquarters_address_id) REFERENCES autoentreprise.address(id)
);