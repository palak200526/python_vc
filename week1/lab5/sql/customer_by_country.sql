-- Contains the query for retrieving customers from a specified country.
SELECT CustomerId,
       FirstName,
       LastName,
       Email,
       Country
FROM Customer
WHERE Country = 'USA';