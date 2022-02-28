-- drop user if exist 
DROP USER IF EXISTS 'pysports_user'@'localhost';

-- create pysport_user and grant them all priviledges to the pysport database
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Password';

-- grant all priviledges to the pysport database to user pysport_user on localhost
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';

-- drop user if exist
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;


-- create the team table and set the foreign key
CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

-- create the player tablke and set the foreign key
CREATE TABLE player (
    player_id   INT             NOT NULL       AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY (player_id),
    CONSTRAINT fk_team
    FOREIGN KEY (team_id)
        REFERENCES team(team_id)
);



-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Team Gandalf', 'White Wizards'); 

INSERT INTO team(team_name, mascot)
    VALUES('Team Sauron', 'Orcs');     

-- insert player records 
INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Thorin', 'Oakenshield', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Bilbo', 'Baggins', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Frodo', 'Baggins', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Saruman', 'The White', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Angmar', 'Witch-king', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Azog', 'The Defiler', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));



-- inner join query 
SELECT player_id, first_name, last_name, team_name
FROM player
INNER JOIN team
    ON player.team_id = team.team_id;


-- left outer join query 
SELECT player_id, first_name, last_name, team_name
FROM player
LEFT OUTER JOIN team 
    ON player.team_id = team.team_id;

-- right outer join query
SELECT player_id, first_name, last_name, team_name
FROM player
RIGHT OUTER JOIN team
    ON player.team_id = team.team_id;

-- where clause 
SELECT  first_name, last_name
FROM player
WHERE player_id = 3;

-- sql update query 
UPDATE player
SET team_id = 2
    first_name = 'Gollum',
    last_name = 'Ring Stealer'
WHERE first_name = 'Smeagol';

-- sql delete query 
DELETE FROM player
WHERE first_name = 'Smeagol';




