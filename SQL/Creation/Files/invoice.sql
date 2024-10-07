-- autoentreprise.invoice definition

-- Drop table

-- DROP TABLE autoentreprise.invoice;

CREATE TABLE autoentreprise.invoice (
	"number" varchar NOT NULL,
	"date" date NOT NULL,
	amount numeric NOT NULL,
	customer_code varchar NOT NULL,
	address_id int8 NOT NULL,
	is_paid bool NOT NULL,
	delivery_date date NULL,
	payment_date date NULL,
	payment_method varchar NULL,
	CONSTRAINT invoice_pk PRIMARY KEY (number),
	CONSTRAINT invoice_to_address_fk FOREIGN KEY (address_id) REFERENCES autoentreprise.address(id),
	CONSTRAINT invoice_to_customer_fk FOREIGN KEY (customer_code) REFERENCES autoentreprise.customer(code)
);