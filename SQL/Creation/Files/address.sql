-- autoentreprise.address definition

-- Drop table

-- DROP TABLE autoentreprise.address;

CREATE TABLE autoentreprise.address (
	id int8 NOT NULL,
	address varchar NULL,
	zip_code int8 NULL,
	city varchar NULL,
	country varchar NULL,
	is_headquarters bool NULL,
	CONSTRAINT address_pk PRIMARY KEY (id)
);