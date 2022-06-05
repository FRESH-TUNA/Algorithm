SELECT name "Customers"
FROM Customers
WHERE id NOT IN (
    SELECT customerid FROM ORDERS GROUP BY customerid
);
