CREATE ROLE redmine WITH LOGIN ENCRYPTED PASSWORD '%%SECRET:redminedb%%';
CREATE DATABASE redmine WITH ENCODING='UTF8' OWNER redmine;
-- See http://www.redmine.org/projects/redmine/wiki/redmineinstall#Supported-database-back-ends
ALTER DATABASE redmine SET datestyle="ISO,MDY";
