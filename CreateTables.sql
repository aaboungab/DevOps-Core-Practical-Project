CREATE TABLE IF NOT EXISTS player(
    id	INTEGER NOT NULL AUTO_INCREMENT,
    position VARCHAR(20) NOT NULL,
    team VARCHAR(20) NOT NULL,
    name VARCHAR(6) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;