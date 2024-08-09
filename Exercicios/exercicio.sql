-- Quais são o nome e país das cidades com mais de 400 anos desde sua independência?
SELECT c.Name AS CityName, p.Name AS CountryName
FROM city c
INNER JOIN country p ON c.CountryCode = p.Code
WHERE p.IndepYear <= 1624;

-- Quais são as nome, país, capital e densidades demográficas das cidades com mais de 1000000 de habitantes?
SELECT c.Name AS CityName, p.Name As CountryName, capitalCity.Name AS CountryCapital, 
(c.Population / p.SurfaceArea) AS PopulationDensity
FROM city c
INNER JOIN country p ON c.CountryCode = p.Code
LEFT JOIN city capitalCity ON p.Capital = capitalCity.ID
WHERE c.Population > 1000000;

-- Quais são os nomes e paises das 10 cidades com maior expectativa de vida?
SELECT c.Name AS CityName, p.Name AS CountryName 
FROM city c
INNER JOIN country p ON c.CountryCode = p.Code
ORDER BY p.LifeExpectancy
LIMIT 10;

-- Qual é o nome, capital e população médica dos 10 paises mais populosos?
WITH Top10Countries AS (
    SELECT p.Code, p.Name AS CountryName, p.Capital, p.Population
    FROM country p
    ORDER BY p.Population DESC
    LIMIT 10
)
SELECT 
    t.CountryName AS CountryName,
    c.Name AS CapitalName,
    t.Population / COUNT(t.Code) OVER () AS AveragePopulation
FROM Top10Countries t
INNER JOIN city c ON t.Capital = c.ID;
