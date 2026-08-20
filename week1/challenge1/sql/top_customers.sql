-- Top 5 customers by total spend
SELECT
    c.customerId, 
    c. firstName || ' ' || c.lastName AS CustomerName,
    SUM(i.total) AS TotalSpend
FROM Customer c 
JOIN Invoice i 
    ON c.customerId=i.customerId
GROUP BY c.customerId
ORDER BY TotalSpend DESC
LIMIT 5;