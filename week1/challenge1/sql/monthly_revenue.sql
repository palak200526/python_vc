-- Monthly revenue for 2012

SELECT
    strftime('%m', InvoiceDate) AS Month,
    SUM(Total) AS Revenue
FROM Invoice
WHERE strftime('%Y', InvoiceDate) = '2012'
GROUP BY strftime('%m', InvoiceDate)
ORDER BY Month;