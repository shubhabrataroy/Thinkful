-- create weather table
CREATE TABLE weather (city text,year integer,warm_month text,cold_month text,average_high integer);

-- populate weather table
INSERT INTO weather (city,year,warm_month,cold_month,average_high) VALUES
    ('New York City',2013,'July','January',62),
    ('Boston',2013,'July','January',59),
    ('Chicago',2013,'July','January',59),
    ('Miami',2013,'August','January',84),
    ('Dallas',2013,'July','January',77),
    ('Seattle',2013,'July','January',61),
    ('Portland',2013,'July','December',63),
    ('San Francisco',2013,'September','December',64),
    ('Los Angeles',2013,'September','December',75);

-- count the number of rows
select count(*) from weather;

-- What cities were hottest in July in 2013?
select city from weather where warm_month = 'July';

-- What cities were hottest in July and not coldest in January?
select city from weather where warm_month = 'July' and cold_month != 'January';

-- The first two cities which were coldest in January
select city from weather where cold_month = 'January' ORDER BY average_high limit 2;
