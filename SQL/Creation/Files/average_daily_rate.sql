-- autoentreprise.average_daily_rate definition

-- Drop table

-- DROP TABLE autoentreprise.average_daily_rate;

CREATE TABLE autoentreprise.average_daily_rate (
	mission_id int8 NOT NULL,
	adr numeric NOT NULL,
	fee_amount numeric NULL,
	fee_unit varchar NULL,
	bonus_amount numeric NULL,
	bonus_unit varchar NULL,
	from_date date NOT NULL,
	to_date date NULL,
	CONSTRAINT average_daily_rate_pk PRIMARY KEY (mission_id, from_date),
	CONSTRAINT average_daily_rate_to_mission_fk FOREIGN KEY (mission_id) REFERENCES autoentreprise.mission(id)
);