-- autoentreprise.mission_customer definition

-- Drop table

-- DROP TABLE autoentreprise.mission_customer;

CREATE TABLE autoentreprise.mission_customer (
	mission_id int8 NOT NULL,
	parent_customer_code varchar NOT NULL,
	child_customer_code varchar NULL,
	invoiced_customer bool NOT NULL,
	CONSTRAINT mission_customer_pk PRIMARY KEY (mission_id, parent_customer_code),
	CONSTRAINT mission_customer_to_customer_fk FOREIGN KEY (parent_customer_code) REFERENCES autoentreprise.customer(code),
	CONSTRAINT mission_customer_to_mission_fk FOREIGN KEY (mission_id) REFERENCES autoentreprise.mission(id)
);