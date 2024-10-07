-- autoentreprise.sector definition

-- Drop table

-- DROP TABLE autoentreprise.sector;

CREATE TABLE autoentreprise.sector (
	code varchar(2) NOT NULL,
	"name" varchar NOT NULL,
	from_date date NULL,
	CONSTRAINT sector_pk PRIMARY KEY (code)
);