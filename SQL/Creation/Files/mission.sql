-- autoentreprise.mission definition

-- Drop table

-- DROP TABLE autoentreprise.mission;

CREATE TABLE autoentreprise.mission (
	id int8 NOT NULL,
	customer_code varchar NOT NULL,
	address_id int8 NOT NULL,
	sector_code varchar NOT NULL,
	title varchar NULL,
	description varchar NULL,
	from_date date NOT NULL,
	to_date date NULL,
	CONSTRAINT mission_pk PRIMARY KEY (id),
	CONSTRAINT mission_to_address_fk FOREIGN KEY (address_id) REFERENCES autoentreprise.address(id),
	CONSTRAINT mission_to_customer_fk FOREIGN KEY (customer_code) REFERENCES autoentreprise.customer(code),
	CONSTRAINT mission_to_sector_fk FOREIGN KEY (sector_code) REFERENCES autoentreprise.sector(code)
);