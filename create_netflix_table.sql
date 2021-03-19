CREATE TABLE netflix_data2(
    show_id VARCHAR(5) NOT NULL ,
    type VARCHAR(20) ,
    title VARCHAR (100),
    director VARCHAR(10) NULL,
    cast_ VARCHAR (255),
    country VARCHAR (50),
    date_added VARCHAR (50),
    release_year SMALLINT (4),
    rating VARCHAR (50),
    duration VARCHAR (50),
    listed_in VARCHAR (50),
    description VARCHAR (255),

);

LOAD DATA INFILE 'netflix_titles.csv' 
INTO TABLE netflix_data 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS