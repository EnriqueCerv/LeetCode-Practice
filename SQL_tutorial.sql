-------------
-- Billboard
-------------



-- Write a query that returns all rows for top-10 songs 
-- that featured either Katy Perry or Bon Jovi.
SELECT *   
FROM tutorial.billboard_top_100_year_end  
WHERE year_rank <= 10
  AND (artist = 'Bon Jovi' OR artist = 'Katy Perry');


-- Write a query that returns all songs with titles that 
-- contain the word "California" in either the 1970s or 1990s.
SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE 1970 <= year <= 1990
    AND song_name ILIKE '%California%';


-- Write a query that lists all top-100 recordings that feature 
-- Dr. Dre before 2001 or after 2009.
SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE  year_rank < 100
    -- AND (year <= 2001 OR year >= 2009)
    AND year NOT BETWEEN 2002 AND 2008
    AND artist = 'Dr. Dre';


-- Write a query that returns all rows for songs that were on the 
-- charts in 2013 and do not contain the letter "a".
SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE year = 2013
  AND song_name NOT ILIKE '%a%';


-- Write a query that returns all rows from 2012, ordered by song title from Z to A.
WHERE year = 2012
ORDER BY song_name DESC


-- Write a query that returns all rows from 2010 ordered by rank, 
-- with artists ordered alphabetically for each song.
SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE year = 2010
ORDER BY rank, artist


-- Write a query that shows all rows for which T-Pain was a group member, 
-- ordered by rank on the charts, from lowest to highest rank (from 100 to 1).
WHERE artist ILIKE '%T-Pain%'
ORDER BY year_rank DESC


-- Write a query that returns songs that ranked between 10 and 20 (inclusive) in 
-- 1993, 2003, or 2013. Order the results by year and rank, and leave a comment on 
-- each line of the WHERE clause to indicate what that line does
SELECT *
From tutorial.billboard_top_100_year_end
WHERE year IN (1993, 2003, 2013)
    AND 10 <= year_rank <= 20
ORDER BY year, year_rank




-------------
-- Housing
-------------



-- Write a query to select all of the columns in the tutorial.us_housing_units table without using *.
SELECT year,
    month, 
    month_name, 
    south, 
    west, 
    midwest, 
    northeast
From Tutorial.us_housing_units


-- Write a query to select all of the columns in tutorial.us_housing_units and 
-- rename them so that their first letters are capitalized.
SELECT year as Year,
    month as Month, 
    month_name as Month_name, 
    south as South, 
    west as West, 
    midwest as Midwest, 
    northeast as Northeast
From Tutorial.us_housing_units


-- Write a query that uses the LIMIT command to restrict the result set to only 15 rows.
SELECT *
FROM tutorial.us_housing_units
LIMIT 5


-- Did the West Region ever produce more than 50,000 housing units in one month?
SELECT *
FROM tutorial.us_housing_units 
WHERE west > 50


-- Did the South Region ever produce 20,000 or fewer housing units in one month?
WHERE south < 20


-- Write a query that only shows rows for which the month name is February.
WHERE month_name = 'February'


-- Write a query that only shows rows for which the month_name starts with the letter "N" or an earlier letter in the alphabet.
WHERE month_name < 'o'


-- Write a query that calculates the sum of all four regions in a separate column.
SELECT year,
       month,
       south, 
       west, 
       midwest, 
       northeast,
       south + west + midwest + northeast AS total_sum
FROM tutorial.us_housing_units


-- Write a query that returns all rows for which more units were produced in the West region than in the Midwest and Northeast combined.
SELECT *
FROM tutorial.us_housing_units
WHERE west > midwest + northeast


-- Write a query that calculates the percentage of all houses completed in the United States 
-- represented by each region. Only return results from the year 2000 and later.
SELECT year,
       month,
       south, 
       west, 
       midwest, 
       northeast,
       total_sum,
       south / total_sum * 100 AS south_pct,
       west / total_sum * 100 AS west_pct,
       midwest / total_sum * 100 AS midwest_pct,
       northeast / total_sum * 100 AS northeast_pct
FROM (
    SELECT year,
        month, 
        south, west, midwest, northeast,
        south + west + midwest + northeast AS total_sum
    FROM tutorial.us_housing_units
) subquery
WHERE year >= 2000;

SELECT year,
       month,
       west/(west + south + midwest + northeast)*100 AS west_pct,
       south/(west + south + midwest + northeast)*100 AS south_pct,
       midwest/(west + south + midwest + northeast)*100 AS midwest_pct,
       northeast/(west + south + midwest + northeast)*100 AS northeast_pct
FROM tutorial.us_housing_units
WHERE year >= 2000;




-------------
-- AAPL Shares
-------------


-- Calculate the total number of shares traded each month. Order your results chronologically.
SELECT year,
    month,
    SUM(volume) AS Total
FROM tutorial.aapl_historical_stock_price
GROUP BY year, month
ORDER BY year, month


-- Write a query to calculate the average daily price change in Apple stock, grouped by year.
SELECT year, 
    AVG(close - open) AS average_change
FROM tutorial.aapl_historical_stock_price
GROUP BY year
ORDER BY year


-- Write a query that calculates the lowest and highest prices that Apple stock achieved each month.
SELECT year, 
    month,
    MAX(high) as highest,
    MIN(low) as lowest
FROM tutorial.aapl_historical_stock_price
GROUP BY year, month
ORDER BY year, month




-------------
-- Billboard
-------------


-- Write a query that returns all rows for which Ludacris was a member of the group.
SELECT *
FROM tutorial.billboard_top_100_year_end
WHERE artist ILIKE 'Ludacris%'


-- Write a query that returns all rows for which the first artist listed in the group has a name that begins with "DJ".
WHERE artist ILIKE 'DJ%'