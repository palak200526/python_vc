-- Contains the query for calculating total revenue per country.
SELECT c.Country,
       SUM(i.Total) AS TotalRevenue
FROM Customer c
JOIN Invoice i
ON c.CustomerId = i.CustomerId
GROUP BY c.Country
ORDER BY TotalRevenue DESC;