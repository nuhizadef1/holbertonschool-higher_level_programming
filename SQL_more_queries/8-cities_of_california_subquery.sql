-- cities of california
SELECT id, name
FROM cities
WHERE name = (SELECT name FROM states WHERE name="California")
ORDER BY id ASC;
