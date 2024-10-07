-- autoentreprise.public_holiday definition

-- Drop table

-- DROP TABLE autoentreprise.public_holiday;

CREATE TABLE autoentreprise.public_holiday (
	"date" date NOT NULL,
	"name" varchar NULL,
	CONSTRAINT public_holiday_pk PRIMARY KEY (date)
);