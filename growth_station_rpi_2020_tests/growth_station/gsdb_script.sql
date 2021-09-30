-- https://stackoverflow.com/questions/13357760/mysql-create-user-if-not-exists

-- This account will be used by all local processes to access the database
CREATE USER IF NOT EXISTS 'basementFarmer'@'localhost' IDENTIFIED BY 'EnvS#310';

-- User: basementFarmer / EnvS#310

-- The following is the growth station database

DROP SCHEMA `gsdb` IF EXISTS;

CREATE SCHEMA `gsdb`;

CREATE TABLE `gsdb`.`readings` (
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
	source_id varchar(20),
	reading decimal(10,2),
	tstamp timestamp DEFAULT CURRENT_TIMESTAMP,
	backup boolean DEFAULT false
);

CREATE TABLE `gsdb`.`sources` (
	source_id varchar(20),
	source_desc varchar(100)
);

-- TODO: Add constraint between readings.source_id and sources.source_id

-- Modify the name of the database as well as the username
GRANT ALL ON `database`.* TO 'user'@'localhost' IDENTIFIED BY 'password';

INSERT INTO `gsdb`.`sources` (source_id, source_desc) VALUES ('AT','Ambient Temperature'), ('WT','Water Temperature');
INSERT INTO `gsdb`.`sources` (source_id, source_desc) VALUES ('ATT','Ambient Temperature Test Data'), ('WTT','Water Temperature Test Data');

-- Populating with some dummy data
INSERT INTO `envdb`.`readings` (source_id, reading) VALUES ('ATT', 23.4), ('WTT', 28.9);
