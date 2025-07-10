-- cities of california
SELECT cities.id, states.state_id, cities.name
FROM cities
WHERE name = (SELECT name FROM states WHERE name="California")
ORDER BY cities.id ASC;
