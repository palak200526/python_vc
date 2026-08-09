-- Contains the query for finding the 10 best-selling tracks by quantity.
SELECT t.TrackId,
       t.Name,
       SUM(il.Quantity) AS TotalSold
FROM Track t
JOIN InvoiceLine il
ON t.TrackId = il.TrackId
GROUP BY t.TrackId, t.Name
ORDER BY TotalSold DESC
LIMIT 10;