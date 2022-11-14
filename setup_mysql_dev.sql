-- created database, user, password, sets up privileges


CREATE DATABASE IF NOT EXISTS arc_dev_db;
CREATE USER IF NOT EXISTS 'arc_dev'@'localhost' IDENTIFIED BY 'arc_dev_pwd';
GRANT ALL PRIVILEGES ON `arc_dev_db`.* TO 'arc_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'arc_dev'@'localhost';
FLUSH PRIVILEGES;
