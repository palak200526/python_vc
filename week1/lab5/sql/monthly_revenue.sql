-- Contains the query for calculating monthly revenue for one year.
SELECT strftime('%Y-%m', InvoiceDate) AS Month,
       SUM(Total) AS TotalRevenue
FROM Invoice
WHERE strftime('%Y', InvoiceDate) = '2012'
GROUP BY Month
ORDER BY Month;