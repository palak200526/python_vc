-- Revenue by Country from highest to lowest 
SELECT c.Country, SUM(i.Total) AS Revenue
FROM Customer c
JOIN Invoice i
    ON c.CustomerId = i.CustomerId
GROUP BY c.Country
ORDER BY Revenue DESC;