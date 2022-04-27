-- CREATE DATABASE IF NOT EXISTS nyc_subway;

CREATE USER nyc_subway_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE nyc_subway TO nyc_subway_admin
