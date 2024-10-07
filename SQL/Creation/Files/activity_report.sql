-- autoentreprise.activity_report definition

-- Drop table

-- DROP TABLE autoentreprise.activity_report;

CREATE TABLE autoentreprise.activity_report (
	"date" date NOT NULL,
	business_day bool NOT NULL,
	mission_id int8 NOT NULL,
	first_half_morning int8 NULL,
	second_half_morning int8 NULL,
	first_half_afternoon int8 NULL,
	second_half_afternoon int8 NULL,
    description varchar NULL,
	total numeric NULL,
	CONSTRAINT activity_report_pk PRIMARY KEY (date, mission_id),
	CONSTRAINT activity_report_to_mission_fk FOREIGN KEY (mission_id) REFERENCES autoentreprise.mission(id)
);