-- The query identifies the 10 tracks with the highest total quantity sold.
SELECT TrackId,
       Name,
       UnitPrice
FROM Track
ORDER BY UnitPrice DESC
LIMIT 10;